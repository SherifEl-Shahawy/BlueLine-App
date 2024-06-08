import tkinter as tk
from gui.main_window.main import main_window

# Main window constructor
root = tk.Tk()  # Make temporary window for app to start
root.withdraw()  # WithDraw the window


if __name__ == "__main__":

    main_window()

    root.mainloop()
