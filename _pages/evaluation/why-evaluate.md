---
layout: evaluation-toolkit
permalink: /evaluation-toolkit/why-evaluate/
title: Why Evaluate?
---
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum</p>
<div class="grid-row grid-gap">
	<div class="mobile-lg:grid-col padding-2">
		<a class="usa-button btn-primary border-0 padding-keyword" href="{{site.baseurl}}/about/" aria-label="keyword">keyword</a>
	</div>
	<div class="mobile-lg:grid-col padding-2">
		<a class="usa-button btn-primary border-0 padding-keyword" href="{{site.baseurl}}/about/" aria-label="keyword">keyword</a>
	</div>
	<div class="mobile-lg:grid-col padding-2">
		<a class="usa-button btn-primary border-0 padding-keyword" href="{{site.baseurl}}/about/" aria-label="keyword">keyword</a>
	</div>
	<div class="mobile-lg:grid-col padding-2">
		<a class="usa-button btn-primary border-0 padding-keyword" href="{{site.baseurl}}/about/" aria-label="keyword">keyword</a>
	</div>
</div>
{% assign resources = site.data.evaluation-101 %}
{% for resource in resources%}
<div class="event-card padding-bottom-3 margin-top-1">
	<div class="grid-row clearfix shadow-5 radius-lg bg-white padding-2 flex-align-center">
		<div class="tablet:grid-col-12">
			<h3 class="title text-no-underline">{{resource.name}}</h3>
			<div class="text-base margin-bottom-1">
				<div class="margin-top-neg-105">
					{{resource.description}}
				</div>
			</div>
		</div>
		<div class="grid-row tablet:grid-col-12">
			<div class="grid-col-3 tablet:grid-col-3">
			<strong>Keywords</strong>
			<p class="margin-top-0">{{resource.keywords}}</p>
			</div>
			<div class="grid-col-3 tablet:grid-col-3">
			<strong>Format</strong>
			<p class="margin-top-0">{{resource.format}}</p>
			</div>
			{% if resource contains "source" %}
			<div class="grid-col-3 tablet:grid-col-3">
			<strong>Source</strong>
			<p class="margin-top-0">{{resource.source}}</p>
			</div>
			{% endif %}
			{% if resource contains "coverSheet" %}
			<div class="grid-col-3 tablet:grid-col-3">
			<strong>Cover Sheet</strong>
			<p class="margin-top-0">{{resource.coverSheet}}</p>
			</div>
			{% endif %}
		</div>
	</div>
</div>
{% endfor %}