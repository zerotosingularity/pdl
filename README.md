# Disclaimer: alpha - preview

# PDL - Python Download Library

High level library for downloading and unarchiving files.

# Install

```bash
$ pip install pdl
```

# How to use

```python

import pdl

# Download a file (zip, tar, tgz, tar.gz)
pdl.download(url, data_dir="data/", keep_download=False, overwrite_download=False, verbose=False)

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
$ pytest
```

For more details on pytest: [Getting started with pytest](https://docs.pytest.org/en/latest/getting-started.html).
