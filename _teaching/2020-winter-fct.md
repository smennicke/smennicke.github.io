---
title: "Foundations of Complexity Theory"
category: Lectures
collection: teaching
type: "Graduate Course (M.Sc.)"
permalink: "/teaching/2020-winter-fct"
venue: "TU Dresden, Knowledge-Based Systems Group"
date: 2020-10-01
location: Dresden, Germany
roles:
  - name: Tutor
    terms:
    - semester: winter
      url: https://iccl.inf.tu-dresden.de/web/Complexity_Theory_(WS2020)
      year: 2020
  
tags: [theoretical computer science,complexity theory,Turing machines,computational models,foundations of computing]
---


## Terms and Roles
{% for role in page.roles %}
  **{{ role.name }}:** {% for term in role.terms %}{% if term.url %}[{{ term.semester | capitalize }} {{ term.year }}]({{ term.url }}){% else %}{{ term.semester | capitalize }} {{ term.year }}{% endif %}{% unless forloop.last %}, {% endunless %}{% endfor %}
{% endfor %}
