const fs = require('fs');
const path = require('path');
const yaml = require('js-yaml');
const slugify = require('slugify');

// Load YAML file
const yamlPath = path.join(__dirname, '../_data/toolkit_resources.yml');
const yamlData = fs.readFileSync(yamlPath, 'utf8');
const resources = yaml.load(yamlData);

// Directory path for keyword files
const keywordDirectory = path.join(__dirname, '../_pages/keywords/');

// Remove existing files from keyword directory
fs.readdirSync(keywordDirectory).forEach(file => {
    const filePath = path.join(keywordDirectory, file);
    fs.unlinkSync(filePath);
    console.log(`Removed existing file: ${filePath}`);
});

// Iterate through resources and extract unique keywords
const uniqueKeywords = new Set();
resources.forEach(resource => {
    resource.keywords.forEach(keyword => uniqueKeywords.add(keyword));
});

// Generate files for each unique keyword
uniqueKeywords.forEach(keyword => {
    const slug = slugify(keyword, { lower: true });
    const filename = path.join(keywordDirectory, `${slug}.md`);
    const fileContent = `---
layout: keyword
permalink: /keywords/${slug}/
title: ${keyword}
---
`;
    fs.writeFileSync(filename, fileContent);
    console.log(`Generated file: ${filename}`);
});

console.log('Keyword files generated successfully.');
