---
key: us-federal-census-1930
title: United States Federal Census (1930)
---

The United States Federal Census of 1930 contains information about the population of the United States as of 1 April 1930.

### Records

{% assign sorted_records = "" | split: "" %}

{% for record_item in site.data.records[page.key] %}
  {% assign sorted_records = sorted_records | push: record_item[1] %}
{% endfor %}

{% assign sorted_records = sorted_records | sort: "name" %}

{% for record_item in sorted_records %}
- <a href="/records/{{ page.key }}/{{ record_item["key"] }}">{{ record_item["name"] }}</a>
{% endfor %}

Source Citation
Year: 1930; Census Place: Portville, Cattaraugus, New York; Page: 9A; Enumeration District: 0063; FHL microfilm: 2341144

Description
District: 0063; Description: PORTVILLE VILLAGE

Source Information
Ancestry.com. 1930 United States Federal Census [database on-line]. Provo, UT, USA: Ancestry.com Operations Inc, 2002.
Original data:United States of America, Bureau of the Census. Fifteenth Census of the United States, 1930. Washington, D.C.: National Archives and Records Administration, 1930. T626, 2,667 rolls.

Source Description
The 1930 Census contains records for approximately 123 million Americans. The census gives us a glimpse into the lives of Americans in 1930, and contains information about a household’s family members and occupants including: birthplaces, occupations, immigration, citizenship, and military service. The names of those listed in the census are linked to actual images of the 1930 Census.






### External Links

* Ancestry.com: [1930 United States Federal Census](https://www.ancestry.com/search/collections/6224/)
* FamilySearch: [United States Census, 1930](https://www.familysearch.org/search/collection/1810731)
* FamilySearch Research Wiki: [United States Census 1930](https://www.familysearch.org/en/wiki/United_States_Census_1930)
* U.S. National Archives and Records Administration: [1930 Federal Population Census](https://www.archives.gov/research/census/1930)
* Wikipedia: [1930 United States census](https://en.wikipedia.org/wiki/1930_United_States_census)


Original citation, in *Evidence Explained* format:

> TODO

Ancestry citation:

> Ancestry.com. *1930 United States Federal Census* [database on-line]. Provo, UT, USA: Ancestry.com Operations Inc, 2002.
> 
> Original data: United States of America, Bureau of the Census. *Fifteenth Census of the United States, 1930*. Washington, D.C.: National Archives and Records Administration, 1930. T626, 2,667 rolls.

FamilySearch citation:

> "United States Census, 1930." Database with images. *FamilySearch*. http://FamilySearch.org : 24 October 2022. Citing NARA microfilm publication T626. Washington, D.C.: National Archives and Records Administration, 2002.
