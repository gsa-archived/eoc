---
layout: evaluation-toolkit
permalink: /evaluation-toolkit/non-evaluator/
title: Getting Started as a Non-Evaluator
---
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum</p>
{% assign resources = site.data.non-evaluator | group_by : "name" %}
{% assign size = resources| size %}
{% for i in (0..size) %}
{% assign resourcesList = resources[i].items %}
<div id="{{resourcesList[i].name| replace: ' ', '-'}}">
<h2 class="title margin-top-0 margin-bottom-0">{{resourcesList[0].name}}</h2>
{% for resource in resourcesList[0].resources %}
<div class="event-card padding-bottom-3 margin-top-1">
	<div class="grid-row clearfix shadow-5 radius-lg bg-white padding-2 flex-align-center">
		<div class="tablet:grid-col-12">
			<h3 class="title text-no-underline">{{resource.resourceName}}</h3>
			<div class="text-base margin-bottom-1">
				<div class="margin-top-neg-105">
					{{resource.description}}
				</div>
			</div>
		</div>
		<div class="grid-row tablet:grid-col-12">
			<div class="mobile-lg:grid-col-3">
			<strong>Format</strong>
			<p class="margin-top-0">{{resource.format}}</p>
			</div>
			<div class="mobile-lg:grid-col-3">
			<strong>Keywords</strong>
			<p class="margin-top-0">{{resource.keywords}}</p>
			</div>
			{% if resource contains "source" %}
			<div class="mobile-lg:grid-col-3">
			<strong>Source</strong>
			<p class="margin-top-0">{{resource.source}}</p>
			</div>
			{% endif %}
			{% if resource contains "coverSheet" %}
			<div class="mobile-lg:grid-col-3">
			<strong>Cover Sheet</strong>
			<p class="margin-top-0">{{resource.coverSheet}}</p>
			</div>
			{% endif %}
		</div>
	</div>
</div>
{% endfor %}
</div>
{% endfor %}

