import datetime
from pathlib import Path
from tkinter import (
    Frame, LabelFrame,
    Entry, Label, Button,
    ttk, IntVar, DoubleVar, StringVar)

from PIL import Image, ImageTk

from gui.main_window.colors.Add_Color.Add import AddColor
from gui.main_window.colors.Delete_Color.Del import Delete

from fucs import colors_ftchs, color_ftch_rate, materials_ftch

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def color():
    Colors()


class Colors(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.date = datetime.datetime.now().date()
        self.configure(bg="#FFFFFF")

        # ================variables================= #
        self.data_2 = {'weight': DoubleVar(), 'cost': IntVar(), 'total': IntVar(), 'rest': IntVar()}
        self.gettis = DoubleVar()
        self.color = StringVar()
        self.qun = IntVar()
        self.cname = StringVar()
        self.total = IntVar()
        color_vlu = colors_ftchs()

        self.rows = {'raw1': DoubleVar(), 'raw2': DoubleVar(), 'raw3': DoubleVar(), 'raw4': DoubleVar(),
                     'raw5': DoubleVar(), 'raw6': DoubleVar(), 'raw7': DoubleVar(),
                     'raw8': DoubleVar(), 'raw9': DoubleVar(), 'raw10': DoubleVar()}

        self.costs = {'raw1': DoubleVar(), 'raw2': DoubleVar(), 'raw3': DoubleVar(), 'raw4': DoubleVar(),
                      'raw5': DoubleVar(), 'raw6': DoubleVar(), 'raw7': DoubleVar(),
                      'raw8': DoubleVar(), 'raw9': DoubleVar(), 'raw10': DoubleVar()}

        self.mts = {'mts1': StringVar(), 'mts2': StringVar(), 'mts3': StringVar(), 'mts4': StringVar(),
                    'mts5': StringVar(), 'mts6': StringVar(), 'mts7': StringVar(),
                    'mts8': StringVar(), 'mts9': StringVar(), 'mts10': StringVar()}

        Label(self, text='نظام الـصـبـاغـات', fg='#5E95FF', font=('Tajawal', 18, 'bold'), bg='#FFF').place(x=415, y=20)
        self.label_txt('اختر اللـوان', x=800, y=100)
        self.label_txt('وزن الـحـامـل', x=800, y=140)
        self.label_txt('الـصـبـغـة', x=800, y=180), self.label_txt('الـوزن', x=635, y=180), self.label_txt('الـتـكلفة',
                                                                                                           x=455, y=180)
        self.str_txt(self.mts['mts1'], x=800, y=210), self.str_txt(self.rows['raw1'], x=635, y=210), self.str_txt(
            self.costs['raw1'], x=455, y=210)
        self.str_txt(self.mts['mts2'], x=800, y=240), self.str_txt(self.rows['raw2'], x=635, y=240), self.str_txt(
            self.costs['raw2'], x=455, y=240)
        self.str_txt(self.mts['mts3'], x=800, y=270), self.str_txt(self.rows['raw3'], x=635, y=270), self.str_txt(
            self.costs['raw3'], x=455, y=270)
        self.str_txt(self.mts['mts4'], x=800, y=300), self.str_txt(self.rows['raw4'], x=635, y=300), self.str_txt(
            self.costs['raw4'], x=455, y=300)
        self.str_txt(self.mts['mts5'], x=800, y=330), self.str_txt(self.rows['raw5'], x=635, y=330), self.str_txt(
            self.costs['raw5'], x=455, y=330)
        self.str_txt(self.mts['mts6'], x=800, y=360), self.str_txt(self.rows['raw6'], x=635, y=360), self.str_txt(
            self.costs['raw6'], x=455, y=360)
        self.str_txt(self.mts['mts7'], x=800, y=390), self.str_txt(self.rows['raw7'], x=635, y=390), self.str_txt(
            self.costs['raw7'], x=455, y=390)
        self.str_txt(self.mts['mts8'], x=800, y=420), self.str_txt(self.rows['raw8'], x=635, y=420), self.str_txt(
            self.costs['raw8'], x=455, y=420)
        self.str_txt(self.mts['mts9'], x=800, y=450), self.str_txt(self.rows['raw9'], x=635, y=450), self.str_txt(
            self.costs['raw9'], x=455, y=450)
        self.str_txt(self.mts['mts10'], x=800, y=480), self.str_txt(self.rows['raw10'], x=635, y=480), self.str_txt(
            self.costs['raw10'], x=455, y=480)
        self.label_txt('الاجمالي', x=455, y=520), self.str_txt(self.total, x=455, y=550)

        self.en_cname = ttk.Combobox(self, font=('Cairo', 12), justify='center', state='readonly',
                                     values=color_vlu, textvariable=self.cname)
        self.en_cname.place(x=453, y=110, width=150, height=25)
        self.en_kind = Entry(self, font=('Tajawal', 13), justify='center', bd=1, background='#f0f0f4',
                             textvariable=self.qun)
        self.en_kind.place(x=500, y=150, width=50, height=25)

        self.qun.trace_add("write", self.updatee)

        f2 = LabelFrame(self, text='إدارة الـصـبـاغـات', font=('Tajawal', 17, 'bold'), bd=10, fg='#5E95FF', bg='#FFF',
                        labelanchor='n')
        f2.place(x=40, y=240, width=340, height=220)

        self.button_image_3 = ImageTk.PhotoImage(Image.open("col_1.png"))
        button_3 = Button(f2, image=self.button_image_3, borderwidth=0, highlightthickness=0, command=AddColor,
                          relief="flat", cursor='hand2')
        button_3.place(x=67.0, y=30.0, width=190.0, height=48.0)

        self.button_image_5 = ImageTk.PhotoImage(Image.open("col_3.png"))
        button_5 = Button(f2, image=self.button_image_5, borderwidth=0, highlightthickness=0, command=Delete,
                          relief="flat", cursor='hand2')
        button_5.place(x=67.0, y=100.0, width=190.0, height=48.0)

    def label_txt(self, txt, x, y):
        Label(self, font=('Tajawal', 12), fg='#5E95FF', bg='#FFF', text=txt).place(x=x, y=y)

    def str_txt(self, txt, x, y):
        Label(self, font=('Tajawal', 12), fg='#5E95FF', bg='#FFF', text='', textvariable=txt).place(x=x, y=y)

    def updatee(self, *args):
        li = color_ftch_rate(self.cname.get())
        try:
            for i in li:
                self.mts['mts1'].set(i[1])
                self.rows['raw1'].set(i[2] * self.qun.get())
                self.mts['mts2'].set(i[3])
                self.rows['raw2'].set(i[4] * self.qun.get())
                self.mts['mts3'].set(i[5])
                self.rows['raw3'].set(i[6] * self.qun.get())
                self.mts['mts4'].set(i[7])
                self.rows['raw4'].set(i[8] * self.qun.get())
                self.mts['mts5'].set(i[9])
                self.rows['raw5'].set(i[10] * self.qun.get())
                self.mts['mts6'].set(i[11])
                self.rows['raw6'].set(i[12] * self.qun.get())
                self.mts['mts7'].set(i[13])
                self.rows['raw7'].set(i[14] * self.qun.get())
                self.mts['mts8'].set(i[15])
                self.rows['raw8'].set(i[16] * self.qun.get())
                self.mts['mts9'].set(i[17])
                self.rows['raw9'].set(i[18] * self.qun.get())
                self.mts['mts10'].set(i[19])
                self.rows['raw10'].set(i[20] * self.qun.get())
        except:
            pass
        self.gettis = 0
        if self.mts['mts1'].get() != '':
            self.costs['raw1'].set(materials_ftch(name=self.mts['mts1'].get()) * self.rows['raw1'].get())
            self.gettis = (self.costs['raw1'].get())
        if self.mts['mts2'].get() != '':
            self.costs['raw2'].set(materials_ftch(name=self.mts['mts2'].get()) * self.rows['raw2'].get())
            self.gettis += self.costs['raw2'].get()
        if self.mts['mts3'].get() != '':
            self.costs['raw3'].set(materials_ftch(name=self.mts['mts3'].get()) * self.rows['raw3'].get())
            self.gettis += self.costs['raw3'].get()
        if self.mts['mts4'].get() != '':
            self.costs['raw4'].set(materials_ftch(name=self.mts['mts4'].get()) * self.rows['raw4'].get())
            self.gettis += self.costs['raw4'].get()
        if self.mts['mts5'].get() != '':
            self.costs['raw5'].set(materials_ftch(name=self.mts['mts5'].get()) * self.rows['raw5'].get())
            self.gettis += self.costs['raw5'].get()
        if self.mts['mts6'].get() != '':
            self.costs['raw6'].set(materials_ftch(name=self.mts['mts6'].get()) * self.rows['raw6'].get())
            self.gettis += self.costs['raw6'].get()
        if self.mts['mts7'].get() != '':
            self.costs['raw7'].set(materials_ftch(name=self.mts['mts7'].get()) * self.rows['raw7'].get())
            self.gettis += self.costs['raw7'].get()
        if self.mts['mts8'].get() != '':
            self.costs['raw8'].set(materials_ftch(name=self.mts['mts8'].get()) * self.rows['raw8'].get())
            self.gettis += self.costs['raw8'].get()
        if self.mts['mts9'].get() != '':
            self.costs['raw9'].set(materials_ftch(name=self.mts['mts9'].get()) * self.rows['raw9'].get())
            self.gettis += self.costs['raw8'].get()
        if self.mts['mts10'].get() != '':
            self.costs['raw10'].set(materials_ftch(name=self.mts['mts10'].get()) * self.rows['raw10'].get())
            self.gettis += self.costs['raw10'].get()
        self.total.set(self.gettis)
