from pathlib import Path
import datetime
from tkinter import ttk
from tkinter import (
    Frame,
    Entry, Label,
    Scrollbar, Button,
    messagebox, IntVar, StringVar,
    VERTICAL, RIGHT, Y, NO, E, BOTH)

from PIL import Image, ImageTk

from gui.main_window.check.del_check.Delete import DelCheck

from fucs import check_store, check_ftch

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def check():
    Checks()


class Checks(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.storageTree = None
        self.scroll_y = None
        self.f9 = None
        self.parent = parent
        self.configure(bg="#FFFFFF")
        self.date = datetime.datetime.now().date()
        # ================variables================= #
        self.data_n = {'from_1': StringVar(), 'to_2': StringVar(), 'owner_3': StringVar(), 'bank_n': StringVar(),
                       'deti': StringVar()}
        self.payment = IntVar()

        Label(self, text='حـركـه الـشـيـكـات', fg='#5E95FF', font=('Tajawal', 18, 'bold'), bg='#FFF').place(x=415, y=20)
        self.label_txt('الـتـاريـخ', x=870, y=70), self.label_txt('مـبـلـغ', x=730, y=70)
        self.label_txt('مــن', x=580, y=70), self.label_txt('إلــي', x=405, y=70)
        self.label_txt('صـاحـب الـشـيـك', x=170, y=70), self.label_txt('بـنـك', x=50, y=70)
        self.label_txt('تـفـاصـيـل اضـافـيـه', x=680, y=170)
        
        self.en_date = Entry(self, font=('Tajawal', 13), justify='center', bd=1, background='#f0f0f4')
        self.en_date.insert(0, str(self.date))
        self.en_date.place(x=850, y=110, width=100, height=25)
        self.en_paym = Entry(self, font=('Tajawal', 13), justify='center', bd=1, background='#f0f0f4',
                             textvariable=self.payment)
        self.en_paym.place(x=710, y=110, width=100, height=25)
        self.en_from = Entry(self, font=('Tajawal', 13), justify='right', bd=1, background='#f0f0f4',
                             textvariable=self.data_n['from_1'])
        self.en_from.place(x=520, y=110, width=150, height=25)
        self.en_to = Entry(self, font=('Tajawal', 13), justify='right', bd=1, background='#f0f0f4',
                           textvariable=self.data_n['to_2'])
        self.en_to.place(x=340, y=110, width=150, height=25)
        self.en_owner = Entry(self, font=('Tajawal', 13), justify='right', bd=1, background='#f0f0f4',
                              textvariable=self.data_n['owner_3'])
        self.en_owner.place(x=160, y=110, width=150, height=25)
        self.en_bank = Entry(self, font=('Tajawal', 13), justify='center', bd=1, background='#f0f0f4',
                             textvariable=self.data_n['bank_n'])
        self.en_bank.place(x=25, y=110, width=100, height=25)
        self.en_details = Entry(self, font=('Tajawal', 13), justify='center', bd=1, background='#f0f0f4',
                                textvariable=self.data_n['deti'])
        self.en_details.place(x=170, y=170, width=450, height=40)

        self.button_image_1 = ImageTk.PhotoImage(Image.open("chk_del.png"))
        button_1 = Button(self, image=self.button_image_1, borderwidth=0, highlightthickness=0, command=DelCheck,
                          relief="flat", cursor='hand2')
        button_1.place(x=250.0, y=220.0, width=190.0, height=48.0)

        self.button_image_2 = ImageTk.PhotoImage(Image.open("check_dn.png"))
        button_2 = Button(self, image=self.button_image_2, borderwidth=0, highlightthickness=0, command=self.submit,
                          relief="flat", cursor='hand2')
        button_2.place(x=550.0, y=220.0, width=190.0, height=48.0)

        self.reviews()

    def submit(self):
        try:
            int(self.payment.get())
        except:
            messagebox.showerror(
                "Error", "خطأ، بعض البيانات التي قمت بأدخالها غير صحيحة\nتأكد ان الارقام مكتوبه بالانجليزية")
        else:
            op = messagebox.askyesno("Save Data", "هـل انـت مـتـأكـد انـك تـرغـب بـتـخـزيـن تلـك البـيانات ؟")
            if op > 0:
                check_store(date_1=self.en_date.get(), pay=self.payment.get(), from_1=self.data_n['from_1'].get(),
                            tor=self.data_n['to_2'].get(), owner=self.data_n['owner_3'].get(),
                            bank=self.data_n['bank_n'].get(), detail=self.data_n['deti'].get())
                self.reviews()

    def label_txt(self, txt, x, y):
        Label(self, font=('Tajawal', 12), fg='#5E95FF', bg='#FFF', text=txt).place(x=x, y=y)

    def reviews(self):
        self.f9 = Frame(self, bg='#FFF')
        self.f9.place(x=120, y=280, width=750, height=310)
        self.scroll_y = Scrollbar(self.f9, orient=VERTICAL)
        self.storageTree = ttk.Treeview(self.f9, yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.storageTree.yview)
        self.storageTree['columns'] = ('Bank', 'Owner', 'From', 'To', 'Payment', 'Date', 'Detail')
        self.storageTree.column('#0', width=0, stretch=NO)
        self.storageTree.column('Detail', width=100, minwidth=40, anchor='center')
        self.storageTree.column('Bank', width=50, minwidth=40, anchor='center')
        self.storageTree.column('Owner', width=80, minwidth=40, anchor='center')
        self.storageTree.column('From', width=80, minwidth=30, anchor='center')
        self.storageTree.column('To', width=80, minwidth=50, anchor='center')
        self.storageTree.column('Payment', width=60, minwidth=50, anchor='center')
        self.storageTree.column('Date', width=50, minwidth=30, anchor=E)

        self.storageTree.heading('#0', text='', anchor='center')
        self.storageTree.heading('Detail', text='تفاصيل', anchor='center')
        self.storageTree.heading('Bank', text='بـنـك', anchor='center')
        self.storageTree.heading('Owner', text='صاحب الشيك', anchor='center')
        self.storageTree.heading('From', text='إلــي', anchor='center')
        self.storageTree.heading('To', text='مــن', anchor='center')
        self.storageTree.heading('Payment', text='مـبـلـغ', anchor='center')
        self.storageTree.heading('Date', text='الـنـاريـخ', anchor=E)
        self.storageTree.pack(fill=BOTH, expand=1)

        recordy = check_ftch()

        self.storageTree.tag_configure('oddrow', background='white')
        self.storageTree.tag_configure('evenrow', background='skyblue')
        row_no = 0
        for record in recordy:
            if row_no % 2 == 0:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[5], record[4], record[3], record[2], record[1], record[0], record[6]),
                                        tags=('evenrow',))
            else:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[5], record[4], record[3], record[2], record[1], record[0], record[6]),
                                        tags=('oddrow',))
            row_no += 1
