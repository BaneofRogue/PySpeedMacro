import win32api
import win32con
import time

def accurate_delay(delay):
    _ = time.perf_counter() + delay
    while time.perf_counter() < _:
        pass

class WinMouse:
    def __init__(self):
        self.position = (0, 0)
        self.left_down = False
        self.right_down = False

    def move(self, x, y, duration=0):
        if duration <= 0:
            win32api.SetCursorPos((x, y))
            print(x)
            print(y)
            self.position = (x, y)
        else:
            start_x, start_y = self.position
            num_steps = max(abs(x - start_x), abs(y - start_y))
            sleep_amount = duration / num_steps

            for i in range(num_steps):
                tween = (i + 1) / num_steps
                tween_x = int(round(start_x + (x - start_x) * tween))
                tween_y = int(round(start_y + (y - start_y) * tween))
                win32api.SetCursorPos((tween_x, tween_y))
                self.position = (tween_x, tween_y)
                accurate_delay(sleep_amount)

    def press(self, button):
        if button == "left":
            if not self.left_down:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                self.left_down = True
        elif button == "right":
            if not self.right_down:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                self.right_down = True

    def release(self, button):
        if button == "left":
            if self.left_down:
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                self.left_down = False
        elif button == "right":
            if self.right_down:
                win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
                self.right_down = False

    def click(self, button, separation):
        self.press(button)
        accurate_delay(separation)
        self.release(button)