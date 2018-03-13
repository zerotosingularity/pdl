import requests

import zipfile
import os
import tarfile

# TODO: constant naming in Python?
zip_extension = ".zip"
tar_extension = ".tar"
tgz_extension = ".tgz"
tar_gz_extension = ".tar.gz"


def download(url, data_dir="data/", keep_download=False, overwrite_download=False, verbose=False):

    # Get filename from url
    echo("Get the filename from the supplied url", verbose)

    filename = get_filename(url)

    file_location = f"{data_dir}{filename}"
    print(file_location)

    # TODO handle execeptions
    # - no url supplied
    # - no file name found
    # - only zip / tar / tar.gz are supported at the moment??
    # -- Should allow for other downloads as well

    if os.path.exists(file_location) and not overwrite_download:
        echo(
            f"The requested file: {filename} already exists in location: {file_location}", verbose)
    else:
        print(file_location)
        # download file
        # TODO see if file exists and overwrite file
        echo(f"Downloading: {url}", verbose)
        resp = requests.get(url, allow_redirects=True, stream=True)

        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        zfile = open(file_location, 'wb+')
        # TODO Puts the whole thing into memory, so need to look out for a better way to stream this to disk
        zfile.write(resp.content)
        zfile.close()

        echo("finished downloading", verbose)

    if filename.endswith(zip_extension):
        # unzip file
        echo("Extracting zip file.", verbose)
        zip = zipfile.ZipFile(file_location, 'r')
        zip.extractall(data_dir)
        zip.close()
    elif filename.endswith(tar_extension) or filename.endswith(tar_gz_extension) or filename.endswith(tgz_extension):
        echo("Extracting tar file.", verbose)

        tar = tarfile.open(file_location, 'r')
        tar.extractall(data_dir)
        tar.close()
    else:
        echo(f"No support for {filename} extraction.")

    # Keep or remove downloaded file
    if not keep_download:
        echo(f"Removing file: {filename}", verbose)
        os.remove(file_location)
    else:
        echo("Keeping the downloaded file.", verbose)


def echo(msg, on=True):
    if on:
        print(msg)


def get_filename(url):
    return url[url.rfind("/")+1:]


def get_filelocation(data_dir, filename):
    return f"{data_dir}{filename}"
