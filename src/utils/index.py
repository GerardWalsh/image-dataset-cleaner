""""
Written by A Rosebrock: https://www.pyimagesearch.com/2019/08/26/building-an-image-hashing-search-engine-with-vp-trees-and-opencv/
"""

import pickle
import vptree
import cv2

from src.utils.hash import convert_hash, hamming, dhash
from src.utils.duplicates import handle_duplicate

def index_images(imagePaths, tree_name, hash_name, duplicate_dir):

	hashes = {}

	# loop over the image paths
	for (i, imagePath) in enumerate(imagePaths):
		# load the input image
		print("[INFO] processing image {}/{}".format(i + 1,
			len(imagePaths)))
		image = cv2.imread(imagePath)

		# compute the hash for the image and convert it
		h = dhash(image)
		h = convert_hash(h)

		# Debug
		# print('Hash dictionary prior:', hashes)

		# Check the existing hashes dictionary, else add it to hash dictionary
		l = hashes.get(h, [])
		if l:
			handle_duplicate(l, imagePath, duplicate_dir, image, verbose=True)
		else:
			l.append(imagePath)
			hashes[h] = l

		# Debug
		# print('Hash dictionary post:', hashes)

	# build the VP-Tree
	print("[INFO] building VP-Tree...")
	points = list(hashes.keys())
	tree = vptree.VPTree(points, hamming)

	# serialize the VP-Tree to disk
	print("[INFO] serializing VP-Tree...")
	f = open(tree_name, "wb")
	f.write(pickle.dumps(tree))
	f.close()

	# serialize the hashes to dictionary
	print("[INFO] serializing hashes...")
	f = open(hash_name, "wb")
	f.write(pickle.dumps(hashes))
	f.close()