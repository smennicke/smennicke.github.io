import yaml
import io

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

with open("my_publications.yaml", 'r') as stream:
  bib = yaml.safe_load(stream)

# print(bib)

collection = "publications"
permastart = "/publication"
for i, pub in enumerate(bib,1):

  title = pub.get('title')
  authors = pub.get('authors')
  citekey = pub.get('id')

  # print(pub.get('issued'))
  year = pub.get('issued')[0].get('year')
  month = monthmap[pub.get('issued')[0].get('month')]
  url_slug = pub.get('url_slug')
  md_filename = f"{year}-{month}-{url_slug}.md"

  if (pub.get('proceedings')):
    venue = pub.get('proceedings')
  if (pub.get('journal')):
    venue = pub.get('journal')
  if (pub.get('school')):
    venue = pub.get('school')

  pub_string =  "---\n"
  pub_string += f'title: "{title}"\n'
  pub_string += f"collection: {collection}\n"
  pub_string += f"permalink: {permastart}/{year}-{citekey}\n"
  pub_string += f"venue: '{venue}'\n"
  pub_string += f"date: {year}-{month}-01\n"
  pub_string += f"coauthors:\n"
  for author in authors.split(" and "):
    if not author == 'Stephan Mennicke':
      pub_string += f"- name: {author}\n"
  pub_string += "---\n"

  with open(f"../_publications/{md_filename}", 'w') as f:
    f.write(pub_string)
