# PySpeedMacro

PyAutoGUI is a GUI automation Python module for creating macros and scripting. It is used to programmatically control the mouse & keyboard.

**Pip install**
```
pip install PySpeedMacro
```

Source code available at https://github.com/BaneofRogue/PySpeedMacro

If you need help installing Python, visit 

# Dependencies

*This has only been tested on Windows 10 as of updating this document.*

**Pillow**
```
pip install pillow
```

**OpenCV Python**
```
pip install opencv-python
```

**Logging**
```
pip install logging
```

# Disclaimers

*This is my first ever python library so code may be spaghetti.*

Please not that many new functions and updates will be posted as time progresses.

This was inspired by PyAutoGui, PyDirectInput, and Mouse! 

I use these modules a lot, but I always wished I could have a faster and more simpler code library to create scripts.

**Thank you to all the people who contributed to those projects.**

# How does PySpeedMacro work?

Working with python to create macros and scripts can be confusing and overwhelming. PySpeedMacro's job is to remove the complexity behind creating scripts and macros!

**PySpeedMacro has only been tested on Windows 10.**

Windows:
- The already integrated win32api is used to interact with the Windows API, controlling the mouse and simulating inputs.
- OpenCV for Python is used to search for images on screen, which turns out to be faster than PyAutoGui.