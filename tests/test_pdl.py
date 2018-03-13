""" Tests for PDL """

import http.server
import threading

import os
import shutil

from pdl import pdl

PORT = 7972

ZIP_URL = f"http://localhost:{PORT}/tests/fixtures/hello_tensorflow.zip"
TAR_GZ_URL = f"http://localhost:{PORT}/tests/fixtures/hello_tensorflow.tar.gz"
TAR_URL = f"http://localhost:{PORT}/tests/fixtures/hello_tensorflow.tar"
TGZ_URL = f"http://localhost:{PORT}/tests/fixtures/hello_tensorflow.tgz"

DATA_DIR = "data/"
TEST_FILE = "1_hello_tensorflow.py"

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


def setup_function(function):
    # pylint: disable=W0612,W0613
    """ Setup function """

    print("setting up %s" % function)


def test_zip_download():
    """ Test zip downlaod """

    pdl_helper(ZIP_URL)


def test_tar_gz_download():
    """ Test .tar.gz download """

    pdl_helper(TAR_GZ_URL)


def test_tar_download():
    """ Test tar download """

    pdl_helper(TAR_URL)


def test_tgz_download():
    """ Test .tgz download """

    pdl_helper(TGZ_URL)


def pdl_helper(url):
    """ Test for PDL """

    filename = pdl.get_filename(url)
    file_location = pdl.get_file_location(DATA_DIR, filename)

    print(file_location)
    assert not os.path.exists(file_location)
    pdl.download(url, DATA_DIR)

    test_file_location = pdl.get_file_location(DATA_DIR, TEST_FILE)

    assert os.path.exists(test_file_location)
    assert not os.path.exists(file_location)


def stop_server():
    """ Stop HTTP server """

    httpd.shutdown()
