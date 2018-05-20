""" PDL Module download dataset archives """

import zipfile
import os
import tarfile

import requests

ZIP_EXTENSION = ".zip"
TAR_EXTENSION = ".tar"
TGZ_EXTENSION = ".tgz"
TAR_GZ_EXTENSION = ".tar.gz"

EMPTY_URL_ERROR = "ERROR: url parameter should not be empty."
FILE_FORMAT_ERROR = "ERROR: File format currently not supported."
FILENAME_ERROR = "ERROR: Filename could not be found."

# Dataset helpers (alphabetically) #


def cifar_100_matlab(data_dir="data/", keep_download=False,
                     overwrite_download=False, verbose=False, info_only=False):
    """ Download the cifar_100_matlab dataset
    more info: http://www.cs.utoronto.ca/~kriz/cifar.html"""
    if info_only:
        print(""" Download the cifar_100_matlab dataset
                 more info: http://www.cs.utoronto.ca/~kriz/cifar.html""")
    else:
        download("http://www.cs.utoronto.ca/~kriz/cifar-100-matlab.tar.gz",
                 data_dir, keep_download, overwrite_download, verbose)


def cifar_100_python(data_dir="data/", keep_download=False,
                     overwrite_download=False, verbose=False, info_only=False):
    """ Download the cifar_100_python dataset
    more info: http://www.cs.utoronto.ca/~kriz/cifar.html"""
    if info_only:
        print(""" Download the cifar_100_python dataset
                 more info: http://www.cs.utoronto.ca/~kriz/cifar.html""")
    else:
        download("http://www.cs.utoronto.ca/~kriz/cifar-100-python.tar.gz",
                 data_dir, keep_download, overwrite_download, verbose)


def cifar_10_matlab(data_dir="data/", keep_download=False,
                    overwrite_download=False, verbose=False, info_only=False):
    """ Download the cifar_10_matlab dataset
    more info: http://www.cs.utoronto.ca/~kriz/cifar.html"""
    if info_only:
        print(""" Download the cifar_10_matlab dataset
                 more info: http://www.cs.utoronto.ca/~kriz/cifar.html""")
    else:
        download("http://www.cs.utoronto.ca/~kriz/cifar-10-matlab.tar.gz",
                 data_dir, keep_download, overwrite_download, verbose)


def cifar_10_python(data_dir="data/", keep_download=False,
                    overwrite_download=False, verbose=False, info_only=False):
    """ Download the cifar_10_python dataset
    more info: http://www.cs.utoronto.ca/~kriz/cifar.html"""
    if info_only:
        print(""" Download the cifar_10_python dataset
                 more info: http://www.cs.utoronto.ca/~kriz/cifar.html""")
    else:
        download("http://www.cs.utoronto.ca/~kriz/cifar-10-python.tar.gz",
                 data_dir, keep_download, overwrite_download, verbose)


def coco_2014(data_dir="data/", keep_download=False,
              overwrite_download=False, verbose=False, info_only=False):
    """ Download the coco_2014 dataset
    more info: http://cocodataset.org/#download"""
    if info_only:
        print(""" Download the coco_2014 dataset
                 more info: http://cocodataset.org/#download""")
    else:
        download("http://images.cocodataset.org/annotations/image_info_test2014.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://images.cocodataset.org/annotations/annotations_trainval2014.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://images.cocodataset.org/zips/test2014.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://images.cocodataset.org/zips/val2014.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://images.cocodataset.org/zips/train2014.zip",
                 data_dir, keep_download, overwrite_download, verbose)


def coco_2015(data_dir="data/", keep_download=False,
              overwrite_download=False, verbose=False, info_only=False):
    """ Download the coco_2015 dataset
    more info: http://cocodataset.org/#download"""
    if info_only:
        print(""" Download the coco_2015 dataset
                 more info: http://cocodataset.org/#download""")
    else:
        download("http://images.cocodataset.org/annotations/image_info_test2015.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://images.cocodataset.org/zips/test2015.zip",
                 data_dir, keep_download, overwrite_download, verbose)


def coco_2017(data_dir="data/", keep_download=False,
              overwrite_download=False, verbose=False, info_only=False):
    """ Download the coco_2017 dataset
    more info: http://cocodataset.org/#download"""
    if info_only:
        print(""" Download the coco_2017 dataset
                 more info: http://cocodataset.org/#download""")
    else:
        download("http://images.cocodataset.org/annotations/image_info_unlabeled2017.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://images.cocodataset.org/annotations/image_info_test2017.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://images.cocodataset.org/annotations/stuff_annotations_trainval2017.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://images.cocodataset.org/annotations/annotations_trainval2017.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://images.cocodataset.org/zips/unlabeled2017.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://images.cocodataset.org/zips/test2017.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://images.cocodataset.org/zips/val2017.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://images.cocodataset.org/zips/train2017.zip",
                 data_dir, keep_download, overwrite_download, verbose)


def dogscats(data_dir="data/", keep_download=False,
             overwrite_download=False, verbose=False, info_only=False):
    """ Download the dogscats dataset
    more info: http://localhost:8888/notebooks/courses/dl1/lesson1.ipynb"""
    if info_only:
        print(""" Download the dogscats dataset
                 more info: http://localhost:8888/notebooks/courses/dl1/lesson1.ipynb""")
    else:
        download("http://files.fast.ai/data/dogscats.zip",
                 data_dir, keep_download, overwrite_download, verbose)


def gsvh_cropped(data_dir="data/", keep_download=False,
                 overwrite_download=False, verbose=False, info_only=False):
    """ Download the gsvh_cropped dataset
    more info: http://ufldl.stanford.edu/housenumbers/"""
    if info_only:
        print(""" Download the gsvh_cropped dataset
                 more info: http://ufldl.stanford.edu/housenumbers/""")
    else:
        download("http://ufldl.stanford.edu/housenumbers/extra_32x32.mat",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://ufldl.stanford.edu/housenumbers/test_32x32.mat",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://ufldl.stanford.edu/housenumbers/train_32x32.mat",
                 data_dir, keep_download, overwrite_download, verbose)


def gsvh_full(data_dir="data/", keep_download=False,
              overwrite_download=False, verbose=False, info_only=False):
    """ Download the gsvh_full dataset
    more info: http://ufldl.stanford.edu/housenumbers/"""
    if info_only:
        print(""" Download the gsvh_full dataset
                 more info: http://ufldl.stanford.edu/housenumbers/""")
    else:
        download("http://ufldl.stanford.edu/housenumbers/extra.tar.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://ufldl.stanford.edu/housenumbers/test.tar.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://ufldl.stanford.edu/housenumbers/train.tar.gz",
                 data_dir, keep_download, overwrite_download, verbose)


def imdb(data_dir="data/", keep_download=False,
         overwrite_download=False, verbose=False, info_only=False):
    """ Download the imdb dataset
    more info: https://datasets.imdbws.com/"""
    if info_only:
        print(""" Download the imdb dataset
                 more info: https://datasets.imdbws.com/""")
    else:
        download("https://datasets.imdbws.com/title.ratings.tsv.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://datasets.imdbws.com/title.principals.tsv.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://datasets.imdbws.com/title.episode.tsv.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://datasets.imdbws.com/title.crew.tsv.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://datasets.imdbws.com/title.basics.tsv.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://datasets.imdbws.com/title.akas.tsv.gz",
                 data_dir, keep_download, overwrite_download, verbose)


def mnist(data_dir="data/", keep_download=False,
          overwrite_download=False, verbose=False, info_only=False):
    """ Download the mnist dataset
    more info: http://yann.lecun.com/exdb/mnist/"""
    if info_only:
        print(""" Download the mnist dataset
                 more info: http://yann.lecun.com/exdb/mnist/""")
    else:
        download("http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz",
                 data_dir, keep_download, overwrite_download, verbose)


def mnist-fashion(data_dir="data/", keep_download=False,
                  overwrite_download=False, verbose=False, info_only=False):
    """ Download the mnist-fashion dataset
    more info: https://github.com/zalandoresearch/fashion-mnist"""
    if info_only:
        print(""" Download the mnist-fashion dataset
                 more info: https://github.com/zalandoresearch/fashion-mnist""")
    else:
        download("http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-labels-idx1-ubyte.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/t10k-images-idx3-ubyte.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-labels-idx1-ubyte.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://fashion-mnist.s3-website.eu-central-1.amazonaws.com/train-images-idx3-ubyte.gz",
                 data_dir, keep_download, overwrite_download, verbose)


def movie_lens_latest(data_dir="data/", keep_download=False,
                      overwrite_download=False, verbose=False, info_only=False):
    """ Download the movie_lens_latest dataset
    more info: http://files.grouplens.org/datasets/movielens/"""
    if info_only:
        print(""" Download the movie_lens_latest dataset
                 more info: http://files.grouplens.org/datasets/movielens/""")
    else:
        download("http://files.grouplens.org/datasets/movielens/ml-latest-small.zip",
                 data_dir, keep_download, overwrite_download, verbose)


def nfpa(data_dir="data/", keep_download=False,
         overwrite_download=False, verbose=False, info_only=False):
    """ Download the nfpa dataset
    more info: https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/"""
    if info_only:
        print(""" Download the nfpa dataset
                 more info: https://timebutt.github.io/static/how-to-train-yolov2-to-detect-custom-objects/""")
    else:
        download("https://timebutt.github.io/content/other/NFPA_dataset.zip",
                 data_dir, keep_download, overwrite_download, verbose)


def open-images-dataset-v4(data_dir="data/", keep_download=False,
                           overwrite_download=False, verbose=False, info_only=False):
    """ Download the open-images-dataset-v4 dataset
    more info: https://www.figure-eight.com/dataset/open-images-annotated-with-bounding-boxes/"""
    if info_only:
        print(""" Download the open-images-dataset-v4 dataset
                 more info: https://www.figure-eight.com/dataset/open-images-annotated-with-bounding-boxes/""")
    else:
        download("https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/zip_files/validation.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/zip_files/train_08.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/zip_files/train_07.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/zip_files/train_06.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/zip_files/train_05.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/zip_files/train_04.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/zip_files/train_03.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/zip_files/train_02.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/zip_files/train_01.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/zip_files/train_00.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://requestor-proxy.figure-eight.com/figure_eight_datasets/open-images/zip_files/test.zip",
                 data_dir, keep_download, overwrite_download, verbose)


def sentiment140(data_dir="data/", keep_download=False,
                 overwrite_download=False, verbose=False, info_only=False):
    """ Download the sentiment140 dataset
    more info: http://help.sentiment140.com/for-students/"""
    if info_only:
        print(""" Download the sentiment140 dataset
                 more info: http://help.sentiment140.com/for-students/""")
    else:
        download("http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip",
                 data_dir, keep_download, overwrite_download, verbose)


def twenty-newsgroups(data_dir="data/", keep_download=False,
                      overwrite_download=False, verbose=False, info_only=False):
    """ Download the twenty-newsgroups dataset
    more info: https://archive.ics.uci.edu/ml/machine-learning-databases/20newsgroups-mld/"""
    if info_only:
        print(""" Download the twenty-newsgroups dataset
                 more info: https://archive.ics.uci.edu/ml/machine-learning-databases/20newsgroups-mld/""")
    else:
        download("https://archive.ics.uci.edu/ml/machine-learning-databases/20newsgroups-mld/mini_newsgroups.tar.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://archive.ics.uci.edu/ml/machine-learning-databases/20newsgroups-mld/20newsgroups.html",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://archive.ics.uci.edu/ml/machine-learning-databases/20newsgroups-mld/20newsgroups.data.html",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://archive.ics.uci.edu/ml/machine-learning-databases/20newsgroups-mld/20_newsgroups.tar.gz",
                 data_dir, keep_download, overwrite_download, verbose)


def vqa-2015(data_dir="data/", keep_download=False,
             overwrite_download=False, verbose=False, info_only=False):
    """ Download the vqa-2015 dataset
    more info: http://www.visualqa.org/download.html"""
    if info_only:
        print(""" Download the vqa-2015 dataset
                 more info: http://www.visualqa.org/download.html""")
    else:
        download("http://visualqa.org/data/abstract_v002/scene_img/scene_img_abstract_v002_test2015.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/abstract_v002/scene_img/scene_img_abstract_v002_val2015.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/abstract_v002/scene_img/scene_img_abstract_v002_train2015.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/abstract_v002/vqa/Questions_Test_abstract_v002.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/abstract_v002/vqa/Questions_Val_abstract_v002.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/abstract_v002/vqa/Questions_Train_abstract_v002.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/abstract_v002/vqa/Annotations_Val_abstract_v002.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/abstract_v002/vqa/Annotations_Train_abstract_v002.zip",
                 data_dir, keep_download, overwrite_download, verbose)


def vqa-2016(data_dir="data/", keep_download=False,
             overwrite_download=False, verbose=False, info_only=False):
    """ Download the vqa-2016 dataset
    more info: http://www.visualqa.org/download.html"""
    if info_only:
        print(""" Download the vqa-2016 dataset
                 more info: http://www.visualqa.org/download.html""")
    else:
        download("http://visualqa.org/data/abstract_v002/scene_img/scene_img_abstract_v002_binary_val2017.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/abstract_v002/scene_img/scene_img_abstract_v002_binary_train2017.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/abstract_v002/vqa/Questions_Binary_Val2017_abstract_v002.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/abstract_v002/vqa/Questions_Binary_Train2017_abstract_v002.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/abstract_v002/vqa/Annotations_Binary_Val2017_abstract_v002.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/abstract_v002/vqa/Annotations_Binary_Train2017_abstract_v002.zip",
                 data_dir, keep_download, overwrite_download, verbose)


def vqa-2017(data_dir="data/", keep_download=False,
             overwrite_download=False, verbose=False, info_only=False):
    """ Download the vqa-2017 dataset
    more info: http://www.visualqa.org/download.html"""
    if info_only:
        print(""" Download the vqa-2017 dataset
                 more info: http://www.visualqa.org/download.html""")
    else:
        download("http://visualqa.org/data/mscoco/vqa/v2_Complementary_Pairs_Val_mscoco.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/mscoco/vqa/v2_Complementary_Pairs_Train_mscoco.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://msvocds.blob.core.windows.net/coco2015/test2015.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://msvocds.blob.core.windows.net/coco2014/val2014.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://msvocds.blob.core.windows.net/coco2014/train2014.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/mscoco/vqa/v2_Questions_Test_mscoco.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/mscoco/vqa/v2_Questions_Val_mscoco.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/mscoco/vqa/v2_Questions_Train_mscoco.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/mscoco/vqa/v2_Annotations_Val_mscoco.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://visualqa.org/data/mscoco/vqa/v2_Annotations_Train_mscoco.zip",
                 data_dir, keep_download, overwrite_download, verbose)


def yolo9000_weights(data_dir="data/", keep_download=False,
                     overwrite_download=False, verbose=False, info_only=False):
    """ Download the yolo9000_weights dataset
    more info: https://github.com/AlexeyAB/darknet#how-to-use"""
    if info_only:
        print(""" Download the yolo9000_weights dataset
                 more info: https://github.com/AlexeyAB/darknet#how-to-use""")
    else:
        download("http://pjreddie.com/media/files/yolo9000.weights",
                 data_dir, keep_download, overwrite_download, verbose)


def yolo_voc_weights(data_dir="data/", keep_download=False,
                     overwrite_download=False, verbose=False, info_only=False):
    """ Download the yolo_voc_weights dataset
    more info: https://github.com/AlexeyAB/darknet#how-to-use"""
    if info_only:
        print(""" Download the yolo_voc_weights dataset
                 more info: https://github.com/AlexeyAB/darknet#how-to-use""")
    else:
        download("http://pjreddie.com/media/files/yolo-voc.weights",
                 data_dir, keep_download, overwrite_download, verbose)


def yolov2_tiny_voc_weights(data_dir="data/", keep_download=False,
                            overwrite_download=False, verbose=False, info_only=False):
    """ Download the yolov2_tiny_voc_weights dataset
    more info: https://github.com/AlexeyAB/darknet#how-to-use"""
    if info_only:
        print(""" Download the yolov2_tiny_voc_weights dataset
                 more info: https://github.com/AlexeyAB/darknet#how-to-use""")
    else:
        download("http://pjreddie.com/media/files/yolov2-tiny-voc.weights",
                 data_dir, keep_download, overwrite_download, verbose)


def yolov2_tiny_weights(data_dir="data/", keep_download=False,
                        overwrite_download=False, verbose=False, info_only=False):
    """ Download the yolov2_tiny_weights dataset
    more info: https://github.com/AlexeyAB/darknet#how-to-use"""
    if info_only:
        print(""" Download the yolov2_tiny_weights dataset
                 more info: https://github.com/AlexeyAB/darknet#how-to-use""")
    else:
        download("https://pjreddie.com/media/files/yolov2-tiny.weights",
                 data_dir, keep_download, overwrite_download, verbose)


def yolov2_weights(data_dir="data/", keep_download=False,
                   overwrite_download=False, verbose=False, info_only=False):
    """ Download the yolov2_weights dataset
    more info: https://github.com/AlexeyAB/darknet#how-to-use"""
    if info_only:
        print(""" Download the yolov2_weights dataset
                 more info: https://github.com/AlexeyAB/darknet#how-to-use""")
    else:
        download("https://pjreddie.com/media/files/yolov2.weights",
                 data_dir, keep_download, overwrite_download, verbose)


def yolov3_weights(data_dir="data/", keep_download=False,
                   overwrite_download=False, verbose=False, info_only=False):
    """ Download the yolov3_weights dataset
    more info: https://github.com/AlexeyAB/darknet#how-to-use"""
    if info_only:
        print(""" Download the yolov3_weights dataset
                 more info: https://github.com/AlexeyAB/darknet#how-to-use""")
    else:
        download("https://pjreddie.com/media/files/yolov3.weights",
                 data_dir, keep_download, overwrite_download, verbose)


# PDL Core #


def download(url, data_dir="data/", keep_download=False,
             overwrite_download=False, verbose=False):
    """ Download and extract the archive from the url """

    is_archive = True

    if url == "":
        raise Exception(EMPTY_URL_ERROR)

    # Get filename from url
    echo("Get the filename from the supplied url", verbose)

    filename = get_filename(url)

    if filename == "" or filename is None:
        raise Exception(FILENAME_ERROR)

    file_location = get_file_location(data_dir, filename)
    echo(file_location, verbose)

    if os.path.exists(file_location) and not overwrite_download:
        echo(
            "The requested file: {filename} already exists in location: {file_location}. \
            Use: 'overwrite_download=True' to force overwrite"
            .format(filename=filename, file_location=file_location), True)
    else:
        echo(file_location, verbose)

        echo("Downloading: {url}".format(url=url), verbose)
        resp = requests.get(url, allow_redirects=True, stream=True)

        os.makedirs(data_dir, exist_ok=True)

        local_file = open(file_location, 'wb')

        local_file.write(resp.content)
        local_file.close()

        echo("finished downloading", verbose)

    if filename.endswith(ZIP_EXTENSION):
        echo("Extracting zip file.", verbose)
        zipf = zipfile.ZipFile(file_location, 'r')
        zipf.extractall(data_dir)
        zipf.close()

    elif(filename.endswith(TAR_EXTENSION) or
         filename.endswith(TAR_GZ_EXTENSION) or
         filename.endswith(TGZ_EXTENSION)):
        echo("Extracting tar file.", verbose)

        tar = tarfile.open(file_location, 'r')
        tar.extractall(data_dir)
        tar.close()
    else:
        is_archive = False
        echo("Not extracting: {filename}.".format(filename=filename))

    # Keep or remove downloaded file
    if not keep_download and is_archive:
        echo("Removing file: {filename}".format(filename=filename), verbose)
        os.remove(file_location)
    else:
        echo("Keeping the downloaded file.", verbose)


# Helper methods #


def echo(msg, debug=True):
    """ Print msg optionally """
    if debug:
        print(msg)


def get_filename(url):
    """ Get the filename of a url """
    return url[url.rfind("/")+1:]


def get_file_location(data_dir, filename):
    """ Concat data_dir and filename """
    return data_dir + filename
