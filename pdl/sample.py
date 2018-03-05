# this file should be removed once the module can be installed or referenced
# from another directory

import pdl

url = "http://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
download_dir = "data"

pdl.pdl(url, download_dir, verbose=True)
