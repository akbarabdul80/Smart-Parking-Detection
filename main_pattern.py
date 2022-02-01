import cv2
import pickle
import cvzone
import numpy as np

cap = cv2.VideoCapture("carPark.mp4")

rows = []
rows_empty = []
pixels_w = 0
pixels_h = 0

with open('polygons', 'rb') as f:
    posList = pickle.load(f)


def empty(a):
    pass


cv2.namedWindow("Vals")
cv2.resizeWindow("Vals", 640, 240)
cv2.createTrackbar("Val1", "Vals", 25, 50, empty)
cv2.createTrackbar("Val2", "Vals", 16, 50, empty)
cv2.createTrackbar("Val3", "Vals", 5, 50, empty)

pattern_string = "PATTERN PARKIR\n"


def print_pattern(pattern_string):
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
                if tmp_list[0] in rows_empty or (tmp_list[0][0] - pixels_w, tmp_list[0][1]) in rows_empty:
                    tmp_string += "F"
                else:
                    tmp_string += "P"
                # Field
            position += 1
        else:
            tmp_string += "_/\n"
            position = 1

        if pattern_string != tmp_string:
            print(pattern_string)
    return pattern_string


def checkSpaces():
    spaces = 0
    rows_empty.clear()
    for pos in posList:
        x, y = pos
        w, h = pixels_w, pixels_h
        w *= 2

        imgCrop = imgThres[y:y + h, x:x + w]
        count = cv2.countNonZero(imgCrop)

        if count < 900:
            color = (0, 200, 0)
            thic = 2
            spaces += 1
            rows_empty.append(pos)
        else:
            color = (0, 0, 200)
            thic = 2
            try:
                rows_empty.remove(pos)
            except:
                a = 1

        cv2.rectangle(img, (x, y), (x + w, y + h), color, thic)

        cv2.putText(img, str(cv2.countNonZero(imgCrop)), (x, y + h - 6), cv2.FONT_HERSHEY_PLAIN, 1,
                    color, 2)

    cvzone.putTextRect(img, f'Free: {spaces}/{len(posList)}', (50, 60), thickness=3, offset=20,
                       colorR=(0, 200, 0))


added = False
while True:
    # Get image frame
    success, img = cap.read()
    cap.set(cv2.CAP_PROP_FPS, 1)
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    no_w = 22  # replace with no. of patches in width
    no_h = 15  # replace with no. of patches in height
    h, w = img.shape[:2]
    pixels_w = round(w / no_w)
    pixels_h = round(h / no_h)

    # create rows
    for y in range(0, h, pixels_h):
        for x in range(0, w, pixels_w):
            if not added:
                rows.append((x, y))
    added = True
    # img = cv2.imread('img.png')
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (3, 3), 1)
    # ret, imgThres = cv2.threshold(imgBlur, 150, 255, cv2.THRESH_BINARY)

    val1 = cv2.getTrackbarPos("Val1", "Vals")
    val2 = cv2.getTrackbarPos("Val2", "Vals")
    val3 = cv2.getTrackbarPos("Val3", "Vals")
    if val1 % 2 == 0: val1 += 1
    if val3 % 2 == 0: val3 += 1
    imgThres = cv2.adaptiveThreshold(imgBlur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                     cv2.THRESH_BINARY_INV, val1, val2)
    imgThres = cv2.medianBlur(imgThres, val3)
    kernel = np.ones((3, 3), np.uint8)
    imgThres = cv2.dilate(imgThres, kernel, iterations=1)

    checkSpaces()
    # pattern_string = print_pattern(pattern_string)
    # print(pattern_string)

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
                if tmp_list[0] in rows_empty or (tmp_list[0][0] - pixels_w, tmp_list[0][1]) in rows_empty:
                    tmp_string += "F"
                else:
                    tmp_string += "P"
                # Field
            position += 1
        else:
            tmp_string += "_/\n"
            position = 1

    if pattern_string != tmp_string:
        pattern_string = tmp_string
        print("Pattern :" + pattern_string)

    # Display Output
    cv2.imshow("Image", img)
    # cv2.imshow("ImageGray", imgThres)
    # cv2.imshow("ImageBlur", imgBlur)
    key = cv2.waitKey(1)
    if key == ord('r'):
        pass

    # Press Esc key to exit
    if cv2.waitKey(1) == 27:
        break
