from ultralytics import YOLO
import cv2
import cvzone
import math
import time
import notify

model = YOLO(r"C:\Users\saran\Downloads\fire_spark_smoke.pt")

classNames = ['Fire-Smoke', 'fire', 'smoke', 'spark']

import serial
esp32 = serial.Serial('COM3', 9600)
prev_frame_time = 0
new_frame_time = 0
cap = cv2.VideoCapture(0)

while True:
    new_frame_time = time.time()
    success, img = cap.read()
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1
            conf = math.ceil((box.conf[0] * 100)) / 100
            cls = int(box.cls[0])

            cvzone.cornerRect(img, (x1, y1, w, h))
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
            f=0
            if classNames[cls] == 'fire':
                if not f : notify.send_alert(classNames[cls])
                f=1
                esp32.write(b'f')
            elif classNames[cls] == 'spark' :
                if not f : notify.send_alert(classNames[cls])
                f=1
                esp32.write(b'p')
            elif classNames[cls] == 'smoke' :
                if not f : notify.send_alert(classNames[cls])
                f=1
                esp32.write(b's')
            else:
                f=0
                esp32.write(b'n')
    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    print(fps)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release video capture and close all windows
cap.release()
cv2.destroyAllWindows()
