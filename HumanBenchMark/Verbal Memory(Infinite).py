from pyautogui import*
import pyautogui
import time
import win32api,win32con
import keyboard
from pytesseract import pytesseract
import cv2
import numpy as np
import os

print("Press r to start, q to quit.")
keyboard.wait('r')
time.sleep(0.1)
custom_config = r'--oem 3 --psm 6'
f = open("Verbal Memory\Words_Database.txt", "r+")

def click(x,y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    #keyboard.wait('r')
    img = pyautogui.screenshot(region=(650,420,650,120))
    img.convert("RGB")
    d = img.getdata()
     
    new_image = []
    for item in d:
           
        # change all white (also shades of whites) pixels to black
        # change all blue (also shades of blues) pixels to white
        if item[0] in list(range(200, 256)):
            new_image.append((0, 0, 0))
        elif item[2] in list(range(150, 256)):
            new_image.append((255, 255, 255))
        else:
            new_image.append(item)
        
        
    # update image data
    img.putdata(new_image)
    img.save("Verbal Memory/Altered_image.png")
    pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(img, config=custom_config)
    text = text[:-1].split("Statistics About the tqest")[0].replace("\n","").removesuffix(' ').strip()
    #Honestly, don't understand how string splicing works, like I get the
    #one to one java to python kind of substring(2,5) or text[2:5]
    #but like text[-1] is just wack
    time.sleep(0.01)
    f.seek(0)
    words = f.read()
    if text not in words:
        #print(f.read())
        click(1035,590)
        print("Written")
        f.write("\n"+ text + "\n")
    else:
        print("It's there")
        click(865,590)
        
    print(text)
    
    #keyboard.write(text,0.002)
    time.sleep(0.1)
f.truncate(0)
f.close()
