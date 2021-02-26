import os
import io
import string
import yaml

directory = "../_teaching/"
collection = "teaching"
permastart = "/teaching/"

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
  cid = crs.get('id')
  ctitle = crs.get('title')
  ckeywords = crs.get('keywords')
  ctype = crs.get('type')
  cschool = crs.get('school')
  cdepartment = crs.get('department')
  cinstitute = crs.get('institute')
  clocation = crs.get('location')

  csemester = sorted(crs.get('semester'), reverse=True)
  csemtop = csemester[0].split('-')
  if csemtop[1] == 'summer':
    cdate = f"{csemtop[0]}-04-01"
  else:
    cdate = f"{csemtop[0]}-10-01"

  url_slug = f"{csemester[0]}-{cid}"

  with open(f"../_teaching/{url_slug}.md", 'w') as f:
    f.write(
f'''---
title: "{ctitle}"
collection: {collection}
type: "{ctype}"
permalink: "{permastart}{url_slug}"
venue: "{cschool}, {cinstitute}"
date: {cdate}
location: {clocation}
---''')
