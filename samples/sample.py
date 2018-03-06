# this file should be removed once the module can be installed or referenced
# from another directory

import pdl

#url = "http://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
url = "https://github.com/phayes/geoPHP/archive/1.2.tar.gz"
download_dir = "data"

pdl.pdl(url, download_dir, verbose=True)
