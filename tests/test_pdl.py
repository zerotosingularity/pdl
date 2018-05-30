""" Tests for PDL """

import http.server
import threading

import os
import shutil
import pytest

from pdl import pdl

DATA_DIR = "data/"
TEST_FILE = "1_hello_tensorflow.py"
MAT_FILE = "data.mat"

PORT = 7972
URL = "http://localhost:{port}".format(port=PORT)

ZIP_URL = "{url}/tests/fixtures/hello_tensorflow.zip".format(url=URL)
TAR_GZ_URL = "{url}/tests/fixtures/hello_tensorflow.tar.gz".format(url=URL)
TAR_URL = "{url}/tests/fixtures/hello_tensorflow.tar".format(url=URL)
TGZ_URL = "{url}/tests/fixtures/hello_tensorflow.tgz".format(url=URL)
GZ_URL = "{url}/tests/fixtures/1_hello_tensorflow.py.gz".format(url=URL)

NON_ARCHIVE_URL = "{url}/tests/fixtures/{mat_file}".format(
    url=URL, mat_file=MAT_FILE)

EMPTY_URL = ""
URL_WITHOUT_FILE = URL + "/"

# pylint: disable=C0103
httpd = http.server.HTTPServer(
    ('', PORT), http.server.SimpleHTTPRequestHandler)
# pylint: disable=C0103
thread = threading.Thread(target=httpd.serve_forever)


def setup_module(module):
    # pylint: disable=W0612,W0613
    """ Setup function for test framework """

    print("setting up module")
    thread.start()


def teardown_module(module):
    # pylint: disable=W0612,W0613
    """ Tear down module """

    print("tearing down module")
    stop_server()

    print(os.getcwd())
    shutil.rmtree(DATA_DIR)


def test_zip_download():
    """ Test zip downlaod """

    pdl_test_helper(ZIP_URL)


def test_tar_gz_download():
    """ Test .tar.gz download """

    pdl_test_helper(TAR_GZ_URL)


def test_tar_download():
    """ Test tar download """

    pdl_test_helper(TAR_URL)


def test_tgz_download():
    """ Test .tgz download """

    pdl_test_helper(TGZ_URL)


def test_gz_download():
    """ Test .gz download """

    pdl_test_helper(GZ_URL)


def test_empty_url():
    """ Test an empty url """
    with pytest.raises(Exception):
        pdl_test_helper(EMPTY_URL)


def test_no_file_url():
    """ Test a url without a file """
    with pytest.raises(Exception):
        pdl_test_helper(URL_WITHOUT_FILE)


def test_no_archive_url():
    """ Test a non-archive url """
    pdl_test_helper(NON_ARCHIVE_URL, False)


@pytest.mark.skip(reason="only used for attribute error fixing")
def test_movie_lens_latest():
    """ Skipped test for movie lens; advised use for debugging only """
    try:
        pdl.movie_lens_latest()
    except AttributeError:
        pytest.fail("Unexpected error")


def pdl_test_helper(url, archive=True):
    """ Test for PDL """

    filename = pdl.get_filename(url)
    file_location = pdl.get_file_location(DATA_DIR, filename)

    print(file_location)
    assert not os.path.exists(file_location)
    pdl.download(url, DATA_DIR)

    test_file_location = pdl.get_file_location(DATA_DIR, TEST_FILE)

    assert os.path.exists(test_file_location)

    if archive:
        assert not os.path.exists(file_location)


def stop_server():
    """ Stop HTTP server """

    httpd.shutdown()
