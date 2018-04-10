import requests
import os
import json
import http
from string import Template

r = requests.get("http://localhost:5000/api/dlurl")

if(r.status_code != requests.codes.ok):
    print("PDL: Url fetching failed, exiting...")
    exit(1)

tag_list = {}

urls = json.loads(r.text)

for url in urls:
    if url["tags"] is not None:
        matching = [u for u in url["tags"] if "pdl" in u["title"]]

        for m in matching:
            # get title and strip "pdl-"
            title = m["title"][4:]

            if title not in tag_list:
                tag_list[title] = []

            tag_list[title].append(url)

dataset_download_template = Template(
    'def $method_name(data_dir="data/", keep_download=False,\n\
                    overwrite_download=False, verbose=False, info_only=False): \n\
    """ Download the $method_name dataset\n\
    more info: $page_url"""\n\
    if info_only:\n\
        print(""" Download the $method_name dataset\n \
                more info: $page_url""")\n\
    else:\n\
        download("$url",\n\
                data_dir, keep_download, overwrite_download, verbose)')

for tag in tag_list:
    for url in tag_list[tag]:
        method_name = tag
        page_url = url["page_url"]
        url = url["url"]

        parameters = dict(
            method_name=method_name,
            page_url=page_url,
            url=url
        )

        method = dataset_download_template.substitute(parameters)
        print(method)

# print("-- taglist --")
# print(tag_list)

# for each tag:

# add a download for each url

# add generated text to header_template

# update pdl library

# update tests?

# add script to:
# run this script
# update version
# deploy
# commit & push
