import math
import numpy as np
import cv2

from cvzone.HandTrackingModule import HandDetector
from pyfirmata import Arduino, SERVO

from utils.hand_closing_utils import check_closed
from utils.hand_position_calc import calc_x_position, calc_y_position, calc_z_position

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
coff = np.polyfit(x, y, 2)

# Arduino
port = 'COM3'
pin_1 = 10
pin_2 = 11
pin_3 = 9
pin_4 = 8
board = Arduino(port)
board.digital[pin_1].mode = SERVO
board.digital[pin_2].mode = SERVO
board.digital[pin_3].mode = SERVO
board.digital[pin_4].mode = SERVO

distanceCM = 0

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img)

    if hands:
        lmList = hands[0]['lmList']
        x1, y1, _ = lmList[5]
        x2, y2, _ = lmList[17]

        x3, y3, _ = lmList[9]

        distance = int(math.sqrt((y1 - y2) ** 2 + (x1 - x2) ** 2))
        A, B, C = coff
        distanceCM = int(A * distance ** 2 + B * distance + C)

        to_close = check_closed(lmList)

        if to_close:
            board.digital[pin_4].write(0)
        else:
            board.digital[pin_4].write(50)

        board.digital[pin_1].write(calc_z_position(distanceCM))
        board.digital[pin_2].write(calc_y_position(y3))
        board.digital[pin_3].write(calc_x_position(x3))

    cv2.imshow("Image", img)
    cv2.waitKey(1)
