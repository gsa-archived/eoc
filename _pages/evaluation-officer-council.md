---
layout: wide
title: Interagency Council on Evaluation Policy
permalink: /interagency-council-on-evaluation-policy/
page_title: The Council
---

<div class="usa-layout-docs">
  {% include eoc-header.html %}
  <div class="grid-container">
    <div class="grid-row grid-gap">
        <div>
          {% for icep in site.data.icep %}
            <h2>{{icep.header}}</h2>
            {% for text in icep.body.contentText %}
                <p>{{text}}</p>
                {% if icep.body.contentText.length > 0 %}<br> {% endif %}
            {%endfor%}
            <ul>
              {% for eachList in icep.body.bullets %}
                <li>{{eachList.bullet}} </li>
              {%endfor%}
            </ul>
            {% if icep.key == 'membership' %}
              <p>ICEP membership is by application only. If you are interested in applying to serve or would like to learn more, please contact 
                <a href="mailto:evidence@omb.eop.gov" aria-label="Email Address (opens your default email application)">evidence@omb.eop.gov</a>
              .</p>
              <p> Federal employees can learn about upcoming ICEP events, including monthly evaluation office hours on the second Friday, by visiting 
                <a 
                  href="https://community.max.gov/x/wVkCgg" 
                  aria-label="Internal website (opens in a new window)"
                  target="_blank">this
                </a> 
                internal website (log-in required).</p>
            {% endif %}
          {%endfor%}
        </div>
    </div>
  </div>
</div>
