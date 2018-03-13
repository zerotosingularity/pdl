""" PDL Module download dataset archives """

import zipfile
import os
import tarfile

import requests

ZIP_EXTENSION = ".zip"
TAR_EXTENSION = ".tar"
TGZ_EXTENSION = ".tgz"
TAR_GZ_EXTENSION = ".tar.gz"

EMPTY_URL_ERROR = "ERROR: url parameter should not be empty."
FILE_FORMAT_ERROR = "ERROR: File format currently not supported."
FILENAME_ERROR = "ERROR: Filename could not be found."

### Dataset helpers (alphabetically) ###


def cifar_10():
    """ Download the CIFAR-10 dataset
    more info: http://www.cs.utoronto.ca/~kriz/cifar.html """
    download("http://www.cs.utoronto.ca/~kriz/cifar-10-python.tar.gz")


def cifar_100():
    """ http://www.cs.utoronto.ca/~kriz/cifar.html """
    download("http://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz")


def gsvh_full():
    """ Download the Google Street View House numbers
    more info: http://ufldl.stanford.edu/housenumbers/ """
    download("http://ufldl.stanford.edu/housenumbers/train.tar.gz")
    download("http://ufldl.stanford.edu/housenumbers/test.tar.gz")
    download("http://ufldl.stanford.edu/housenumbers/extra.tar.gz")


def gsvh_cropped():
    """ Download the Google Street View House numbers
    more info: http://ufldl.stanford.edu/housenumbers/ """
    download("http://ufldl.stanford.edu/housenumbers/train_32x32.mat")
    download("http://ufldl.stanford.edu/housenumbers/test_32x32.mat")
    download("http://ufldl.stanford.edu/housenumbers/extra_32x32.mat")


def mnist():
    """ http://yann.lecun.com/exdb/mnist/ """
    download("http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz")
    download("http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz")
    download("http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz")
    download("http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz")


def movie_lens_latest():
    """ Download the movie lens dataset
    more info: http: // files.grouplens.org/datasets/movielens / """
    download("http://files.grouplens.org/datasets/movielens/ml-latest-small.zip")


### PDL Core ###


def download(url, data_dir="data/", keep_download=False, overwrite_download=False, verbose=False):
    """ Download and extract the archive from the url """

    is_archive = True

    if url == "":
        raise Exception(EMPTY_URL_ERROR)

    # Get filename from url
    echo("Get the filename from the supplied url", verbose)

    filename = get_filename(url)

    if filename == "" or filename is None:
        raise Exception(FILENAME_ERROR)

    file_location = get_file_location(data_dir, filename)
    echo(file_location, verbose)

    if os.path.exists(file_location) and not overwrite_download:
        echo(
            f"The requested file: {filename} already exists in location: {file_location}. \
            Use: 'overwrite_download=True' to force overwrite", True)
    else:
        echo(file_location, verbose)

        echo(f"Downloading: {url}", verbose)
        resp = requests.get(url, allow_redirects=True, stream=True)

        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        zfile = open(file_location, 'wb')

        zfile.write(resp.content)
        zfile.close()

        echo("finished downloading", verbose)

    if filename.endswith(ZIP_EXTENSION):
        echo("Extracting zip file.", verbose)
        zipf = zipfile.ZipFile(file_location, 'r')
        zipf.extractall(data_dir)
        zipf.close()

    elif (filename.endswith(TAR_EXTENSION)
          or filename.endswith(TAR_GZ_EXTENSION)
          or filename.endswith(TGZ_EXTENSION)):
        echo("Extracting tar file.", verbose)

        tar = tarfile.open(file_location, 'r')
        tar.extractall(data_dir)
        tar.close()
    else:
        is_archive = False
        echo(f"Not extracting: {filename}.")

    # Keep or remove downloaded file
    if not keep_download and is_archive:
        echo(f"Removing file: {filename}", verbose)
        os.remove(file_location)
    else:
        echo("Keeping the downloaded file.", verbose)


### Helper methods ###


def echo(msg, debug=True):
    """ Print msg optionally """
    if debug:
        print(msg)


def get_filename(url):
    """ Get the filename of a url """
    return url[url.rfind("/")+1:]


def get_file_location(data_dir, filename):
    """ Concat data_dir and filename """
    return f"{data_dir}{filename}"
