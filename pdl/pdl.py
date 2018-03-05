import requests

import zipfile
import os


def pdl(url, data_dir, keep_download=False, overwrite_download=False, verbose=False):

    # Get filename from url
    echo("Get the filename from the supplied url", verbose)

    filename = url[url.rfind("/")+1:]

    # TODO handle execeptions
    # - no url supplied
    # - no file name found
    # - only zip / tar / tar.gz are supported at the moment??
    # -- Should allow for other downloads as well
    echo(f"Got filename: {filename}", verbose)

    # download file
    # TODO see if file exists and overwrite file
    echo(f"Downloading: {url}", verbose)
    resp = requests.get(url, allow_redirects=True)

    zfile = open(filename, 'wb')
    zfile.write(resp.content)
    zfile.close()

    echo("finished downloading", verbose)

    # unzip file
    # TODO add support for tar.gz
    echo("Unzipping...", verbose)
    zip = zipfile.ZipFile(filename, 'r')
    zip.extractall(data_dir)
    zip.close()

    if not keep_download:
        echo(f"Removing file: {filename}", verbose)
        os.remove(filename)
    else:
        echo("Keeping the downloaded file.", verbose)


def echo(msg, on=True):
    if on:
        print(msg)

# TODO set global var for verbose?
