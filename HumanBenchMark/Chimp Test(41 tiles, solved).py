from pyautogui import*
import pyautogui
import time
import keyboard as keyboard
import random
import win32api,win32con
from collections import deque
from pynput.keyboard import Listener, KeyCode
from pynput.keyboard import Key, Controller
import cv2

q = deque()
#q commands
#q.count(3), number of occuring parameter in queue
#q.index(4), the first occuring position of parameter
#q.index(4,2,5), the first occuring 4 in position 2 to 5
#q.reverse() reverse the order
#q.rotate() rotates the queue a certain number of times
start_stop_key = KeyCode(char='r')
exit_key = KeyCode(char='.')
click_key = Key.enter
numbered_keys = [KeyCode(char='1')]
running = True
print("Press enter to press them.")
#950, 665
def click(x,y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def click_them():
    while len(q) != 0:
        q.pop()
    
    for x in range(1,41):
        print(x)
        if pyautogui.locateOnScreen(f'Chimp Test\img{x}.png', confidence = 0.99) != None:
            location = pyautogui.center(pyautogui.locateOnScreen(f'Chimp Test\img{x}.png', confidence = 0.99))
            q.append(location)
            print(location)
            time.sleep(0.001)
        else:
            break
            
    while len(q) != 0:
        x,y = q.popleft()
        print(x,y)
        click(x,y)
        time.sleep(0.1)
    click(960,665)
    win32api.SetCursorPos([1750, 925])
def on_press(key):
    if key == start_stop_key:
        print("input detected") 
    elif key == click_key:
        click_them()
    elif key == exit_key:
        running = False
        listener.stop()
    else:
        time.sleep(0.000001)

    
with Listener(on_press=on_press) as listener:
   listener.join()
   
