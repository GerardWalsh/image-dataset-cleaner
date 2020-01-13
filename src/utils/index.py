""""
Some of the source cide was written by A Rosebrock: https://www.pyimagesearch.com/2019/08/26/building-an-image-hashing-search-engine-with-vp-trees-and-opencv/
"""

import pickle
import vptree
import cv2

from src.utils.hash import convert_hash, hamming, dhash
from src.utils.duplicates import handle_duplicate

# Written by A Rosebrock. 
def build_tree(imagePaths, tree_name, hash_name, duplicate_dir):

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


def climb_tree(image_paths, tree, hashes):

	if (tree and hashes):
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
						
	else:
		print('Error: VPtree or hash file not found.')