import click
import os

from imutils import paths
import pickle
import cv2

from src.utils.index import build_tree, climb_tree

DUPLICATE_DIRECTORY = 'duplicates/'


@click.group()
def main():
   pass


@main.command()
@click.argument('dataset')
@click.argument('tree_path')
@click.argument('hash_path')
def build(dataset, tree_path, hash_path):
    """
    Build a vantage point tree (https://en.wikipedia.org/wiki/Vantage-point_tree) of the supplied dataset, in O(n log n) time complexity.
    """
    image_paths = list(paths.list_images(dataset))
    if(image_paths):
        build_tree(image_paths, tree_path, hash_path, duplicate_dir=DUPLICATE_DIRECTORY)
    else:
        print('Error: No images found in query dataset.')


@main.command()
@click.argument('query_dataset')
def query(query_dataset):
    """
    Iterate(climb) through the established VPtree and determine the duplicate images that in the query dataset.
    """
    image_paths = list(paths.list_images(query_dataset))
    if(image_paths):
        try:
            tree = pickle.loads(open('tree.pickle', "rb").read())
            hashes = pickle.loads(open('hashes.pickle', "rb").read())
            climb_tree(image_paths, tree, hashes)
        except:
            print('Error: VPtree or hash file not found.')
    else:
        print('Error: No images found in query dataset.')
    
if __name__ == "__main__":
    main()