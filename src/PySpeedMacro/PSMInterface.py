import tkinter as tk


class Interface:

    def __init__(self, root):

        self.root = root
        self.shapes = []
        self.keybind_active = False

        self.center_x = root.winfo_screenwidth() // 2
        self.center_y = root.winfo_screenheight() // 2
    

    def TRANSPARENT_COLOR(color="black"):
        return color


    def create_interface(self, titleText="Interface"):

        background=self.TRANSPARENT_COLOR

        self.root.title(titleText)
        self.root.attributes("-fullscreen", True)
        self.root.wm_attributes('-transparentcolor', background)
        self.root.attributes("-topmost", True)
        self.canvas = tk.Canvas(self.root, bg=background, highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        def refresh_topmost():
            self.root.attributes("-topmost", True)
            self.root.after(1000, refresh_topmost)

        self.root.after(1000, refresh_topmost)


    def set_circle(self, color, x, y, radius, thickness=2, filler=False, fancy=True):
        if filler:
            circle = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color, outline = color, width=thickness)
        else:
            circle = self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=self.TRANSPARENT_COLOR, outline = color, width=thickness)
        self.shapes.append(circle)
        if fancy:
            line = self.canvas.create_line(x, y, self.center_x, self.center_y, fill = color, width=thickness)
            self.shapes.append(line)


    def set_square(self, color, x, y, radius, thickness=2, filler=False, fancy=True):
        if filler:
            square = self.canvas.create_rectangle(x - radius, y - radius, x + radius, y + radius, fill=color, outline=color, width=thickness)
        else:
            square = self.canvas.create_rectangle(x - radius, y - radius, x + radius, y + radius, fill=self.TRANSPARENT_COLOR, outline=color, width=thickness)
        self.shapes.append(square)
        if fancy:
            line = self.canvas.create_line(x + radius / 2, y + radius / 2, self.center_x, self.center_y, fill=color, width=thickness)
            self.shapes.append(line)


    def set_rectangle(self, color, x, y, width, height, thickness=2, filler=False, fancy=True):
        if filler:
            rectangle = self.canvas.create_rectangle(x, y, x + width, y + height, fill=color, outline=color, width=thickness)
        else:
            rectangle = self.canvas.create_rectangle(x, y, x + width, y + height, fill=self.TRANSPARENT_COLOR, outline=color, width=thickness)
        self.shapes.append(rectangle)
        if fancy:
            line = self.canvas.create_line(x + width / 2, y + height / 2, self.center_x, self.center_y, fill=color, width=thickness)
            self.shapes.append(line)


    def create_center_text(self, color, text):
        text = self.canvas.create_text(self.center_x, self.center_y, text=text, fill=color)
        self.shapes.append(text)


    def clear_canvas(self):

        for shape in self.shapes:
            self.canvas.delete(shape)
        self.shapes = []


root = tk.Tk()
interface = Interface(root)

interface.TRANSPARENT_COLOR = "yellow"

interface.create_interface()

interface.set_circle("red",500, 500, 100)

interface.set_rectangle("green", 300, 300, 100, 125)

root.mainloop()