from ultralytics import YOLO
import cv2
import cvzone
import math
import time
import notify
import threading
import wifisend

f = 0
last=''
model = YOLO(r"C:\Users\saran\Downloads\fire_spark_smoke.pt")

classNames = ['Fire-Smoke', 'fire', 'smoke', 'spark']

import serial as serial



esp32 = serial.Serial('COM3', 115200)
prev_frame_time = 0
new_frame_time = 0
cap = cv2.VideoCapture(0)

data='0'
def read_from_serial():
    global data
    while True:
        data = esp32.readline().decode().strip()
        if data=='1':
            print("Received from ESP32:", data)

thread = threading.Thread(target=read_from_serial)
thread.daemon = True
thread.start()

while True:
    new_frame_time = time.time()
    success, img = cap.read()
    results = model(img, stream=True)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls = int(box.cls[0])
            conf = math.ceil((box.conf[0] * 100)) / 100

            if classNames[cls]=='smoke' and conf<0.7: continue
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2 - x1, y2 - y1

            cvzone.cornerRect(img, (x1, y1, w, h))
            cvzone.putTextRect(img, f'{classNames[cls]} {conf}', (max(0, x1), max(35, y1)), scale=1, thickness=1)
            if classNames[cls] == 'fire':
                esp32.write(b'f')
            elif classNames[cls] == 'spark':
                esp32.write(b'p')
            elif classNames[cls] == 'smoke':
                esp32.write(b's')
            else:
                esp32.write(b'n')
            if data=='1':
                last=classNames[cls]
                f=1
                break

    fps = 1 / (new_frame_time - prev_frame_time)
    prev_frame_time = new_frame_time
    print(fps)

    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q') or f:
        break

cap.release()
cv2.destroyAllWindows()
notify.send_alert(last)