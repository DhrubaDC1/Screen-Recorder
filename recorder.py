import datetime
import subprocess
from PIL import ImageGrab
import numpy as np
import cv2

# from win32api import GetSystemMetrics

# width = GetSystemMetrics(0)
# height = GetSystemMetrics(1)
select = int(input(
    "What's your display resolution?\n   1. 1280*720\n   2. 1366*768\n   3. 1920*1080\n   4. 2560*1600\n   5.custom\n"))
if select == 1:
    width = 1280
    height = 720
elif select == 2:
    width = 1366
    height = 768
elif select == 3:
    width = 1920
    height = 1080
elif select == 4:
    width = 2560
    height = 1600
else:
    width = int(input("Width: "))
    height = int(input("Height: "))
fps_s = int(input("What fps do you want to record?\n  1. 30 fps\n  2. 60 fps\n"))
if fps_s == 1:
    fps = 30.0
else:
    fps = 60.0
timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
print(timestamp)
name = timestamp + ".mp4"
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
captured_video = cv2.VideoWriter(name, fourcc, fps, (width, height))

# webcam = cv2.VideoCapture(1)
print("Started Capturing")
print("Close the window to stop Capturing")
while True:
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    # cv2.imshow('Secret Capture', img_final)
    captured_video.write(img_final)
    # print("Capturing...")
    # if input() == "end":
    #     break
