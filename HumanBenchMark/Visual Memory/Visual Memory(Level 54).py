import os

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
x1 = 650
y1 = 250
x2 = 1250
y2 = 800

#print('Press r for image')
#keyboard.wait("r")

#print('Press r and select the top left of the image')
#keyboard.wait("r")
#x,y = pyautogui.position()

#print('Press r and select the bottom right of the image')
#keyboard.wait("r")
#x2,y2 = pyautogui.position()
#keyboard.wait("r")
#pic = pyautogui.screenshot(region=(x1,y1,x2-x1,y2-y1))
#pic.save(r"C:\Users\yolos\OneDrive\Desktop\Image recongition\HumanBenchMark\image.png")
#os.startfile(r"C:\Users\yolos\OneDrive\Desktop\Image recongition\HumanBenchMark\image.png")
#print("done")
print('Press r each time a new round starts, and q to start clicking.')
while keyboard.is_pressed('.') == False:
    keyboard.wait("r")
    
    pic = pyautogui.screenshot(region=(x1,y1,x2-x1,y2-y1))
    width, height = pic.size
    keyboard.wait("q")
    
    locations = pyautogui.locateAll('Visual Memory\size1.png', pic)
    for pos in locations:
        a,b,c,d = pos
        click(a+c/2+x1,b+d/2+y1)
        print(a,b,c,d)
    locations = pyautogui.locateAll('size2.png', pic)
    for pos in locations:
        a,b,c,d = pos
        click(a+c/2+x1,b+d/2+y1)
        print(a,b,c,d)
    locations = pyautogui.locateAll('size3.png', pic)
    for pos in locations:
        a,b,c,d = pos
        click(a+c/2+x1,b+d/2+y1)
        print(a,b,c,d)
    locations = pyautogui.locateAll('size4.png', pic)
    for pos in locations:
        a,b,c,d = pos
        click(a+c/2+x1,b+d/2+y1)
        print(a,b,c,d)
    locations = pyautogui.locateAll('size5.png', pic)
    for pos in locations:
        a,b,c,d = pos
        click(a+c/2+x1,b+d/2+y1)
        print(a,b,c,d)
    locations = pyautogui.locateAll('size6.png', pic)
    for pos in locations:
        a,b,c,d = pos
        click(a+c/2+x1,b+d/2+y1)
        print(a,b,c,d)
    locations = pyautogui.locateAll('size7.png', pic)
    for pos in locations:
        a,b,c,d = pos
        click(a+c/2+x1,b+d/2+y1)
        print(a,b,c,d)
    locations = pyautogui.locateAll('size8.png', pic)
    for pos in locations:
        a,b,c,d = pos
        click(a+c/2+x1,b+d/2+y1)
        print(a,b,c,d)
    locations = pyautogui.locateAll('size9.png', pic)
    for pos in locations:
        a,b,c,d = pos
        click(a+c/2+x1,b+d/2+y1)
        print(a,b,c,d)
    locations = pyautogui.locateAll('Visual Memory\size10.png', pic)
    for pos in locations:
        a,b,c,d = pos
        click(a+c/2+x1,b+d/2+y1)
        print(a,b,c,d)
    #locations = pyautogui.locateAll('size11.png', pic)
    #for pos in locations:
        #a,b,c,d = pos
        #click(a+c/2+x1,b+d/2+y1)
        #print(a,b,c,d)




    
    #for x in range(0,width,50):
        #for y in range(0,height,50):
            #r,g,b = pic.getpixel((x,y))
            
            #if r == 255 and g == 255 and b == 255:
                #click(x+x1,y+y1)
                #time.sleep(0.01)
                #break
        
