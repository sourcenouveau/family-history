---
layout: home
title: Dudley-Dixon Family History
subtitle: People, Places, and Events
---

The stories begin with my grandparents:

{% assign self_grandparents = "dudley-daniel-clifton-1920,tolsma-blanche-edith-1916,lubozynski-joseph-1923,dorazio-mary-rose-1924" | split: "," %}
{% for gp_key in self_grandparents %}
{% assign gp = site.data.people[gp_key] %}
- [{{ gp.name }}](/people/{{ gp.key }}.html) ({{ gp.birth_date | date: "%Y" }}–{{ gp.death_date | date: "%Y" }}) of {{ site.data.places[gp.birth_place_key].name }}
{% endfor %}

and my spouse's grandparents:

{% assign spouse_grandparents = "dixon-paul-bernard-1918,witheral-alice-rebecca-1920,hulslander-donald-eugene-1936,humphrey-eleanor-marie-1935" | split: "," %}
{% for gp_key in spouse_grandparents %}
{% assign gp = site.data.people[gp_key] %}
- [{{ gp.name }}](/people/{{ gp.key }}.html) ({{ gp.birth_date | date: "%Y" }}–{{ gp.death_date | date: "%Y" }}) of {{ site.data.places[gp.birth_place_key].name }}
{% endfor %}
