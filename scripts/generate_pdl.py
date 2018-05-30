""" Add PDL helper methods based on the Zero to Singularity lnkr api """
import os
import json

from string import Template

import requests

MINIMAL_INFO_INDENT = 5
DOUBLE_NEW_LINE = "\n\n"
PDL_START_DELIMITER = "# Dataset helpers (alphabetically) #"
PDL_END_DELIMITER = "# PDL Core #"
PDL_BACKEND = "https://lnkr-api.zerotosingularity.com/api/dlurl"
USERNAME = os.environ["PDL_USERNAME"]
TOKEN = os.environ["PDL_TOKEN"]
README_DATASETS_DELIMITER = "# Datasets"


def generate_method(parameters):
    """ generates a helper method based on the parameters. """
    indent = (len(parameters["method_name"]) + MINIMAL_INFO_INDENT) * " "
    template_string = f'def $method_name(data_dir="data/", keep_download=False,\n\
{indent}overwrite_download=False, verbose=False, info_only=False):\n\
    """ Download the $method_name dataset\n\
    more info: $page_url"""\n\
    if info_only:\n\
        print(""" Download the $method_name dataset\n \
                more info: $page_url""")\n\
    else:\n\
        download("$url",\n\
                 data_dir, keep_download, overwrite_download, verbose)\n'

    dataset_download_template = Template(template_string)

    generated_method = dataset_download_template.substitute(parameters)
    return generated_method


def append_download_url(parameters, method=None):
    """ If a dataset requires multiple files to be downloaded,\
    this method simply appends the additional url."""
    append_download_url_template = Template(
        '        download("$url",\n\
                 data_dir, keep_download, overwrite_download, verbose)\n')

    generated_code = append_download_url_template.substitute(parameters)

    if method is not None:
        method += generated_code
        return method
    return generated_code


def generate():
    """ regenerate PDL """
    headers = {}
    headers["X-Session-User"] = USERNAME
    headers["X-Session-Token"] = TOKEN
    headers["Content-Type"] = "application/json"

    r = requests.get(PDL_BACKEND, headers=headers)

    if r.status_code != requests.codes.ok:
        print("PDL: Url fetching failed, exiting...")
        exit(1)

    # Construct list of tags

    tag_list = {}

    urls = json.loads(r.text)

    for url in urls:
        if url["tags"] is not None:
            matching = [u for u in url["tags"] if "pdl-" in u["title"]]

            for match in matching:
                # get title and strip "pdl-"
                title = match["title"][4:]

                if title not in tag_list:
                    tag_list[title] = []

                tag_list[title].append(url)

    sorted_tag_list = {}

    for key in sorted(tag_list):
        sorted_tag_list[key] = tag_list[key]

    methods = ""
    readme_datasets = ""

    # Generate methods and README Datasets section based on tags

    for tag in sorted_tag_list:
        method = DOUBLE_NEW_LINE
        new_method = True
        for url in sorted_tag_list[tag]:
            page_url = url["page_url"]
            url = url["url"]
            if new_method:
                method_name = tag

                parameters = dict(
                    method_name=method_name.replace("-", "_"),
                    page_url=page_url,
                    url=url
                )

                method += generate_method(parameters)
                new_method = False

                readme_dataset = f"* [{method_name}]({page_url})\n"
                readme_datasets += readme_dataset
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

    current_readme = open("../README.md", "r").read()

    readme_start, _ = current_readme.split(README_DATASETS_DELIMITER)

    generated_readme = readme_start
    generated_readme += README_DATASETS_DELIMITER + DOUBLE_NEW_LINE
    generated_readme += readme_datasets

    new_readme = open("../README.md", "w")

    new_readme.write(generated_readme)


generate()
