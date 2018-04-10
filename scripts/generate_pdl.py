import requests
import os
import json
import http
from string import Template


DOUBLE_NEW_LINE = "\n\n"
PDL_START_DELIMITER = "# Dataset helpers (alphabetically) #"
PDL_END_DELIMITER = "# PDL Core #"


def generate_method(paramaters):
    dataset_download_template = Template(
        'def $method_name(data_dir="data/", keep_download=False,\n\
                    overwrite_download=False, verbose=False, info_only=False):\n\
    """ Download the $method_name dataset\n\
    more info: $page_url"""\n\
    if info_only:\n\
        print(""" Download the $method_name dataset\n \
                more info: $page_url""")\n\
    else:\n\
        download("$url",\n\
                data_dir, keep_download, overwrite_download, verbose)\n')

    generated_method = dataset_download_template.substitute(parameters)
    return generated_method


def append_download_url(parameters, method=None):
    append_download_url_template = Template(
        '        download("$url",\n\
                data_dir, keep_download, overwrite_download, verbose)\n')

    generated_code = append_download_url_template.substitute(parameters)

    if method is not None:
        method += generated_code
        return method
    else:
        return generated_code


r = requests.get("http://localhost:5000/api/dlurl")

if(r.status_code != requests.codes.ok):
    print("PDL: Url fetching failed, exiting...")
    exit(1)

# Construct list of tags

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

sorted_tag_list = {}

for key in sorted(tag_list):
    sorted_tag_list[key] = tag_list[key]

methods = ""

# Generate methods based on tags

for tag in sorted_tag_list:
    method = DOUBLE_NEW_LINE
    newMethod = True
    for url in sorted_tag_list[tag]:
        page_url = url["page_url"]
        url = url["url"]
        if newMethod:
            method_name = tag

            parameters = dict(
                method_name=method_name,
                page_url=page_url,
                url=url
            )

            method += generate_method(parameters)
            newMethod = False
        else:
            parameters = dict(
                url=url
            )
            method += append_download_url(parameters)

    methods += method
    # print(methods)

pdl = open("../pdl/pdl.py", "r").read()

start, rest = pdl.split(PDL_START_DELIMITER)
rest, end = rest.split(PDL_END_DELIMITER)

pdl_generated = start + PDL_START_DELIMITER + "\n"
pdl_generated += methods
pdl_generated += DOUBLE_NEW_LINE + PDL_END_DELIMITER + end

new_pdl = open("../pdl/pdl.py", "w")
new_pdl.write(pdl_generated)


# update pdl library

# update tests?

# add script to:
# run this script
# update version
# deploy
# commit & push
