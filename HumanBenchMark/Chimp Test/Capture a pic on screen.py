from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import os 

print('Press r and select the top left of the image')
keyboard.wait("r")
x,y = pyautogui.position()

print('Press r and select the bottom right of the image')
keyboard.wait("r")
x2,y2 = pyautogui.position()
imgNum = 40
link = (f'img{imgNum}.png')
img = pyautogui.screenshot(region=(x,y,x2-x,y2-y))
img.save(link)
os.system(link)
