import datetime
import subprocess
from PIL import ImageGrab
import numpy as np
import cv2
# from win32api import GetSystemMetrics

# width = GetSystemMetrics(0)
# height = GetSystemMetrics(1)
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
print(timestamp)
name = timestamp+".mp4"
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(name, fourcc, 20.0, (1920, 1080))

webcam = cv2.VideoCapture(1)
print("Started Capturing")
while True:
    img = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    cv2.imshow('Secret Capture', img_final)
    captured_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break
print("Stopped Capturing")