from pyautogui import*
import pyautogui
import time
import win32api,win32con
import keyboard
from pytesseract import pytesseract

print("Press enter to start.")
keyboard.wait('enter')
time.sleep(0.1)

custom_config = r'--oem 3 --psm 6'

img = pyautogui.screenshot(region=(340,460,1550,650))
pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(img, config=custom_config)
text = text[:-1].split("Statistics About the test")[0].replace("\n"," ").removesuffix(' ')
print(text)
#Honestly, don't understand how string splicing works, like I get the
#one to one java to python kind of substring(2,5) or text[2:5]
#but like text[-1] is just wack
keyboard.write(text,0.002)
