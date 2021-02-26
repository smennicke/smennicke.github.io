import sys
import os
import io
import string
import yaml

directory = "../_teaching/"
collection = "teaching"
permastart = "/teaching/"

semester2date = {
  'winter': '10-01',
  'summer': '04-01'
}

contents = """
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

{% endfor %}"""

#1 - remove all teaching files
for f in os.listdir(directory):
  os.remove(f"{directory}{f}")
os.rmdir(directory)
os.mkdir(directory)

#2 - load yaml files into data structures
with open("../_data/teaching.yaml", 'r') as stream:
  courses = yaml.safe_load(stream)

#3 - Writing Publications Files
for i, crs in enumerate(courses,1):
  cid = crs.get('id').lower()
  ctitle = crs.get('title')

  # Create Role String + Obtain most recent term for ordering
  croles = crs.get('roles')
  role_string = "roles:"
  for line in yaml.dump(croles).split('\n'):
    role_string += f"\n  {line}"
  recent_year = 0
  recent_semester = ""
  for role in croles:
    for term in role.get('terms'):
      if recent_year == term.get('year') and recent_semester == 'summer':
        recent_semester = term.get('semester')
      if recent_year < term.get('year'):
        recent_year = term.get('year')
        recent_semester = term.get('semester')
  cdate = f"{recent_year}-{semester2date.get(recent_semester)}"

  ckeywords = crs.get('keywords')
  keywords_string = f"tags: [{ ','.join(ckeywords) }]"

  ctype = crs.get('type')
  cschool = crs.get('school')
  cdepartment = crs.get('department')
  cinstitute = crs.get('institute')
  clocation = crs.get('location')

  url_slug = f"{recent_year}-{recent_semester}-{cid}"

  with open(f"../_teaching/{url_slug}.md", 'w') as f:
    f.write(
f'''---
title: "{ctitle}"
category: {crs.get('category')}
collection: {collection}
type: "{ctype}"
permalink: "{permastart}{url_slug}"
venue: "{cschool}, {cinstitute}"
date: {cdate}
location: {clocation}
{role_string}
{keywords_string}
---

{contents}
''')
