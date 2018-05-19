# Disclaimer: beta version

# PDL - Python Download Library

High level library for:
* download and unarchiving,
* discovering,

datasets.

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

from pdl import pdl

# Download a file (zip, tar, tgz, tar.gz)
pdl.download(url, data_dir="data/", keep_download=False, overwrite_download=False, verbose=False)

```

## Dataset helpers

Below you can find the current supported datasets with their simplest invocation. Of course, you can still specify the parameters from the core: data_dir, keep_download, overwrite_download, verbose. Additionally, you can use info_only to print info about the dataset.

```python
from pdl import pdl

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







# Datasets

* [cifar_100_matlab](http://www.cs.utoronto.ca/~kriz/cifar.html)
* [cifar_100_python](http://www.cs.utoronto.ca/~kriz/cifar.html)
* [cifar_10_matlab](http://www.cs.utoronto.ca/~kriz/cifar.html)
* [cifar_10_python](http://www.cs.utoronto.ca/~kriz/cifar.html)
* [coco_2014](http://cocodataset.org/#download)
* [coco_2015](http://cocodataset.org/#download)
* [coco_2017](http://cocodataset.org/#download)
* [dogscats](http://localhost:8888/notebooks/courses/dl1/lesson1.ipynb)
* [gsvh_cropped](http://ufldl.stanford.edu/housenumbers/)
* [gsvh_full](http://ufldl.stanford.edu/housenumbers/)
* [imdb](https://datasets.imdbws.com/)
* [mnist](http://yann.lecun.com/exdb/mnist/)
* [movie_lens_latest](http://files.grouplens.org/datasets/movielens/)
* [nfpa](https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/)
* [open-images-dataset-v4](https://www.figure-eight.com/dataset/open-images-annotated-with-bounding-boxes/)
* [yolo9000_weights](https://github.com/AlexeyAB/darknet#how-to-use)
* [yolo_voc_weights](https://github.com/AlexeyAB/darknet#how-to-use)
* [yolov2_tiny_voc_weights](https://github.com/AlexeyAB/darknet#how-to-use)
* [yolov2_tiny_weights](https://github.com/AlexeyAB/darknet#how-to-use)
* [yolov2_weights](https://github.com/AlexeyAB/darknet#how-to-use)
* [yolov3_weights](https://github.com/AlexeyAB/darknet#how-to-use)
