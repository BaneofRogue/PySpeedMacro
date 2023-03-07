import PySpeedMacro as psm
import pyautogui as p
import time
import random

@psm.timer
def psm1():
    try:
        x, y, w, h = psm.LocateOnScreen("image.png", grayscale=True, region = (2800, 1050, 1000, 1000), confidence = 0.8)

        new_x = x+w//2
        new_y = y+h//2

        psm.moveMouse(new_x, new_y, speed = 0.1)
    except TypeError:
        pass
    

@psm.timer
def psm2():
    try:
        x, y = psm.LocateCenter("image.png", grayscale=True, region = (2800, 1050, 1000, 1000), confidence = 0.8)
        psm.moveMouse(x, y, speed = 0.1)
    except TypeError:
        pass

    
@psm.timer
def psm3():
    try:
        psm.LocateAndMove("image.png", grayscale=True, speed=0.1, region = (2800, 1050, 1000, 1000), direct=False, confidence = 0.8)
    except TypeError:
        pass


@psm.timer
def pyauto():
    try:
        x, y, w, h = p.locateOnScreen("image.png", grayscale = True, region = (2800, 1050, 1000, 1000), confidence = 0.8)
        
        new_x = x+w//2
        new_y = y+h//2

        p.moveTo(new_x, new_y, 0.1)
    except TypeError:
        pass
    except AttributeError:
        pass
    
@psm.timer
def pyauto2():
    try:
        location = p.locateCenterOnScreen("image.png", grayscale = True, region = (2800, 1050, 1000, 1000), confidence = 0.8)
        p.moveTo(location.x, location.y, 0.1)
        
    except TypeError:
        pass

    except AttributeError:
        pass




    
repeat = 2

for i in range(repeat):

    psm.returnMouse(function = psm1, direct = True)


time.sleep(1)
for i in range(repeat):

    psm.returnMouse(function = psm2, direct = True)

time.sleep(1)
for i in range(repeat):

    psm.returnMouse(function = psm3, direct = True)


time.sleep(1)
for i in range(repeat):

    psm.returnMouse(function = pyauto, direct = True)

time.sleep(1)
for i in range(repeat):

    psm.returnMouse(function = pyauto2, direct = True)
