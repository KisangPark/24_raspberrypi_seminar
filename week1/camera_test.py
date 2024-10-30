"""

Raspberry pi seminar

Week1. Camera test

1. make venv & install dependencies

    1) make venv
        python3 -m venv [env_name]
        cd [env_name]
        source [env_name]/bin/activate

    2) install dependencies
        pip3 install [package_name]
        -> opencv-python, numpy, mfrc522-python, RPI.GPIO

    3) make python file
        nano camera_test.py
        ctrl+O & ctrl+x

    4) Git clone
        git clone [https_address]

"""

import cv2

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    cv2.imshow('test', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
