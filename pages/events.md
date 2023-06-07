---
title: Events
datatable: true
custom_editme: pages/events/events.md
---



<a class="visually-hidden-focusable" href='#skip-tool-table'>Skip tool table</a>
<div class="table-responsive mt-4 mb-5">
  <table class="tooltable table display">
    <thead>
      <tr class="text-nowrap">
        <th>Event
          <a data-bs-toggle="tooltip"></a>
        </th>
        <th>Title</th>
        <th>Organisers</th>
        <th>Teachers</th>
        <th>Venue</th>
        <th>Date</th>
        <th>State</th>
      </tr>
    </thead>
    <tbody>
      {%- for page in site.pages %}
      {%- unless page.search_exclude == true %}
      {%- if page.event %}
      {%- assign actual_event = nil %}
      {%- for event in page.event %}
      {%- if training.name %}
      {%- assign actual_name = 1 %}
      {%- endif %}
      {%- endfor %}
      {%- endif %}
      {%- if actual_training %}
      {%- for training in page.training %}
      <tr>
        <td><a href="{{training.url | relative_url }}">{{training.name}}{%- if training.name == 'Training in TeSS'%} about {{page.title}}{%- endif %}</a></td>
        <td><a href="{{page.url | relative_url }}"><span class="badge default-badge">{{page.title}}</span></a></td>
      </tr>
      {%- endfor %}
      {%- endif %}
      {%- endunless %}
      {%- endfor %}      
    </tbody>
  </table>
</div>
<div id="skip-tool-table"></div>