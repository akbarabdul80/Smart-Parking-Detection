import cv2
import pickle

width, height = 107, 48

try:
    with open('polygons', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []


def mouse_click(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        posList.append((x, y))
    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('polygons', 'wb') as f:
        pickle.dump(posList, f)


while True:
    img = cv2.imread('carParkImg.png')

    no_w = 20  # replace with no. of patches in width
    no_h = 15  # replace with no. of patches in height
    h, w = img.shape[:2]
    pixels_w = round(w / no_w)
    pixels_h = round(h / no_h)
    # (Margin Start, Lebar) , (Panjang, Margin Top)
    # cv2.rectangle(img, (0, 2), (w, 2), (255, 0, 255), 2)

    # for pos in posList:
    #     cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), (255, 0, 255), 1)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouse_click)
    cv2.waitKey(1)