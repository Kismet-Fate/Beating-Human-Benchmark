from pyautogui import*
import pyautogui
import time
import keyboard
import random
import win32api,win32con

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
    pic = pyautogui.screenshot(region=(1300,440,1300,440))
    width, height = pic.size
    r,g,b = pic.getpixel((0,0))
    if r == 75 and g == 219 and b == 106:
        click(1300,440)
        time.sleep(0.05)
        click(1300,400)
        
