import cv2

img = cv2.imread('carParkImg.png')
no_w = 20  # replace with no. of patches in width
no_h = 15  # replace with no. of patches in height
h, w = img.shape[:2]
pixels_w = round(w / no_w)
pixels_h = round(h / no_h)

for i in range(0, h, pixels_h):
    cv2.line(img, (0, i), (w, i), (0, 255, 0), 1)
for i in range(0, w, pixels_w):
    cv2.line(img, (i, 0), (i, h), (0, 255, 0), 1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
