import tkinter as tk
import math
import time
from PIL import Image, ImageTk

class Clock:
    def __init__(self, root):
        self.root = root
        self.root.title("Real-time Clock")
        self.root.geometry("400x400")
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Load clock face image
        self.clock_face = Image.open("clock_face.png").resize((300, 300))
        self.clock_face = ImageTk.PhotoImage(self.clock_face)
        self.canvas.create_image(200, 200, image=self.clock_face)

        # Update clock hands every second
        self.update_clock()

    def draw_hand(self, length, angle, color, width):
        """Draws a clock hand on the canvas."""
        angle = math.radians(angle)
        x = 200 + length * math.sin(angle)
        y = 200 - length * math.cos(angle)
        self.canvas.create_line(200, 200, x, y, fill=color, width=width)

    def update_clock(self):
        """Updates the clock hands based on the current time."""
        self.canvas.delete("hands")

        # Get current time
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # Calculate angles for each hand
        second_angle = 6 * seconds
        minute_angle = 6 * minutes + seconds / 10
        hour_angle = 30 * hours + minutes / 2

        # Draw hour, minute, and second hands
        self.draw_hand(80, hour_angle, "black", 6)
        self.draw_hand(110, minute_angle, "blue", 4)
        self.draw_hand(130, second_angle, "red", 2)

        # Schedule the next update after 1000 ms (1 second)
        self.root.after(1000, self.update_clock)

# Create the main window and run the clock
root = tk.Tk()
clock = Clock(root)
root.mainloop()
