from PySpeedMacro import PSMMouse
import keyboard
import time

#@psm.timer
def test():

    r, g, b = psm.getPixel(100, 100)

    print("{}, {}, {}").format(r, g, b)

#psm.timer
def test2():

    r, g, b = psm.getPixel2(100, 100)

    print("{}, {}, {}").format(r, g, b)


test()
test2()
