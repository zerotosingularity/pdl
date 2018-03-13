""" Tests for PDL """

import http.server
import threading

import os
import shutil

from pdl import pdl

PORT = 7972
URL = f"http://localhost:{PORT}/tests/fixtures/hello_tensorflow.zip"
DATA_DIR = "data/"

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


def test_pdl():
    """ Test for PDL """

    filename = pdl.get_filename(URL)
    file_location = pdl.get_file_location(DATA_DIR, filename)

    print(file_location)
    assert not os.path.exists(file_location)
    pdl.download(URL, DATA_DIR)


def stop_server():
    """ Stop HTTP server """

    httpd.shutdown()
