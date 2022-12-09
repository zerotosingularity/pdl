# Disclaimer: beta version

# PDL - Public Download Library

High level library for:
* download and unarchiving,
* discovering,

datasets as well as pre-trained models for Transfer Learning.

[Read more in the blog post](https://www.zerotosingularity.com/posts/downloading-datasets-introducting-pdl/)

# Note: Adding your own datasets

The PDL library gets generated based on the scripts/generate.py script, which depends on the https://lnkr-api.zerotosingularity.com api, which is currently online but not yet publicly accessible. Feel free to contact me at jan@zerotosingularity.com if you want to have your dataset added.

# Install

```bash
$ pip install pdl
```

# How to use

## PDL Core

```python

import pdl

# Download a file (zip, tar, tgz, tar.gz)
pdl.download(url, data_dir="data/", keep_download=False, overwrite_download=False, verbose=False)

```

## Dataset helpers

Below you can find the current supported datasets with their simplest invocation. Of course, you can still specify the parameters from the core: data_dir, keep_download, overwrite_download, verbose. Additionally, you can use info_only to print info about the dataset.

```python
import pdl

# Download cifar-10 (http://www.cs.utoronto.ca/~kriz/cifar.html)
pdl.cifar_10()

# Example of more control, which can also be applied to the datasets below:
pdl.cifar_10(data_dir="my-data-dir/")
pdl.cifar_10(data_dir="my-data-dir/", verbose=True)
pdl.cifar_10(data_dir="my-data-dir/", overwrite_download=True, verbose=True)
pdl.cifar_10(data_dir="my-data-dir/", keep_download=True, verbose=True)
pdl.cifar_10(data_dir="my-data-dir/", keep_download=True, overwrite_download=True, verbose=True, info_only=False)
pdl.cifar_10("my-data-dir/", True, True, True)

# Download cifar-100 (http://www.cs.utoronto.ca/~kriz/cifar.html)
pdl.cifar_100()

# Download the Google Street View House (GSVH) numbers (http://ufldl.stanford.edu/housenumbers/)
pdl.gsvh_cropped()

# Download the Google Street View House (GSVH) numbers (http://ufldl.stanford.edu/housenumbers/)
pdl.gsvh_full()

# Download MNIST (http://yann.lecun.com/exdb/mnist/)
pdl.mnist()

# Download movie lens dataset(http://files.grouplens.org/datasets/movielens/)
pdl.movie_lens_latest()
```

## Helper methods

```python
import pdl

# Get the file name from a url
pdl.get_filename(url)

# Get the location of a file
pdl.get_file_location(data_dir, filename)

```

# Tests

To run the tests from command line, simpy run:

```bash
$ ./test.sh
```

This starts pytest to run all the tests. For more details on pytest: [Getting started with pytest](https://docs.pytest.org/en/latest/getting-started.html).


# Datasets

