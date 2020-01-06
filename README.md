# Image sorting

This repository is designed to create an tool that can be used to efficiently search index of images, from a base directory, for a duplicate when trying to add a new folder of images to the base directory. Images in the base directory are hashed, using a gradient-difference hash, and added to an index that is created with a Python implementation of VP-trees.

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

## Basic use

First we hash and create the index of the images in the base directory with the CLI command `build`, the image dataset path `train`, tree index file `tree.pickle` and the hash dictionary file `hashes.pickle`:

```
$ python test.py build dataset tree.pickle hashes.pickle
```

The resulting index and hashes is stored in a `pickle` file. Once this has been completed, we can search through the exisiting files, with the command `query` to see if duplicates exist within `my_data/`:

```
$ python test.py query query_dataset
```

## References

* [This](https://www.pyimagesearch.com/2019/08/26/building-an-image-hashing-search-engine-with-vp-trees-and-opencv/) blog post by Adrian Rosebrock at pyimagesearch.com. 
