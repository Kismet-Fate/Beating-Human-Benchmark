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
    pic = pyautogui.screenshot(region=(0,150,1900,820))
    width, height = pic.size
    for x in range(0,width,45):
        for y in range(0,height,45):
            r,g,b = pic.getpixel((x,y))
            
            if r == 149 and g == 195 and b == 232:
                if x in range(965, 1145):
                    if y not in range(665-150, 725-150):
                        click(x,y+150)
                        time.sleep(0.01)
                        break
                else:
                    click(x,y+150)
                    time.sleep(0.01)
                    break
        
