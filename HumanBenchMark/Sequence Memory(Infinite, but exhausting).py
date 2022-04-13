from pyautogui import*
import pyautogui
import time
import keyboard as keyboard
import random
import win32api,win32con
from collections import deque
from pynput.keyboard import Listener, KeyCode
from pynput.keyboard import Key, Controller

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
print("Press numbers on the numpad to enter the position into the queue, press enter to click, backspace to delete.")

def click(x,y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def click_them():
    q2 = q.copy()
    while bool(q2) == True:
        num = q2.popleft()
        if num == 7:
            click(785,370)
        if num == 8:
            click(950,370)
        if num == 9:
            click(1115,370)
        if num == 4:
            click(785,535)
        if num == 5:
            click(950,535)
        if num == 6:
            click(1115,535)
        if num == 1:
            click(785,695)
        if num == 2:
            click(950,695)
        if num == 3:
            click(1115,695)
        time.sleep(0.01)

def on_press(key):
    if key == start_stop_key:
        print("input detected")
    elif hasattr(key, 'vk') and 97 <= key.vk <= 105:
        q.append(key.vk-96)
    elif key == Key.backspace:
        try:
            q.pop()
        except IndexError:
            print("Queue is empty")
        
    elif key == click_key:
        click_them()
    elif key == exit_key:
        running = False
        listener.stop()
    else:
        time.sleep(0.000001)

    
with Listener(on_press=on_press) as listener:
   listener.join()
   



i = 0

q.append(i)
