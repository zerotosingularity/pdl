import http.server
import socketserver
from multiprocessing import Process
from pdl import pdl
import os

PORT = 7972

p = None
url = f"http://localhost:{PORT}/tests/fixtures/hello_tensorflow.zip"
data_dir = "data"


def setup_module(module):
    print("setting up module")
    global p
    p = Process(target=start_server)
    p.start()


def teardown_module(module):
    print("tearing down module")
    stop_server()


def setup_function(function):
    print("setting up %s" % function)


def test_pdl():
    filename = pdl.get_filename(url)
    file_location = pdl.get_filelocation(data_dir, filename)

    assert not os.path.exists(file_location)
    pdl.download(url, data_dir, keep_download=True)


def start_server():
    Handler = http.server.SimpleHTTPRequestHandler

    httpd = socketserver.TCPServer(("", PORT), Handler)
    httpd.serve_forever()


def stop_server():
    print(p.pid)
    p.terminate()
    # assert False
