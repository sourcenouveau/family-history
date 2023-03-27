---
layout: default
title: About
---

<div class="is-pulled-right" style="width: 200px;">
  <figure class="image">
    <img src="/assets/images/michael-dudley-portrait.jpg">
  </figure>
</div>

My name is Michael Dudley and I am the author of this site.
I live with my family near Buffalo, New York and I'm employed as a software engineer.

Genealogy has been a lifelong hobby of mine, and much of my time has been spent accumulating facts and records.
I have been meticulous in my efforts to ensure that the information is accurate and supported by evidence.
When my father passed away several years ago I then shifted my focus toward creating something from that body of research.

This site is an ongoing project to tell my family's stories in a format that is interesting and easy to share.
If you find this site useful or have questions or feedback I'd love to hear from you.
Drop me a message at [michael@dudley-dixon.family](mailto:michael@dudley-dixon.family).

### Using This Site

This site has sections for the [people](/people), [places](/places), and [events](/events) in my family's history.
The main page for each section has an index for the individual pages in the section.
You can navigate quickly between pages using the links in the text.

You are welcome to use the information here for your own personal family research.
Content here is my original work so please do not copy it to other sites.
I provide citations you can use at the bottom of most pages, based on guidance in the excellent book *Evidence Explained*.
The citations look like this:

> Mills, Elizabeth Shown. *Evidence Explained: Citing History Sources from Artifacts to Cyberspace*. Third edition revised. Baltimore: Genealogical Publishing Company, 2017.

### Updates

I share news and updates from time to time, which you can find below.

{% for post in site.posts %}
#### [{{ post.title }} ({{ post.date | date_to_long_string: "ordinal", "US" }})]({{ post.url }})

{{ post.content | strip_html | truncatewords: 40 }} ([continue reading]({{ post.url }})).
{% endfor %}
