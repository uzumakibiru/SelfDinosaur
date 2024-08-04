#import packages

import pyautogui
from PIL import ImageGrab, ImageOps,Image
import numpy as np
import time

#Start dinasaur game
# URL="https://elgoog.im/t-rex/"
bg_box=(200,250,250,300)
box=(250,390,350,500)               
URL="chrome://dino/"
pyautogui.press('win')
time.sleep(3)        
pyautogui.typewrite("Chrome")                 
pyautogui.press("enter")
time.sleep(5)
for _ in range(3):
    pyautogui.hotkey("win","up")
pyautogui.typewrite(URL)
pyautogui.press("enter")
time.sleep(3) 
pyautogui.press("space")
pyautogui.moveTo(400,300)
time.sleep(3)
pyautogui.moveTo(600,600)

#Get the box
# time.sleep(5)
# x1,y1=pyautogui.position()
# print(x1,y1)
# time.sleep(5)
# x2,y2=pyautogui.position()
# print(x2,y2)

def process_obstcel():
    # time.sleep(7) 
    image=ImageGrab.grab(bbox=box)
    # image=Image.open("tree.png")
    gray_image=ImageOps.grayscale(image)
    # gray_image.show()                    
    arr=np.array(gray_image)
    print(np.sum(arr))
    return np.sum(arr)
def process_bg():
    # time.sleep(7) 
    image=ImageGrab.grab(bbox=bg_box)
    # image=Image.open("tree.png")
    gray_image=ImageOps.grayscale(image)
    # gray_image.show()                    
    arr=np.array(gray_image)
    print(f"bg{np.sum(arr)}")      
    return np.sum(arr)

while True:
    if process_bg() >630000    :    
        if process_obstcel() < 2750000:      
            pyautogui.press("space")
    elif process_bg() <300000       :
        if process_obstcel() > 54180:            
            pyautogui.press("space")
# process_obstcel()   