import numpy as np
import cv2

def main():
	img_path = "lena.png"
	img = cv2.imread('lena.png', cv2.IMREAD_COLOR)
	if img is None :
		print("ERROR: Cannot open the image {}".format(img_path))
		return -1
	cv2.imshow("Image 1", img)
	cv2.waitKey()
	cv2.destroyAllWindows()
	return 0

def dummy_func():
	return -1

if __main__=='__main__':
	main()
