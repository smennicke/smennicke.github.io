---
title: "Prozessalgebra"
collection: teaching
type: "Graduate Course (M.Sc.)"
permalink: "/teaching/2017-winter-pa"
venue: "TU Braunschweig, Institut für Programmierung und Reaktive Systeme"
date: 2017-10-01
location: Braunschweig, Germany
roles:
  - name: Lecturer
    terms:
    - semester: winter
      year: 2014
    - semester: winter
      year: 2015
    - semester: winter
      year: 2016
    - semester: winter
      year: 2017
  - name: Tutor
    terms:
    - semester: winter
      year: 2011
    - semester: winter
      year: 2012
  - name: Tutor and Lecturer
    terms:
    - semester: winter
      year: 2013
  
keywords:
  - process algebra
  - process calculi
  - CCS
  - Petri nets
  - concurrency theory
  - verification
---

`{{ page.keywords | join: '``' }}`

## Terms by Role

{% for role in page.roles %}

### {{ role.name }}
{% for term in role.terms %}
  {% if term.url %}
  - [{{ term.semester | capitalize }} {{ term.year }}]({{ term.url }})
  {% else %}
  - {{ term.semester | capitalize }} {{ term.year }}
  {% endif %}
{% endfor %}

{% endfor %}
