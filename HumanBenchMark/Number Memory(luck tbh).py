from pyautogui import*
import pyautogui
import time
import win32api,win32con
import keyboard
from PIL import Image
from pytesseract import pytesseract
from pynput.keyboard import Key
import cv2
import numpy as np

custom_config = r'--oem 3 --psm 6'
print("Press R to screenshot, and enter to type the number")
running = True
while running:
    keyboard.wait('r')
    img = pyautogui.screenshot(region=(600,340,1200,450))
    #img = r"numbers.png"
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
    img.save("Number Memory/Altered_image.png")
    image = cv2.imread('Number Memory/Altered_image.png', flags=cv2.IMREAD_COLOR)
    kernel = np.array([[0, -1, 0],
                       [-1, 5,-1],
                       [0, -1, 0]])
    image2 = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
    image2 = cv2.blur(image2,(5,5))
    #image = cv2.imread('numbers.png')
    #img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    #ret, thresh1 = cv2.threshold(img, 20, 0, cv2.THRESH_BINARY)
    #cv2.imshow('Adaptive Mean', thresh1)
    #image2 = r'Number Memory/Altered_image.png'
    pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(image2, config="--oem 3 --psm 6 digits")
    text = text.replace("\n","")
    text = text + "\n"
    #text = text[:-1].split("Statistics About the test")[0].replace("\n"," ").removesuffix(' ')
    #Honestly, don't understand how string splicing works, like I get the
    #one to one java to python kind of substring(2,5) or text[2:5]
    #but like text[-1] is just wack
    keyboard.wait('enter')
    keyboard.write(text,0.002)
    
