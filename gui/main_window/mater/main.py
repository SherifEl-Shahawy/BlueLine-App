import datetime
from pathlib import Path

from tkinter import (
    Frame, Label, Entry,
    LabelFrame, Button, messagebox,
    IntVar, StringVar, ttk)

from PIL import Image, ImageTk

from gui.main_window.mater.Add_deal.Add import AddDealer
from gui.main_window.mater.Edit_deal.Edits import EditDel
from gui.main_window.mater.Paid.Add_paid import AddPayment
from gui.main_window.mater.Profile_Review.Profile import Review

from fucs import mater_store, mater_ftchs, mater_upd, kind_ftchs, q_update

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def mater_fuc():
    Materials()


class Materials(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(bg="#FFF")
        self.date = datetime.datetime.now().date()

        # ================variables================= #
        self.data_1 = {'quantity': IntVar(), 'cost': IntVar(), 'total': IntVar(), 'rest': IntVar()}
        self.pro = StringVar()
        self.ccname = StringVar()
        name_vlu = mater_ftchs()
        material_vlu = kind_ftchs()

        Label(self, text='تـسـجيـل الـمـواد', fg='#5E95FF', font=('Tajawal', 18, 'bold'), bg='#FFF').place(x=415,
                                                                                                           y=20)
        self.label_txt('اسـم المـورد', x=820, y=100)
        self.label_txt('الـصـنـف', x=820, y=160), self.label_txt('الكمية', x=830, y=220)
        self.label_txt('السعر', x=828, y=280), self.label_txt('الاجمالي', x=815, y=340)
        self.label_txt('التاريخ', x=830, y=400)

        self.en_kind = ttk.Combobox(self, font=('Cairo', 12), justify='center', state='readonly',
                                    values=name_vlu, textvariable=self.ccname)
        self.en_kind.place(x=453, y=110, width=200, height=25)
        self.en_prod = ttk.Combobox(self, font=('Cairo', 12), justify='center', state='readonly',
                                    values=material_vlu, textvariable=self.pro)
        self.en_prod.place(x=453, y=170, width=200, height=25)
        self.en_quantity = Entry(self, font=('Tajawal', 13), justify='center', background='#f0f0f4', bd=1,
                                 textvariable=self.data_1['quantity'])
        self.en_quantity.place(x=503, y=230, width=150, height=25)
        self.en_cost = Entry(self, font=('Tajawal', 13), justify='center', bd=1, textvariable=self.data_1['cost'],
                             background='#f0f0f4')
        self.en_cost.place(x=503, y=290, width=150, height=25)
        self.en_cost.bind('<KeyRelease>', self.checks)
        self.en_total = Entry(self, font=('Tajawal', 13), justify='center', bd=1, textvariable=self.data_1['total'],
                              background='#f0f0f4')
        self.en_total.place(x=503, y=350, width=150, height=25)
        self.en_date = Entry(self, font=('Tajawal', 13), justify='center', bd=1, background='#f0f0f4')
        self.en_date.insert(0, str(self.date))
        self.en_date.place(x=503, y=410, width=150, height=25)

        f2 = LabelFrame(self, text='إدارة الموردين', font=('Tajawal', 17, 'bold'), bd=10, fg='#5E95FF', bg='#FFF',
                        labelanchor='n')
        f2.place(x=40, y=220, width=340, height=340)

        self.button_image_0 = ImageTk.PhotoImage(Image.open("gui/main_window/assets/add.png"))
        button_0 = Button(f2, image=self.button_image_0, borderwidth=0, highlightthickness=0, command=AddDealer,
                          relief="flat", cursor='hand2')
        button_0.place(x=67.0, y=30.0, width=190.0, height=48.0)
        
        self.button_image_1 = ImageTk.PhotoImage(Image.open("gui/main_window/assets/Edits.png"))
        button_1 = Button(f2, image=self.button_image_1, borderwidth=0, highlightthickness=0, command=EditDel,
                          relief="flat", cursor='hand2')
        button_1.place(x=67.0, y=90.0, width=190.0, height=48.0)

        self.button_image_2 = ImageTk.PhotoImage(Image.open("gui/main_window/assets/pay.png"))
        button_2 = Button(f2, image=self.button_image_2, borderwidth=0, highlightthickness=0, command=AddPayment,
                          relief="flat", cursor='hand2')
        button_2.place(x=67.0, y=150.0, width=190.0, height=48.0)

        self.button_image_3 = ImageTk.PhotoImage(Image.open("gui/main_window/assets/review.png"))
        button_3 = Button(f2, image=self.button_image_3, borderwidth=0, highlightthickness=0, command=Review,
                          relief="flat", cursor='hand2')
        button_3.place(x=67.0, y=210.0, width=190.0, height=48.0)

        self.button_image_4 = ImageTk.PhotoImage(Image.open("gui/main_window/assets/mat_2.png"))
        button_4 = Button(self, image=self.button_image_4, borderwidth=0, highlightthickness=0, command=self.submit,
                          relief="flat", cursor='hand2')
        button_4.place(x=645.0, y=470.0, width=190.0, height=48.0)

        self.button_image_5 = ImageTk.PhotoImage(Image.open("gui/main_window/assets/mat_3.png"))
        button_5 = Button(self, image=self.button_image_5, borderwidth=0, highlightthickness=0, command=self.clear,
                          relief="flat", cursor='hand2')
        button_5.place(x=645.0, y=540.0, width=190.0, height=48.0)

    def checks(self, *args):
        try:
            typed_quan = int(self.data_1['quantity'].get())
            typed_costx = int(self.data_1['cost'].get())
        except:
            typed_quan, typed_costx = 0, 0
        self.data_1['total'].set(typed_quan * typed_costx)

    def label_txt(self, txt, x, y):
        Label(self, font=('Tajawal', 12), fg='#5E95FF', bg='#FFF', text=txt).place(x=x, y=y)

    def submit(self):
        try:
            int(self.data_1['quantity'].get())
            int(self.data_1['cost'].get())
            int(self.data_1['total'].get())
        except:
            messagebox.showerror(
                "Error", "خطأ، بعض البيانات التي قمت بأدخالها غير صحيحة\nتأكد ان الارقام مكتوبه بالانجليزية")
        else:
            op = messagebox.askyesno("Save Data", "هـل انـت مـتـأكـد انـك تـرغـب بـتـخـزيـن تلـك البـيانات ؟")
            if op > 0:
                mater_store(name_1=self.ccname.get(), kind=self.pro.get(), quant=self.data_1['quantity'].get(),
                            price=self.data_1['cost'].get(), total=self.data_1['total'].get(),
                            date_1=self.en_date.get())

                mater_upd(name_1=self.ccname.get(), total=self.data_1['total'].get())
                q_update(prod=self.pro.get(), qant=self.data_1['quantity'].get(), price=self.data_1['cost'].get())

    def clear(self):
        self.data_1['quantity'].set(0), self.data_1['cost'].set(0), self.data_1['total'].set(0)
        self.pro.set("")
