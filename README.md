# Disclaimer: alpha - preview

# PDL - Python Download Library

High level library for downloading and unarchiving files.

[Blog Post]()

# Install

```bash
$ pip install pdl
```

# How to use

## PDL Core

```python

from pdl import pdl

# Download a file (zip, tar, tgz, tar.gz)
pdl.download(url, data_dir="data/", keep_download=False, overwrite_download=False, verbose=False)

```

## Dataset helpers

Below you can find the current supported datasets with their simplest invocation. Of course, you can still specify the parameters from the core: data_dir, keep_download, overwrite_download, verbose:

```python
from pdl import pdl

# Download cifar-10 (http://www.cs.utoronto.ca/~kriz/cifar.html)
pdl.cifar_10()

# Example of more control, which can also be applied to the datasets below:
pdl.cifar_10(data_dir="my-data-dir/")
pdl.cifar_10(data_dir="my-data-dir/", verbose=True)
pdl.cifar_10(data_dir="my-data-dir/", overwrite_download=True, verbose=True)
pdl.cifar_10(data_dir="my-data-dir/", keep_download=True, verbose=True)
pdl.cifar_10(data_dir="my-data-dir/", keep_download=True, overwrite_download=True, verbose=True)
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
from pdl import pdl

# Get the file name from a url
pdl.get_filename(url)

# Get the location of a file
pdl.get_file_location(data_dir, filename)

```

# Tests

To run the tests from command line, simpy run:

```bash
$ pytest
```

For more details on pytest: [Getting started with pytest](https://docs.pytest.org/en/latest/getting-started.html).
