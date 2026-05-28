# ----------------------------------------
# Image Processing using OpenCV
# ----------------------------------------

import cv2

img = cv2.imread("image.jpg")

# Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur
blur = cv2.GaussianBlur(img, (5,5), 0)

# Edge Detection
edges = cv2.Canny(img, 100, 200)

# Show images
cv2.imshow("Original", img)
cv2.imshow("Grayscale", gray)
cv2.imshow("Blur", blur)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
