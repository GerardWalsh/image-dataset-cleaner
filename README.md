# Image sorting

This repository is designed to create an tool that can be used to efficiently search index of images, from a base directory, for a duplicate when trying to add a new folder of images to the base directory. Images in the base directory are hashed, using a gradient-difference hash, and added to an index that is created with a Python implementation of VP-trees. 

A possible use case could be: an image dataset exists, to which images are to be added that were scraped from the website. Duplicates could be created by naaively adding all the scraped images to the dataset, due to the time sensitive nature of data (imformation is often reposted a website). Duplicates in a training set are not ideal and cause issues with model-fitting.

## Basic use

First we hash and create the index of the images in the base directory with the CLI command `current`, the image path `train`, tree index file `tree.pickle` and the hash dictionary file `hashes.pickle`:

```
$ python test.py current train tree.pickle hashes.pickle
```

The resulting index and hashes is stored in a `pickle` file. Once this has been completed, we can search through the exisiting files, with the command `config` to see if duplicates exist within `my_data/`:

```
$ python test.py config my_data/
```

## Setup

* Create a virtual environment `venv` with: 

```
$ python3 -m venv venv
```

* Activate the virtual environemnt and update the `pip` version:

```
$ source venv/bin/active
$ pip install -U pip
```

* Finally, install the requirements:

``` 
$ pip install -r requirements.txt
```