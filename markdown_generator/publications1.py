import yaml
import io
import string

# prepare monthly mapping
monthmap = {
  "January": "01",
  "February": "02",
  "March": "03",
  "April": "04",
  "May": "05",
  "June": "06",
  "July": "07",
  "August": "08",
  "September": "09",
  "October": "10",
  "November": "11",
  "December": "12",
  "None": "01"
}

categorymap = {
  "inproceedings": "Conference/Workshop",
  "techreport": "Technical Report",
  "phdthesis": "PhD Thesis",
  "article": "Journal"
}

# load yaml files into data structures
with open("my_publications.yaml", 'r') as stream:
  bib = yaml.safe_load(stream)
with open("../_data/coauthors.yaml", 'r') as stream:
  coauth = yaml.safe_load(stream)

# print(coauth)
# print(bib)

# Writing Publications Files
collection = "publications"
permastart = "/publications"

temp_cos = list()
for i, pub in enumerate(bib,1):
  if pub.get('type') == "Unpublished":
    continue

  title = pub.get('title')
  authors = pub.get('authors')
  citekey = pub.get('id')

  category_string = ""
  if (pub.get('type')):
    ctype = pub.get('type').lower()
    category_string += f'"{categorymap.get(ctype)}"'
  abbrv = ""
  keyword_string = "["
  if pub.get('note'):
    abbrv = pub.get('note').lower()
    keyword_string += f"{abbrv},"
  if pub.get('keywords'):
    if abbrv.len():
      keyword_string += ','
    keyword_string += ','.join(pub.get('keywords').split(','))
  keyword_string += "]"

  # print(pub.get('issued'))
  year = pub.get('issued').get('year')
  month = monthmap[pub.get('issued').get('month')]
  url_slug = pub.get('url_slug')
  md_filename = f"{year}-{month}-{url_slug}"

  if (pub.get('proceedings')):
    venue = pub.get('proceedings')
  if (pub.get('journal')):
    venue = pub.get('journal')
  if (pub.get('school')):
    venue = pub.get('school')

  pub_string =  "---\n"
  pub_string += f'title: "{title}"\n'
  pub_string += f"collection: {collection}\n"
  pub_string += f"permalink: {permastart}/{md_filename}\n"
  pub_string += f"category: {category_string}\n"
  pub_string += f"tags: {keyword_string}\n"
  pub_string += f'venue: "{venue}"\n'
  pub_string += f"date: {year}-{month}-01\n"
  pub_string += f"coauthors:"
  for author in authors.split(" and "):
    author_slug = f"{author[0].lower()}{author.split(' ')[-1].lower()}"
    if author_slug == 'smennicke' or author_slug in temp_cos:
      continue
    elif not coauth.get(author_slug):
      temp_cos.append(author_slug)
      with open("../_data/coauthors.yaml", 'a+') as f:
        f.write(f"""{author_slug}:
  name: \"{author}\"
  affiliation:
  url:
""")
    pub_string += f"\n- {author_slug}"
  pub_string += "\n---\n"

  with open(f"../_publications/{md_filename}.md", 'w') as f:
    f.write(pub_string)

# Writing Talks Files (also included in bib)
collection = "talks"
permastart = "/talks"
for i, talk in enumerate(bib, 1):
  if talk.get('type') == "Unpublished":
    # print(talk)
    title = talk.get('title')
    date = talk.get('date')
    url_slug = talk.get('url_slug')

    md_filename = f"{date}-{url_slug}"

    talk_string = "---\n"
    talk_string += f'title: "{title}"\n'
    talk_string += f'collection: {collection}\n'
    # talk_string += f'type: {type}'
    talk_string += f'permalink: {permastart}/{md_filename}\n'
    # talk_string += f'venue: {venue}'
    talk_string += f'date: {date}\n'
    # talk_string += f'location: {location}\n'
    talk_string += "---\n"

    with open(f"../_talks/{md_filename}.md", 'w') as f:
      f.write(talk_string)
