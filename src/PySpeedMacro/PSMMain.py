import cv2
import numpy as np
import os
import win32api, win32con
import time
from PIL import ImageGrab
import math
import ctypes
import logging
from PySpeedMacro.PSMMouse import WinMouse

wm = WinMouse()

speedZeroException = "Value must not be 0. If you are trying to move the mouse instantly, use direct = True"
imageNotFoundException = "Image not found on screen or region."

"""
Just for accurate mouse positioning and movement.
"""


ctypes.windll.user32.SetProcessDPIAware()


class PySpeedMacroException(Exception):
    pass


def accurate_delay(delay):

    """

    A seemingly more accurate time.sleep system.

    """

    _ = time.perf_counter() + delay
    while time.perf_counter() < _:
        pass


def timer(func):

    """

    Description: The 'timer' decorator can be used to returning how long it took for a function to run.

    Usage: @timer

    Note: Not sure if can be used in other scripts.

    """

    def wrapper(*args, **kwargs):

        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Elapsed time for {func.__name__}: {end_time - start_time:.5f} seconds")
        return result

    return wrapper


def Screenshot(region=None):

    """

    Description: Quick and easy Screenshot method. 

    Usage: PySpeedMacro.sceenshot(region = (100, 200, 300, 400))

    # This creates a Screenshot from the pixels x = 100, y = 200, with a size of 300 by 400.
    
    Note: If no region is entered, it will Screenshot the whole screen.

    TODO:
    
     - Allow user to save Screenshot as image.
     - Save Screenshot as image type
     - Save Screenshot as title

    """

    if region is not None:
        left, top, size_x, size_y = region
        right = left + size_x
        bottom = top + size_y
        screen = ImageGrab.grab(bbox=(left, top, right, bottom))
        #print(f"start at {left}, {top}. ends at: {right}, {bottom}")
    else:
        screen = ImageGrab.grab()

    return np.array(screen)


def lerp(a, b, t):

    """

    I forgot

    """

    return a + (b - a) * t


"""

███╗░░░███╗░█████╗░██╗░░░██╗░██████╗███████╗  ░█████╗░░█████╗░███╗░░██╗████████╗██████╗░░█████╗░██╗░░░░░
████╗░████║██╔══██╗██║░░░██║██╔════╝██╔════╝  ██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░
██╔████╔██║██║░░██║██║░░░██║╚█████╗░█████╗░░  ██║░░╚═╝██║░░██║██╔██╗██║░░░██║░░░██████╔╝██║░░██║██║░░░░░
██║╚██╔╝██║██║░░██║██║░░░██║░╚═══██╗██╔══╝░░  ██║░░██╗██║░░██║██║╚████║░░░██║░░░██╔══██╗██║░░██║██║░░░░░
██║░╚═╝░██║╚█████╔╝╚██████╔╝██████╔╝███████╗  ╚█████╔╝╚█████╔╝██║░╚███║░░░██║░░░██║░░██║╚█████╔╝███████╗
╚═╝░░░░░╚═╝░╚════╝░░╚═════╝░╚═════╝░╚══════╝  ░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚══════╝

"""


def getMousePosition():

    """

    Description: Simple function that returns mouse position, using win32api.

    Usage: PySpeedMacro.getMousePosition()
    
    Alternate Usage: x, y = PySpeedMacro.getMousePosition()

    Note: 

    """

    x, y = win32api.GetCursorPos()

    return x, y

def click(button = "left", separation = 0.1):

    wm.click(button, separation)

"""
def move_in_square(x, y, w, h, speed):

    top_left = (int(x - w/2), int(y - h/2))
    top_right = (int(x + w/2), int(y - h/2))
    bottom_left = (int(x - w/2), int(y + h/2))
    bottom_right = (int(x + w/2), int(y + h/2))
    distance = w + h

    start_time = time.time()
    while time.time() - start_time < speed:
        for t in range(0, 101, 1):
            p1 = (lerp(top_left[0], top_right[0], t/100), lerp(top_left[1], top_right[1], t/100))
            p2 = (lerp(top_right[0], bottom_right[0], t/100), lerp(top_right[1], bottom_right[1], t/100))
            p3 = (lerp(bottom_right[0], bottom_left[0], t/100), lerp(bottom_right[1], bottom_left[1], t/100))
            p4 = (lerp(bottom_left[0], top_left[0], t/100), lerp(bottom_left[1], top_left[1], t/100))
            win32api.SetCursorPos((int(p1[0]), int(p1[1])))
            accurate_delay(speed/4)
            win32api.SetCursorPos((int(p2[0]), int(p2[1])))
            accurate_delay(speed/4)
            win32api.SetCursorPos((int(p3[0]), int(p3[1])))
            accurate_delay(speed/4)
            win32api.SetCursorPos((int(p4[0]), int(p4[1])))
            accurate_delay(speed/4)
"""


def multiClick(button = "left", count = 2, separation = 0.1):

    """

    Description: Click multiple times.

    Parameters: 

     - button | Type of button to click: "left", "right", or "middle"
     - count | How many clicks to simulate
     - separation | How long each click will take before starting a new click.

    Usage: PySpeedMacro.multiClick(count = 15, separation = 0.05)

    Note: Delay may be a little inaccurate with different operating systems.

    TODO: 

    """

    for i in range(count):

        wm.click(button, separation)
        #print("ok")


def spinMouse(center_x = None, center_y = None, radius = 100, speed = 1, count = 1):

    """

    Description: Move the mouse in a circular motion.

    Parameters: 

     - center_x, center_y | Center coordinates of the circle that the mouse will go around.
     - radius | Circle radius in pixels.
     - speed | Time in seconds to complete motion.
     - count | Amount of times mouse will spin in a circle.

    Usage: PySpeedMacro.spinMouse(100, 100, radius = 250, speed = 0.1, count = 2)

    Note: 

    TODO: 

    """

    if center_x or center_y or radius <= 0:
        print("center_x, center_y, or radius is 0. You may run into errors!")

    #try:

    if center_x or center_y == None:
        center_x, center_y = getMousePosition()

    if count < 1:
        raise ValueError("Count must be greater than or equal to 1")

    for i in range(count):
        start_time = time.time()
        angle = 0
        while time.time() - start_time < speed:
            angle = (time.time() - start_time) * 2 * math.pi / speed
            x = round(center_x + math.cos(angle) * radius)
            y = round(center_y + math.sin(angle) * radius)
            moveMouse(x, y, direct = True)

    #except:
    #    print("Could not complete operation.")


def moveMouse(x, y, direct = False, speed=0.1):
    
    """

    Description: Run a given function, then return mouse to starting position. 

    Parameters: 

     - x, y | x and y coordinates to move the mouse to.
     - direct | boolean expression for whether mouse should blink back to original spot, or glide smoothly.
     - speed | total time it should take for mouse to glide to original starting point in seconds.

    Usage: PySpeedMacro.moveMouse(100, 100, direct = False, speed = 1)

    Note: 

    TODO: Allow mouse to move freely while mouse is moving??

    """

    if speed == 0:

        raise PySpeedMacroException(speedZeroException)

    if direct:
        print(x)
        print(y)
        win32api.SetCursorPos((x, y))
    else:

        startx, starty = getMousePosition()
        distance = (x - startx, y - starty)
        steps = int(speed * 100)
        step_x = distance[0] / steps
        step_y = distance[1] / steps

        #print(f"step_x, step_y: {step_x}, {step_y}")
        #print(f"Distance: {distance}")

        for i in range(steps):
            new_x = int(startx + step_x * i)
            new_y = int(starty + step_y * i)
            win32api.SetCursorPos((new_x, new_y))
            accurate_delay(speed / steps)

        win32api.SetCursorPos((x, y))


def returnMouse(function=None, direct = False, speed = 0.1):

    """

    Description: Run a given function, then return mouse to starting position. 

    Parameters: 

     - function | run given function.
     - direct | boolean expression for whether mouse should blink back to original spot, or glide smoothly.
     - speed | total time it should take for mouse to glide to original starting point in seconds.

    Usage: PySpeedMacro.returnMouse(function=test, direct = False, speed = 0.1)

    Note: 

    TODO: 

    """

    if function is not None:

        startx, starty = getMousePosition()
        function()
        moveMouse(startx, starty, direct, speed)

    else:

        print("WARNING: No given function to run!")


"""

██╗███╗░░░███╗░█████╗░░██████╗░███████╗░██████╗███████╗░█████╗░██████╗░░█████╗░██╗░░██╗
██║████╗░████║██╔══██╗██╔════╝░██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██║░░██║
██║██╔████╔██║███████║██║░░██╗░█████╗░░╚█████╗░█████╗░░███████║██████╔╝██║░░╚═╝███████║
██║██║╚██╔╝██║██╔══██║██║░░╚██╗██╔══╝░░░╚═══██╗██╔══╝░░██╔══██║██╔══██╗██║░░██╗██╔══██║
██║██║░╚═╝░██║██║░░██║╚██████╔╝███████╗██████╔╝███████╗██║░░██║██║░░██║╚█████╔╝██║░░██║
╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝

"""

# PySpeedMacro is designed to 
#
#
#
#

def LocateOnScreen(path, confidence=1, directory='.', region=None, grayscale=False):

    """

    Description: Locates an image and returns the location variables for the first found image.

    Parameters: 

     - path | Image name in string form.
     - confidence | 0.0 to 1.0 scale of accuracy in matching the image. Example: 0.5 means 50% accuracy. 0.95 means 95% accuracy.
     - directory | If left empty, it will use the current directory to access the image file.
     - region | If no region is entered, it will Screenshot the whole screen.
     - grayscale | Boolean expression for converting the image to gray or not. Increase in performance if True! May lower accuracy! 

    Usage: PySpeedMacro.LocateOnScreen("image.png", confidence = 0.7, region = (100, 100, 200, 200), grayscale = True)

    Explanation: The function searches for "image.png", in a 200 by 200 region starting at 100, 100. The image matching threshold is 70% accuracy and the image is set to grayscale.

    TODO: 

    """
    try:


        fullPath = os.path.join(directory, path)
        screen = Screenshot(region)
        image = cv2.imread(fullPath)

        if grayscale:

            """
            If grayscale is True, then convert image to grayscale.
            """

            screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        else:

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        result = cv2.matchTemplate(screen, image, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= confidence:

            x, y = max_loc[0], max_loc[1]
            w, h = image.shape[1], image.shape[0]

            if region is not None:

                x += region[0]
                y += region[1]

            return (x, y, w, h)

        else:

            return None


    except cv2.error as e:

        print(e)
        return None


def LocateCenter(path, confidence=1, directory='.', region=None, grayscale=False):

    """

    Description: Locates an image and returns the center coordinates for the first found image.

    Parameters: 

     - path | Image name in string form.
     - confidence | 0.0 to 1.0 scale of accuracy in matching the image. Example: 0.5 means 50% accuracy. 0.95 means 95% accuracy.
     - directory | If left empty, it will use the current directory to access the image file.
     - region | If no region is entered, it will Screenshot the whole screen.
     - grayscale | Boolean expression for converting the image to gray or not. Increase in performance if True! May lower accuracy! 

    Usage: PySpeedMacro.LocateCenter("image.png", confidence = 0.7, region = (100, 100, 200, 200), grayscale = True)

    Explanation: The function searches for "image.png", in a 200 by 200 region starting at 100, 100. The image matching threshold is 70% accuracy and the image is set to grayscale.

    TODO: 

    """

    try:


        fullPath = os.path.join(directory, path)
        screen = Screenshot(region)
        image = cv2.imread(fullPath)

        if grayscale:

            screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        else:

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        result = cv2.matchTemplate(screen, image, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= confidence:

            x, y = max_loc[0], max_loc[1]
            w, h = image.shape[1], image.shape[0]

            if region is not None:

                x += region[0]
                y += region[1]

            return (x+w//2, y+h//2)

        else:

            return None


    except cv2.error as e:

        print(e)
        return None


def LocateAndMove(path, confidence=1, directory='.', region=None, grayscale=False, direct=True, speed=1):

    """
    Description: By far the most handy Image Search function! Locates an image and moves the mouse to the center of the first found image.

    Parameters:
     - path | Image name in string form.
     - confidence | 0.0 to 1.0 scale of accuracy in matching the image. Example: 0.5 means 50% accuracy. 0.95 means 95% accuracy.
     - directory | If left empty, it will use the current directory to access the image file.
     - region | If no region is entered, it will Screenshot the whole screen.
     - grayscale | Boolean expression for converting the image to gray or not. Increase in performance if True! May lower accuracy!
     - direct | boolean expression for whether mouse should blink back to original spot, or glide smoothly.
     - speed | total time it should take for mouse to glide to original starting point in seconds.

    Usage: PySpeedMacro.LocateAndMove("image.png", confidence = 0.7, region = (100, 100, 200, 200), grayscale = True, direct = False, speed = 0.2)

    Explanation: The function searches for "image.png", in a 200 by 200 region starting at 100, 100. The image matching threshold is 70% accuracy and the image is set to grayscale. Once the image is located the mouse will glide to that location in 0.2 seconds.

    """

    try:

        fullPath = os.path.join(directory, path)

        if region is not None and region[2] <= 0:

            raise ValueError("Width of the screenshot region must be a positive number.")

        if region is not None and region[3] <= 0:

            raise ValueError("Height of the screenshot region must be a positive number.")

        screen = Screenshot(region)
        image = cv2.imread(fullPath)

        if grayscale:

            screen = cv2.cvtColor(screen, cv2.COLOR_RGB2GRAY)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

        else:

            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        result = cv2.matchTemplate(screen, image, cv2.TM_CCOEFF_NORMED)

        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= confidence:

            x, y = max_loc[0], max_loc[1]
            w, h = image.shape[1], image.shape[0]

            if region is not None:

                x += region[0]
                y += region[1]

            moveMouse(x + w // 2, y + h // 2, direct, speed)

            return (x, y, w, h)

        else:

            print("Image not found")
            return None

    except cv2.error as e:

        print(e)
        return None

    except ValueError as e:

        print(e)
        return None

def getPixel(x, y):
    # Get a screenshot of the screen
    im = ImageGrab.grab()

    # Get the RGB values of the pixel at (x, y)
    r, g, b = im.getpixel((x, y))

    # Return the RGB values as a tuple
    return (r, g, b)

def getPixel2(x, y):
    # Calculate the coordinates of the region to capture
    x1 = x - (10 // 2)
    y1 = y - (10 // 2)
    x2 = x1 + 10
    y2 = y1 + 10

    # Get a screenshot of the region
    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))

    # Get the RGB values of the center pixel
    r, g, b = im.getpixel((5, 5))

    # Return the RGB values as a tuple
    return (r, g, b)
