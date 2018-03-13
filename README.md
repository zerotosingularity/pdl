# Disclaimer: alpha - preview

# PDL - Python Download Library

High level library for downloading and unarchiving files.

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

```python
from pdl import pdl

# Download cifar-10 (http://www.cs.utoronto.ca/~kriz/cifar.html)
pdl.cifar_10()

# Download cifar-100 (http://www.cs.utoronto.ca/~kriz/cifar.html)
pdl.cifar_100()

# Download movie lens dataset(http://files.grouplens.org/datasets/movielens/)
pdl.movie_lens_latest()

# Download the Google Street View House numbers (http://ufldl.stanford.edu/housenumbers/)
pdl.gsv_house_numbers_full()
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
