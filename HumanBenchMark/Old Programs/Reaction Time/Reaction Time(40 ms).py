from pyautogui import*
import pyautogui
import time
import keyboard
import random
import win32api,win32con
from PIL import ImageGrab
import datetime

print("Press r to start, and q to stop")
keyboard.wait('r')
time.sleep(0.1)
def click(x,y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

    #Color of the target(r,g,b),such as if b == 180:
    #you can also use a range of color, such as if(b in range(180,210)):
    #click has to have x,y such as if b == 180: click(x+660, y+350


while keyboard.is_pressed('q') == False:
#for i in range(1000):
    datetime1 = datetime.datetime.now()
    #start = time.process_time()
    #pic = pyautogui.screenshot(region=(0,150,1300,440))
    #r,g,b = pic.getpixel((150,150))
    #time.sleep(1)
    #if g == 219:
    #    click(1300,440)
    #    time.sleep(0.05)
    #    click(1300,400)
    pic = ImageGrab.grab(bbox= (150,150,151,151))
    r,g,b = pic.getpixel((0, 0))
    if g == 219:
        click(1300,440)
        time.sleep(0.05)
        click(1300,400)
    #end = time.process_time()
    datetime2 = datetime.datetime.now()
    #print(end - start)
    print(datetime2 - datetime1)


