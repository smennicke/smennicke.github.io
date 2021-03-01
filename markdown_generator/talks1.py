import yaml
import io
import string

# load yaml files into data structures
with open("my_publications.yaml", 'r') as stream:
  bib = yaml.safe_load(stream)

# Writing Talks Files (also included in bib)
collection = "talks"
permastart = "/talks"
for i, talk in enumerate(bib, 1):
  if talk.get('type') == "Unpublished":
    # print(talk)
    date = talk.get('date')
    url_slug = talk.get('url_slug')

    md_filename = f"{date}-{url_slug}"

    talk_string = "---\n"
    talk_string += f'title: "{talk.get("title")}"\n'
    talk_string += f'collection: {collection}\n'
    # talk_string += f'type: {type}'
    talk_string += f'permalink: {permastart}/{md_filename}\n'
    # talk_string += f'venue: {venue}'
    talk_string += f'date: {date}\n'
    talk_string += f'location: {talk.get("place")}\n'
    talk_string += "---\n"

    with open(f"../_talks/{md_filename}.md", 'w') as f:
      f.write(talk_string)
