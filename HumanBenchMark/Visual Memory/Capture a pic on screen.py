from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

print('Press r and select the top left of the image')
keyboard.wait("r")
x,y = pyautogui.position()

print('Press r and select the bottom right of the image')
keyboard.wait("r")
x2,y2 = pyautogui.position()

img = pyautogui.screenshot(region=(x,y,x2-x,y2-y))
img.save(r"C:\Users\yolos\OneDrive\Desktop\Image recongition\HumanBenchMark\Visual Memory\size11.png")
