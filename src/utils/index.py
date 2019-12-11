# import the necessary packages
from src.utils.hash import convert_hash, hamming, dhash
import pickle
import vptree
import cv2

def index_images(imagePaths, tree_name, hash_name):

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

		# update the hashes dictionary
		l = hashes.get(h, [])
		l.append(imagePath)
		hashes[h] = l

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