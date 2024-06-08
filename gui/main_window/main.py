from pathlib import Path
from tkinter import (
    Toplevel,
    Frame,
    Canvas,
    Button,
    PhotoImage,
    messagebox,
    StringVar)

from PIL import Image, ImageTk

from gui.main_window.check.main import Checks
from gui.main_window.recor.main import Records
from gui.main_window.mater.main import Materials
from gui.main_window.guests.main import Clients
from gui.main_window.colors.main import Colors
from gui.main_window.expense.main import Expenses

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def main_window():
    MainWindow()


class MainWindow(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)

        self.title("مــصــبـغــة غــنـيــم")

        self.geometry("1250x680+50+15")
        self.configure(bg="#5E95FF")

        self.current_window = None
        self.current_window_label = StringVar()

        self.canvas = Canvas(
            self,
            bg="#5E95FF",
            height=680,
            width=1250,
            bd=0,
            highlightthickness=0,
            relief="ridge",
        )

        self.canvas.place(x=0, y=0)

        self.canvas.create_rectangle(
            265, 0.0, 1250.0, 680.0, fill="#FFFFFF", outline=""
        )

        # Add a frame rectangle
        self.sidebar_indicator = Frame(self, background="#FFFFFF")

        self.sidebar_indicator.place(x=0, y=133, height=47, width=7)

        button_image_1 = ImageTk.PhotoImage(Image.open("gui/main_window/assets/button_1.png"))
        self.home_btn = Button(
            self.canvas,
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.home_btn, "hom"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.home_btn.place(x=7.0, y=133.0, width=208.0, height=47.0)

        button_image_2 = ImageTk.PhotoImage(Image.open("gui/main_window/assets/button_2.png"))
        self.mater_btn = Button(
            self.canvas,
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.mater_btn, "mat"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.mater_btn.place(x=7.0, y=183.0, width=208.0, height=47.0)

        button_image_3 = ImageTk.PhotoImage(Image.open("gui/main_window/assets/button_3.png"))
        self.guests_btn = Button(
            self.canvas,
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.guests_btn, "gue"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.guests_btn.place(x=7.0, y=283.0, width=208.0, height=47.0)

        button_image_4 = ImageTk.PhotoImage(Image.open("gui/main_window/assets/button_4.png"))
        self.color_btn = Button(
            self.canvas,
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.color_btn, "col"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.color_btn.place(x=7.0, y=433.0, width=208.0, height=47.0)

        button_image_5 = ImageTk.PhotoImage(Image.open("gui/main_window/assets/button_5.png"))
        self.logout_btn = Button(
            self.canvas,
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.logout,
            relief="flat",
        )
        self.logout_btn.place(x=0.0, y=601.0, width=215.0, height=47.0)

        button_image_6 = ImageTk.PhotoImage(Image.open("gui/main_window/assets/button_6.png"))
        self.checks_btn = Button(
            self.canvas,
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.checks_btn, "chk"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.checks_btn.place(x=7.0, y=233.0, width=208.0, height=47.0)

        button_image_7 = ImageTk.PhotoImage(Image.open("gui/main_window/assets/button_7.png"))
        self.records_btn = Button(
            self.canvas,
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.records_btn, "roc"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.records_btn.place(x=7.0, y=333.0, width=208.0, height=47.0)

        button_image_8 = ImageTk.PhotoImage(Image.open("gui/main_window/assets/button_8.png"))
        self.expense_btn = Button(
            self.canvas,
            image=button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.handle_btn_press(self.expense_btn, "exp"),
            cursor='hand2', activebackground="#5E95FF",
            relief="flat",
        )
        self.expense_btn.place(x=7.0, y=383.0, width=208.0, height=47.0)

        self.heading = self.canvas.create_text(
            305.0,
            33.0,
            anchor="nw",
            text="Hello",
            fill="#5E95FF",
            font=("Montserrat Bold", 26 * -1),
        )

        self.canvas.create_text(
            28.0,
            31.0,
            anchor="nw",
            text="BlueLine",
            fill="#FFFFFF",
            font=("Montserrat Bold", 36 * -1),
        )

        self.canvas.create_text(
            1074.0,
            43.0,
            anchor="nw",
            text="Mustafa Salem",
            fill="#808080",
            font=("Montserrat Bold", 16 * -1),
        )

        self.canvas.create_text(
            471.0,
            263.0,
            anchor="nw",
            text="(The screens below",
            fill="#5E95FF",
            font=("Montserrat Bold", 48 * -1),
        )

        self.canvas.create_text(
            574.0,
            322.0,
            anchor="nw",
            text="will come here)",
            fill="#5E95FF",
            font=("Montserrat Bold", 48 * -1),
        )

        # Loop through windows and place them
        self.windows = {
            "mat": Materials(self),
            "chk": Checks(self),
            "gue": Clients(self),
            "col": Colors(self),
            "roc": Records(self),
            "exp": Expenses(self)
        }

        # self.handle_btn_press(self.home_btn, "hom")
        self.sidebar_indicator.place(x=0, y=133)

        self.resizable(False, False)
        self.mainloop()

    def place_sidebar_indicator(self):
        pass

    def logout(self):
        confirm = messagebox.askyesno(
            "Confirm log-out", "Do you really want to log out?"
        )
        if confirm:
            self.destroy()

    def handle_btn_press(self, caller, name):
        # Place the sidebar on respective button
        self.sidebar_indicator.place(x=0, y=caller.winfo_y())

        # Hide all screens
        for window in self.windows.values():
            window.place_forget()

        # Set ucrrent Window
        self.current_window = self.windows.get(name)

        # Show the screen of the button pressed
        self.windows[name].place(x=265, y=72, width=985.0, height=610.0)

        # Handle label change
        current_name = self.windows.get(name)._name.split("!")[-1].capitalize()
        self.canvas.itemconfigure(self.heading, text=current_name)

    def handle_dashboard_refresh(self):
        pass


'''db = sqlite3.connect('Materials.db')
db.cursor()
db.execute('INSERT INTO Color_T VALUES (:Name, :T_N)',
                   {
                       'Name': 'كاشمير',
                       'T_N': 'M_9x'
                   })
db.commit()'''


'''db = sqlite3.connect('Materials.db')
db.cursor()
db.execute(
    "CREATE TABLE Color_T (Name TEXT, T_N TEXT)")

db.commit()
db.close()'''
