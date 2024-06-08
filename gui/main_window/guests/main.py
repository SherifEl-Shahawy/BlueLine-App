import datetime
from pathlib import Path
from tkinter import (
    Frame, LabelFrame,
    Entry, Label, Button,
    ttk, messagebox,
    IntVar, DoubleVar, StringVar)

from PIL import Image, ImageTk

from gui.main_window.guests.Add_Client.Add import AddClient
from gui.main_window.guests.Edit_gus.Edits import EditDel
from gui.main_window.guests.Client_pay.Add_paid import AddPayment
from gui.main_window.guests.Profile_Review.Profile import Review

from fucs import guests_store, guests_ftchs, guests_upd, client_rets_f, client_upd_rt, colors_ftchs

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def client():
    Clients()


class Clients(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.date = datetime.datetime.now().date()
        self.configure(bg="#FFFFFF")

        # ================variables================= #
        self.data_2 = {'weight': DoubleVar(), 'cost': IntVar(), 'total': IntVar(), 'rest': IntVar()}
        self.color = StringVar()
        self.kind = StringVar()
        self.cname = StringVar()
        self.boly = 0
        self.restn = IntVar()
        name_vlu = guests_ftchs()
        colors_vlu = colors_ftchs()

        Label(self, text='نـظـام الـعـملاء', fg='#5E95FF', font=('Tajawal', 18, 'bold'), bg='#FFF').place(x=415, y=20)
        self.label_txt('اسـم الـعمـيـل', x=800, y=100)
        self.label_txt('الـصـنـف', x=820, y=160), self.label_txt('الـلون', x=830, y=220)
        self.label_txt('الـوزن', x=830, y=280)
        self.label_txt('السعر', x=828, y=340), self.label_txt('التاريخ', x=830, y=460)
        self.label_txt('الاجمالي', x=815, y=400)

        self.en_cname = ttk.Combobox(self, font=('Cairo', 12), justify='center', state='readonly',
                                     values=name_vlu, textvariable=self.cname)
        self.en_cname.place(x=453, y=110, width=200, height=25)
        self.en_kind = Entry(self, font=('Tajawal', 13), justify='right', bd=1, background='#f0f0f4',
                             textvariable=self.kind)
        self.en_kind.place(x=453, y=170, width=200, height=25)
        self.en_color = ttk.Combobox(self, font=('Cairo', 12), justify='center', state='readonly',
                                     values=colors_vlu, textvariable=self.color)
        self.en_color.place(x=503, y=230, width=150, height=25)
        self.en_weight = Entry(self, font=('Tajawal', 13), justify='center', bd=1, background='#f0f0f4',
                               textvariable=self.data_2['weight'])
        self.en_weight.place(x=503, y=290, width=150, height=25)
        self.en_cost = Entry(self, font=('Tajawal', 13), justify='center', bd=1, background='#f0f0f4',
                             textvariable=self.data_2['cost'])
        self.en_cost.place(x=503, y=350, width=150, height=25)
        self.en_cost.bind('<KeyRelease>', self.checks)
        self.en_total = Entry(self, font=('Tajawal', 13), justify='center', bd=1, background='#f0f0f4',
                              textvariable=self.data_2['total'])
        self.en_total.place(x=503, y=410, width=150, height=25)
        self.en_date = Entry(self, font=('Tajawal', 13), justify='center', bd=1, background='#f0f0f4')
        self.en_date.insert(0, str(self.date))
        self.en_date.place(x=503, y=470, width=150, height=25)

        self.button_image_1 = ImageTk.PhotoImage(Image.open("gus_2.png"))
        button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0, command=self.submit,
                          relief="flat", cursor='hand2')
        button_1.place(x=465.0, y=535.0, width=190.0, height=48.0)

        self.button_image_2 = ImageTk.PhotoImage(Image.open("gus_3.png"))
        button_2 = Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0, command=self.clear,
                          relief="flat", cursor='hand2')
        button_2.place(x=690.0, y=535.0, width=190.0, height=48.0)

        f2 = LabelFrame(self, text='إدارة الـعـمـلاء', font=('Tajawal', 17, 'bold'), bd=10, fg='#5E95FF', bg='#FFF',
                        labelanchor='n')
        f2.place(x=40, y=240, width=340, height=340)

        self.button_image_3 = ImageTk.PhotoImage(Image.open("add_gus.png"))
        button_3 = Button(f2, image=self.button_image_3, borderwidth=0, highlightthickness=0, command=AddClient,
                          relief="flat", cursor='hand2')
        button_3.place(x=67.0, y=30.0, width=190.0, height=48.0)
        
        self.button_image_0 = ImageTk.PhotoImage(Image.open("gus_4.png"))
        button_0 = Button(f2, image=self.button_image_0, borderwidth=0, highlightthickness=0, command=EditDel,
                          relief="flat", cursor='hand2')
        button_0.place(x=67.0, y=90.0, width=190.0, height=48.0)

        self.button_image_4 = ImageTk.PhotoImage(Image.open("gus_1.png"))
        button_4 = Button(f2, image=self.button_image_4, borderwidth=0, highlightthickness=0, command=AddPayment,
                          relief="flat", cursor='hand2')
        button_4.place(x=67.0, y=150.0, width=190.0, height=48.0)

        self.button_image_5 = ImageTk.PhotoImage(Image.open("view_gus.png"))
        button_5 = Button(f2, image=self.button_image_5, borderwidth=0, highlightthickness=0, command=Review,
                          relief="flat", cursor='hand2')
        button_5.place(x=67.0, y=210.0, width=190.0, height=48.0)

    def restin(self, *args):
        self.restn.set(client_rets_f(name_1=self.cname.get()))

    def label_txt(self, txt, x, y):
        Label(self, font=('Tajawal', 12), fg='#5E95FF', bg='#FFF', text=txt).place(x=x, y=y)

    def checks(self, *args):
        try:
            typed_quan = int(self.data_2['weight'].get())
            typed_costx = int(self.data_2['cost'].get())
        except:
            typed_quan, typed_costx = 0, 0
        self.data_2['total'].set(typed_quan * typed_costx)

    def submit(self):
        try:
            int(self.data_2['weight'].get())
            int(self.data_2['cost'].get())
            int(self.data_2['total'].get())
        except:
            messagebox.showerror(
                "Error", "خطأ، بعض البيانات التي قمت بأدخالها غير صحيحة\nتأكد ان الارقام مكتوبه بالانجليزية")
        else:
            op = messagebox.askyesno("Save Data", "هـل انـت مـتـأكـد انـك تـرغـب بـتـخـزيـن تلـك البـيانات ؟")
            if op > 0:
                guests_store(name_1=self.cname.get(), prod=self.kind.get(), color=self.color.get(),
                             weight=self.data_2['weight'].get(), price=self.data_2['cost'].get(),
                             total=self.data_2['total'].get(), date_1=self.en_date.get())

                guests_upd(name_1=self.cname.get(), total=self.data_2['total'].get())

    def clear(self):
        self.data_2['weight'].set(0), self.data_2['cost'].set(0), self.data_2['total'].set(0)
        self.kind.set(""), self.color.set("")

    def rest_btn(self):
        client_upd_rt(name_1=self.cname.get(), pay=self.data_2['rest'].get())
        self.restin()
