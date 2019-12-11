import click
from imutils import paths

from src.utils.index import index_images

@click.command()
@click.option("--dataset", help="Path to directory of images of which to construct VP from.")
@click.option("--tree_path", prompt="VP tree name", help="Name of tree for pickle file.")
@click.option("--hash_path", prompt="Hash file name", help="Name of tree for pickle file.")

def build_tree(dataset, tree_path, hash_path):
    """Program that creates VP tree of hashed images."""
    imagePaths = list(paths.list_images(dataset))
    index_images(imagePaths, tree_path, hash_path)
        
if __name__ == '__main__':
    build_tree()


# USAGE
# python index_images.py --images 101_ObjectCategories --tree vptree.pickle --hashes hashes.pickle