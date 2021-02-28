---
title: "Relational Database Systems II"
category: Lectures
collection: teaching
type: "Graduate Course (M.Sc.)"
permalink: "/teaching/2019-summer-rdb2"
venue: "TU Braunschweig, Institut für Informationssysteme"
date: 2019-04-01
location: Braunschweig, Germany
roles:
  - name: Lecturer
    terms:
    - semester: summer
      url: http://www.ifis.cs.tu-bs.de/teaching/ss2019/rdb2
      year: 2019
  
tags: [database management systems,dbms,implementation techniques,query optimization,transaction management,ACID]
---


## Terms and Roles
{% for role in page.roles %}
  **{{ role.name }}:** {% for term in role.terms %}{% if term.url %}[{{ term.semester | capitalize }} {{ term.year }}]({{ term.url }}){% else %}{{ term.semester | capitalize }} {{ term.year }}{% endif %}{% unless forloop.last %}, {% endunless %}{% endfor %}
{% endfor %}
