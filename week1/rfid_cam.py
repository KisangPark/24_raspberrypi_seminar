#python

# Write your code here :-)
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import cv2

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

reader = SimpleMFRC522()

cap = cv2.VideoCapture(0)

try:
        id = 0
        id, text = reader.read() #stall here

except:
        print("error occurred at rfid")


if id!=0:
        print(id)
        while cap.isOpened():
                ret, frame = cap.read()
                cv2.imshow('test', frame)

                if cv2.waitKey(10) & 0xFF == ord('q'):
                        break


GPIO.cleanup()
cap.release()
cv2.destroyAllWindows()