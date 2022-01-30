import cv2
import pickle

rows = []
rowsActive = []
pixels_w = 0
pixels_h = 0
git push -u origin main

try:
    with open('polygons', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []


def print_pattern():
    position = 1  # Posisi sekaranag
    tmp_string = "PATTERN PARKIR\n"
    for pos in rows:
        x1, y1 = pos
        tmp_list = []
        for pos1 in posList:
            x2, y2 = pos1
            if (x1 == x2 and y1 == y2) or (x1 == x2 + pixels_w and y1 == y2):
                tmp_list.append(pos)
        if position != no_w:
            if len(tmp_list) < 1:
                tmp_string += "_"
                # Empty
            else:
                tmp_string += "M"
                # Field
            position += 1
        else:
            tmp_string += "_/\n"
            position = 1
    print(tmp_string)


def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN:
        # posList.append((x, y))
        print("Pointer X : " + str(x) + " Y : " + str(y))
        tmp_list = []  # save tmp result if
        for pos in rows:
            x1, y1 = pos
            if x1 < x < x1 + pixels_w and y1 < y < y1 + pixels_h:
                tmp_list.append(pos)
        posList.append(tmp_list[len(tmp_list) - 1])
        print_pattern()

    if events == cv2.EVENT_RBUTTONDOWN:
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + pixels_w and y1 < y < y1 + pixels_h:
                posList.pop(i)

        print_pattern()

    with open('polygons', 'wb') as f:
        pickle.dump(posList, f)


added = False
while True:
    img = cv2.imread('carParkImg.png')

    no_w = 22  # replace with no. of patches in width
    no_h = 15  # replace with no. of patches in height
    h, w = img.shape[:2]
    pixels_w = round(w / no_w)
    pixels_h = round(h / no_h)
    list_h = []

    # create rows
    for y in range(0, h, pixels_h):
        for x in range(0, w, pixels_w):
            cv2.rectangle(img, (x, y), (x + pixels_w, y + pixels_h), (255, 0, 0), 2)
            if not added:
                rows.append((x, y))
                # print("List X : ", str(x) + " Y : " + str(y))

    added = True
    # Create selection
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0] + pixels_w + pixels_w, pos[1] + pixels_h), (255, 0, 255), 2)

    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)
    cv2.waitKey(1)
