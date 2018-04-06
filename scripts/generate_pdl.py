import requests
import os
import json
import http

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
            if m["title"] not in tag_list:
                tag_list[m["title"]] = []

            tag_list[m["title"]].append(url)

print("-- taglist --")
print(tag_list)

# for each tag:
# remove pdl-
# generate method based on tag name
# add description + parent url
# add a download for each url

# add generated text to header_template

# update pdl library

# update tests?

# add script to:
# run this script
# update version
# deploy
# commit & push
