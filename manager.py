import click
import requests
import os

from imutils import paths
import pickle
import cv2

from src.utils.index import index_images
from src.utils.hash import dhash, hamming, convert_hash


@click.group()
def main():
   pass

@main.command()
@click.argument('dataset')
@click.argument('tree_path')
@click.argument('hash_path')
def current(dataset, tree_path, hash_path):
    """
    A little weather tool that shows you the current weather in a LOCATION of
    your choice. Provide the city name and optionally a two-digit country code.
    Here are two examples:
    1. London,UK
    2. Canmore
    You need a valid API key from OpenWeatherMap for the tool to work. You can
    sign up for a free account at https://openweathermap.org/appid.
    """
    imagePaths = list(paths.list_images(dataset))
    index_images(imagePaths, tree_path, hash_path)

@main.command()
@click.argument('query_dataset')
def config(query_dataset):
    """
    Store configuration values in a file.
    """

    tree = pickle.loads(open('tree.pickle', "rb").read())
    hashes = pickle.loads(open('hashes.pickle', "rb").read())

    for (i, imagePath) in enumerate(list(paths.list_images(query_dataset))):
        image = cv2.imread(imagePath)

        # compute the hash for the query image, then convert it
        queryHash = dhash(image)
        queryHash = convert_hash(queryHash)

        results = tree.get_all_in_range(queryHash, 10)
        results = sorted(results)

        # loop over the results
        for (d, h) in results:
            # grab all image paths in our dataset with the same hash
            resultPaths = hashes.get(h, [])
            print("[INFO] {} total image(s) with d: {}, h: {}".format(len(resultPaths), d, h), resultPaths)

            # loop over the result paths
            for resultPath in resultPaths:
                # load the result image and display it to our screen
                result = cv2.imread(resultPath)
                cv2.imshow("Duplicate", result)
                cv2.imshow("Original", image)
                if cv2.waitKey(0) == ord('d'):
                    print('Deleted')
                    print("duplicate file path:", imagePath)
                    os.remove(imagePath)

if __name__ == "__main__":
    main()