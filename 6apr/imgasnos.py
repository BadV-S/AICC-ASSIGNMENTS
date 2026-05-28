# ----------------------------------------
# Image as Numbers
# ----------------------------------------

import cv2

# Load image
img = cv2.imread("image.jpg")

# Print details
print("Image Shape:", img.shape)
print("Pixel Value at (0,0):", img[0,0])
print("Channels:", img.shape[2])
