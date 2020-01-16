import cv2
import os

def handle_duplicate(original_image_path, duplicate_image_path, duplicate_dir, image, verbose=False):
	""" Moves duplicate image from the dataset that is being indexed (w/ VPtree)
		to directory for duplicates
	
	Arguments:
		original_image_path {[str]} -- [Path to original image]
		duplicate_image_path {[str]} -- [Path of duplicate image]
		duplicate_dir {[str]} -- [Path to directory for containing duplicates]
		image {[cv.Mat]} -- [duplicate image]
	
	Keyword Arguments:
		verbose {bool} -- [Flag to set the print status of the image paths] (default: {False})
	"""

	if verbose:
		print('Path of original image in tree:', original_image_path[0])
		print('Path of duplicate image trying to be added to tree:', duplicate_image_path)

	if not os.path.exists(duplicate_dir):
		os.mkdir(duplicate_dir)

	# Move duplicate image to duplicate dir
	original_image_path = original_image_path[0].split('/')
	original_image_name = original_image_path[-1].split('.')[0]
	print('Original path name:', original_image_path)
	print('Original image name:', original_image_name)
	# path = duplicate_dir + duplicate_image_path.split('/')[-1].split('.')[0] + '_' + original_image_path[0:2].split('/')[-1]
	# cv2.imwrite(path, image)
	# os.remove(duplicate_image_path)
