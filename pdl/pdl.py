import requests

import zipfile
import os
import tarfile

zip_extension = ".zip"
tar_extension = ".tar"
tgz_extension = ".tgz"
tar_gz_extension = ".tar.gz"


def pdl(url, data_dir, keep_download=False, overwrite_download=False, verbose=False):

    # Get filename from url
    echo("Get the filename from the supplied url", verbose)

    filename = url[url.rfind("/")+1:]

    file_location = f"{data_dir}{filename}"

    # TODO handle execeptions
    # - no url supplied
    # - no file name found
    # - only zip / tar / tar.gz are supported at the moment??
    # -- Should allow for other downloads as well

    if os.path.exists(file_location) and not overwrite_download:
        echo(
            f"The requested file: {filename} already exists in location: {file_location}", verbose)
    else:
        # download file
        # TODO see if file exists and overwrite file
        echo(f"Downloading: {url}", verbose)
        resp = requests.get(url, allow_redirects=True)

        zfile = open(file_location, 'wb')
        zfile.write(resp.content)
        zfile.close()

        echo("finished downloading", verbose)

    if filename.endswith(zip_extension):
        # unzip file
        # TODO add support for tar.gz
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

# TODO set global var for verbose?
