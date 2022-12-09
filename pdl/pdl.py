""" PDL Module download dataset archives """

import zipfile
import os
import tarfile
import gzip
import shutil
import requests


ZIP_EXTENSION = ".zip"
TAR_EXTENSION = ".tar"
TGZ_EXTENSION = ".tgz"
TAR_GZ_EXTENSION = ".tar.gz"
GZ_EXTENSION = ".gz"

EMPTY_URL_ERROR = "ERROR: url parameter should not be empty."
FILE_FORMAT_ERROR = "ERROR: File format currently not supported."
FILENAME_ERROR = "ERROR: Filename could not be found."


# Dataset helpers (alphabetically) #


def cats_dataset(data_dir="data/", keep_download=False,
                 overwrite_download=False, verbose=False, info_only=False):
    """ Download the cats_dataset dataset
    more info: https://web.archive.org/web/20150703060412/http://137.189.35.203/WebUI/CatDatabase/catData.html"""
    if info_only:
        print(""" Download the cats_dataset dataset
                 more info: https://web.archive.org/web/20150703060412/http://137.189.35.203/WebUI/CatDatabase/catData.html""")
    else:
        download("https://web.archive.org/web/20150703060412/http://137.189.35.203/WebUI/CatDatabase/Data/CAT_DATASET_02.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://web.archive.org/web/20150703060412/http://137.189.35.203/WebUI/CatDatabase/Data/CAT_DATASET_01.zip",
                 data_dir, keep_download, overwrite_download, verbose)


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


def glove_6b(data_dir="data/", keep_download=False,
             overwrite_download=False, verbose=False, info_only=False):
    """ Download the glove_6b dataset
    more info: """
    if info_only:
        print(""" Download the glove_6b dataset
                 more info: """)
    else:
        download("http://nlp.stanford.edu/data/glove.6B.zip",
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


def imagenette_160(data_dir="data/", keep_download=False,
                   overwrite_download=False, verbose=False, info_only=False):
    """ Download the imagenette_160 dataset
    more info: https://github.com/fastai/imagenette"""
    if info_only:
        print(""" Download the imagenette_160 dataset
                 more info: https://github.com/fastai/imagenette""")
    else:
        download("https://s3.amazonaws.com/fast-ai-imageclas/imagenette-160.tgz",
                 data_dir, keep_download, overwrite_download, verbose)


def imagenette_320(data_dir="data/", keep_download=False,
                   overwrite_download=False, verbose=False, info_only=False):
    """ Download the imagenette_320 dataset
    more info: https://github.com/fastai/imagenette"""
    if info_only:
        print(""" Download the imagenette_320 dataset
                 more info: https://github.com/fastai/imagenette""")
    else:
        download("https://s3.amazonaws.com/fast-ai-imageclas/imagenette-320.tgz",
                 data_dir, keep_download, overwrite_download, verbose)


def imagenette_full(data_dir="data/", keep_download=False,
                    overwrite_download=False, verbose=False, info_only=False):
    """ Download the imagenette_full dataset
    more info: https://github.com/fastai/imagenette"""
    if info_only:
        print(""" Download the imagenette_full dataset
                 more info: https://github.com/fastai/imagenette""")
    else:
        download("https://s3.amazonaws.com/fast-ai-imageclas/imagenette.tgz",
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


def joe_go(data_dir="data/", keep_download=False,
           overwrite_download=False, verbose=False, info_only=False):
    """ Download the joe_go dataset
    more info: https://pjreddie.com/projects/jgdb/"""
    if info_only:
        print(""" Download the joe_go dataset
                 more info: https://pjreddie.com/projects/jgdb/""")
    else:
        download("https://pjreddie.com/media/files/jgdb.tar.gz",
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


def mnist_csv(data_dir="data/", keep_download=False,
              overwrite_download=False, verbose=False, info_only=False):
    """ Download the mnist_csv dataset
    more info: https://pjreddie.com/projects/mnist-in-csv/"""
    if info_only:
        print(""" Download the mnist_csv dataset
                 more info: https://pjreddie.com/projects/mnist-in-csv/""")
    else:
        download("https://pjreddie.com/media/files/mnist_test.csv",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://pjreddie.com/media/files/mnist_train.csv",
                 data_dir, keep_download, overwrite_download, verbose)


def mnist_fashion(data_dir="data/", keep_download=False,
                  overwrite_download=False, verbose=False, info_only=False):
    """ Download the mnist_fashion dataset
    more info: https://github.com/zalandoresearch/fashion-mnist"""
    if info_only:
        print(""" Download the mnist_fashion dataset
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


def open_images_dataset_v4(data_dir="data/", keep_download=False,
                           overwrite_download=False, verbose=False, info_only=False):
    """ Download the open_images_dataset_v4 dataset
    more info: https://www.figure-eight.com/dataset/open-images-annotated-with-bounding-boxes/"""
    if info_only:
        print(""" Download the open_images_dataset_v4 dataset
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


def oxford_iiit_pet(data_dir="data/", keep_download=False,
                    overwrite_download=False, verbose=False, info_only=False):
    """ Download the oxford_iiit_pet dataset
    more info: http://www.robots.ox.ac.uk/~vgg/data/pets/"""
    if info_only:
        print(""" Download the oxford_iiit_pet dataset
                 more info: http://www.robots.ox.ac.uk/~vgg/data/pets/""")
    else:
        download("http://www.robots.ox.ac.uk/~vgg/data/pets/data/annotations.tar.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://www.robots.ox.ac.uk/~vgg/data/pets/data/images.tar.gz",
                 data_dir, keep_download, overwrite_download, verbose)


def pascal_voc_2007(data_dir="data/", keep_download=False,
                    overwrite_download=False, verbose=False, info_only=False):
    """ Download the pascal_voc_2007 dataset
    more info: https://pjreddie.com/projects/pascal-voc-dataset-mirror/"""
    if info_only:
        print(""" Download the pascal_voc_2007 dataset
                 more info: https://pjreddie.com/projects/pascal-voc-dataset-mirror/""")
    else:
        download("http://pjreddie.com/media/files/VOC2007_doc.pdf",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://storage.googleapis.com/coco-dataset/external/PASCAL_VOC.zip",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://pjreddie.com/media/files/VOCdevkit_08-Jun-2007.tar",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://pjreddie.com/media/files/VOCtest_06-Nov-2007.tar",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://pjreddie.com/media/files/VOCtrainval_06-Nov-2007.tar",
                 data_dir, keep_download, overwrite_download, verbose)


def pascal_voc_2012(data_dir="data/", keep_download=False,
                    overwrite_download=False, verbose=False, info_only=False):
    """ Download the pascal_voc_2012 dataset
    more info: https://pjreddie.com/projects/pascal-voc-dataset-mirror/"""
    if info_only:
        print(""" Download the pascal_voc_2012 dataset
                 more info: https://pjreddie.com/projects/pascal-voc-dataset-mirror/""")
    else:
        download("http://pjreddie.com/media/files/VOC2012_doc.pdf",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://pjreddie.com/media/files/VOCdevkit_18-May-2011.tar",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://pjreddie.com/media/files/VOC2012test.tar",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://pjreddie.com/media/files/VOCtrainval_11-May-2012.tar",
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


def standford_squad(data_dir="data/", keep_download=False,
                    overwrite_download=False, verbose=False, info_only=False):
    """ Download the standford_squad dataset
    more info: https://rajpurkar.github.io/SQuAD-explorer/"""
    if info_only:
        print(""" Download the standford_squad dataset
                 more info: https://rajpurkar.github.io/SQuAD-explorer/""")
    else:
        download("https://worksheets.codalab.org/rest/bundles/0xc83bf36cf8714819ba11802b59cb809e/contents/blob/",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://worksheets.codalab.org/rest/bundles/0xbcd57bee090b421c982906709c8c27e1/contents/blob/",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://rajpurkar.github.io/SQuAD-explorer/dataset/dev-v1.1.json",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://rajpurkar.github.io/SQuAD-explorer/dataset/train-v1.1.json",
                 data_dir, keep_download, overwrite_download, verbose)


def trec_1(data_dir="data/", keep_download=False,
           overwrite_download=False, verbose=False, info_only=False):
    """ Download the trec_1 dataset
    more info: https://trec.nist.gov/data/topics_eng/"""
    if info_only:
        print(""" Download the trec_1 dataset
                 more info: https://trec.nist.gov/data/topics_eng/""")
    else:
        download("https://trec.nist.gov/data/topics_eng/topics.51-100.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://trec.nist.gov/data/topics_eng/topics.1-50.gz",
                 data_dir, keep_download, overwrite_download, verbose)


def trec_2(data_dir="data/", keep_download=False,
           overwrite_download=False, verbose=False, info_only=False):
    """ Download the trec_2 dataset
    more info: https://trec.nist.gov/data/topics_eng/"""
    if info_only:
        print(""" Download the trec_2 dataset
                 more info: https://trec.nist.gov/data/topics_eng/""")
    else:
        download("https://trec.nist.gov/data/topics_eng/topics.101-150.gz",
                 data_dir, keep_download, overwrite_download, verbose)


def trec_3(data_dir="data/", keep_download=False,
           overwrite_download=False, verbose=False, info_only=False):
    """ Download the trec_3 dataset
    more info: https://trec.nist.gov/data/topics_eng/"""
    if info_only:
        print(""" Download the trec_3 dataset
                 more info: https://trec.nist.gov/data/topics_eng/""")
    else:
        download("https://trec.nist.gov/data/topics_eng/topics.151-200.gz",
                 data_dir, keep_download, overwrite_download, verbose)


def trec_4(data_dir="data/", keep_download=False,
           overwrite_download=False, verbose=False, info_only=False):
    """ Download the trec_4 dataset
    more info: https://trec.nist.gov/data/topics_eng/"""
    if info_only:
        print(""" Download the trec_4 dataset
                 more info: https://trec.nist.gov/data/topics_eng/""")
    else:
        download("https://trec.nist.gov/data/topics_eng/topics.201-250.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://trec.nist.gov/data/topics_eng/topics.trec4.routing.gz",
                 data_dir, keep_download, overwrite_download, verbose)


def trec_5(data_dir="data/", keep_download=False,
           overwrite_download=False, verbose=False, info_only=False):
    """ Download the trec_5 dataset
    more info: https://trec.nist.gov/data/topics_eng/"""
    if info_only:
        print(""" Download the trec_5 dataset
                 more info: https://trec.nist.gov/data/topics_eng/""")
    else:
        download("https://trec.nist.gov/data/topics_eng/topics.251-300.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://trec.nist.gov/data/topics_eng/topics.interactive.trec5.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://trec.nist.gov/data/topics_eng/topics.trec5.routing.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://trec.nist.gov/data/topics_eng/topics.confusion.cf1-cf50.gz",
                 data_dir, keep_download, overwrite_download, verbose)


def trec_6(data_dir="data/", keep_download=False,
           overwrite_download=False, verbose=False, info_only=False):
    """ Download the trec_6 dataset
    more info: https://trec.nist.gov/data/topics_eng/"""
    if info_only:
        print(""" Download the trec_6 dataset
                 more info: https://trec.nist.gov/data/topics_eng/""")
    else:
        download("https://trec.nist.gov/data/topics_eng/topics.301-350.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://trec.nist.gov/data/topics_eng/trec6.routing.topics.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://trec.nist.gov/data/topics_eng/topics.SDR1-SDR50.trec6.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://trec.nist.gov/data/topics_eng/answers.SDR1-SDR50.trec6.gz",
                 data_dir, keep_download, overwrite_download, verbose)


def trec_7(data_dir="data/", keep_download=False,
           overwrite_download=False, verbose=False, info_only=False):
    """ Download the trec_7 dataset
    more info: https://trec.nist.gov/data/topics_eng/"""
    if info_only:
        print(""" Download the trec_7 dataset
                 more info: https://trec.nist.gov/data/topics_eng/""")
    else:
        download("https://trec.nist.gov/data/topics_eng/topics.351-400.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://trec.nist.gov/data/topics_eng/trec7.sdr.gz",
                 data_dir, keep_download, overwrite_download, verbose)


def trec_8(data_dir="data/", keep_download=False,
           overwrite_download=False, verbose=False, info_only=False):
    """ Download the trec_8 dataset
    more info: https://trec.nist.gov/data/topics_eng/"""
    if info_only:
        print(""" Download the trec_8 dataset
                 more info: https://trec.nist.gov/data/topics_eng/""")
    else:
        download("https://trec.nist.gov/data/topics_eng/topics.401-450.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://trec.nist.gov/data/topics_eng/topics.qa_questions.txt",
                 data_dir, keep_download, overwrite_download, verbose)
        download("ftp://jaguar.ncsl.nist.gov/sdr99/SDR99-topics.sgml",
                 data_dir, keep_download, overwrite_download, verbose)


def trec_9(data_dir="data/", keep_download=False,
           overwrite_download=False, verbose=False, info_only=False):
    """ Download the trec_9 dataset
    more info: https://trec.nist.gov/data/topics_eng/"""
    if info_only:
        print(""" Download the trec_9 dataset
                 more info: https://trec.nist.gov/data/topics_eng/""")
    else:
        download("https://trec.nist.gov/data/topics_eng/qa_questions_201-893",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://trec.nist.gov/data/topics_eng/variants.qnumbers",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://trec.nist.gov/data/topics_eng/topics.451-500.gz",
                 data_dir, keep_download, overwrite_download, verbose)
        download("https://trec.nist.gov/data/topics_eng/variants.qnumbers",
                 data_dir, keep_download, overwrite_download, verbose)


def twenty_newsgroups(data_dir="data/", keep_download=False,
                      overwrite_download=False, verbose=False, info_only=False):
    """ Download the twenty_newsgroups dataset
    more info: https://archive.ics.uci.edu/ml/machine-learning-databases/20newsgroups-mld/"""
    if info_only:
        print(""" Download the twenty_newsgroups dataset
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


def uecfood_100(data_dir="data/", keep_download=False,
                overwrite_download=False, verbose=False, info_only=False):
    """ Download the uecfood_100 dataset
    more info: http://foodcam.mobi/dataset100.html"""
    if info_only:
        print(""" Download the uecfood_100 dataset
                 more info: http://foodcam.mobi/dataset100.html""")
    else:
        download("http://foodcam.mobi/dataset100.zip",
                 data_dir, keep_download, overwrite_download, verbose)


def uecfood_256(data_dir="data/", keep_download=False,
                overwrite_download=False, verbose=False, info_only=False):
    """ Download the uecfood_256 dataset
    more info: http://foodcam.mobi/dataset256.html"""
    if info_only:
        print(""" Download the uecfood_256 dataset
                 more info: http://foodcam.mobi/dataset256.html""")
    else:
        download("http://foodcam.mobi/dataset256.zip",
                 data_dir, keep_download, overwrite_download, verbose)


def vqa_2015(data_dir="data/", keep_download=False,
             overwrite_download=False, verbose=False, info_only=False):
    """ Download the vqa_2015 dataset
    more info: http://www.visualqa.org/download.html"""
    if info_only:
        print(""" Download the vqa_2015 dataset
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


def vqa_2016(data_dir="data/", keep_download=False,
             overwrite_download=False, verbose=False, info_only=False):
    """ Download the vqa_2016 dataset
    more info: http://www.visualqa.org/download.html"""
    if info_only:
        print(""" Download the vqa_2016 dataset
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


def vqa_2017(data_dir="data/", keep_download=False,
             overwrite_download=False, verbose=False, info_only=False):
    """ Download the vqa_2017 dataset
    more info: http://www.visualqa.org/download.html"""
    if info_only:
        print(""" Download the vqa_2017 dataset
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


def wikitext103(data_dir="data/", keep_download=False,
                overwrite_download=False, verbose=False, info_only=False):
    """ Download the wikitext103 dataset
    more info: http://files.fast.ai/models/wt103/"""
    if info_only:
        print(""" Download the wikitext103 dataset
                 more info: http://files.fast.ai/models/wt103/""")
    else:
        download("http://files.fast.ai/models/wt103/itos_wt103.pkl",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://files.fast.ai/models/wt103/fwd_wt103_enc.h5",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://files.fast.ai/models/wt103/fwd_wt103.h5",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://files.fast.ai/models/wt103/bwd_wt103_enc.h5",
                 data_dir, keep_download, overwrite_download, verbose)
        download("http://files.fast.ai/models/wt103/bwd_wt103.h5",
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

        echo(file_location, verbose)
        tar = tarfile.open(file_location, 'r')
        tar.extractall(data_dir)
        tar.close()

    elif filename.endswith(GZ_EXTENSION):
        echo("Extracting gz file.", verbose)

        out_file = file_location.strip(GZ_EXTENSION)

        with gzip.open(file_location, 'rb') as f_in:
            with open(out_file, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

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
    return os.path.join(data_dir, filename)
