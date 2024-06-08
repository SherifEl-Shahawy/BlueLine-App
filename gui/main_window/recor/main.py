import datetime
from pathlib import Path
from tkinter import (
    Frame,
    Label,
    Button,
    Scrollbar,
    W, Y, BOTH, NO, E, RIGHT, VERTICAL)
from tkinter import ttk

from fucs import check_ftch, mater_price_ftchs, client_ftch, mater_quant_ftchs

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def record_fuc():
    Records()


class Records(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(bg="#FFF")
        self.date = datetime.datetime.now().date()
        self.storageTree = None
        self.scroll_y = None
        self.f9 = None

        Label(self, text='مـعـرض الـسـجـلات', fg='#5E95FF', font=('Tajawal', 18, 'bold'), bg='#FFF').place(x=415,
                                                                                                             y=20)

        Label(self, text='عـرض حـسـب', fg='#5E95FF', font=('Tajawal', 14), bg='#FFF').place(x=815, y=80)

        self.en_kind = ttk.Combobox(self, font=25, justify='center', state='readonly')
        self.en_kind['values'] = ('اسـعـار الـمـواد', 'الــمــخــزون', 'حـكـايـات الـعـمـلاء', 'حـركـة الـشـيـكـات')
        self.en_kind.current(1)
        self.en_kind.place(x=585, y=90, width=150, height=25)

        self.reg_s1 = Button(self, text='بــحــث', fg='#5E95FF', font=('arial', 12, 'bold'),
                             width=9, height=1, highlightbackground='#FFF', command=self.search_btn)
        self.reg_s1.place(x=400, y=90)

    def search_btn(self):
        if self.en_kind.get() == 'اسـعـار الـمـواد':
            self.material_price()
        elif self.en_kind.get() == 'الــمــخــزون':
            self.material_quantity()
        elif self.en_kind.get() == 'حـكـايـات الـعـمـلاء':
            self.clients()
        elif self.en_kind.get() == 'حـركـة الـشـيـكـات':
            self.reviews_check()

    def material_price(self, *args):
        self.f9 = Frame(self, bg='#FFF')
        self.f9.place(x=100, y=190, width=750, height=400)
        self.scroll_y = Scrollbar(self.f9, orient=VERTICAL)
        self.storageTree = ttk.Treeview(self.f9, yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.storageTree.yview)
        self.storageTree['columns'] = ('Name', 'Price')
        self.storageTree.column('#0', width=0, stretch=NO)
        self.storageTree.column('Name', width=240, minwidth=180, anchor='center')
        self.storageTree.column('Price', width=170, minwidth=120, anchor='center')

        self.storageTree.heading('#0', text='', anchor=W)
        self.storageTree.heading('Name', text='اسم الصنف', anchor='center')
        self.storageTree.heading('Price', text='السعر', anchor='center')

        self.storageTree.pack(fill=BOTH, expand=1)

        rec_price = mater_price_ftchs()

        self.storageTree.tag_configure('oddrow', background='white')
        self.storageTree.tag_configure('evenrow', background='skyblue')
        row_no = 0
        for record in rec_price:
            if row_no % 2 == 0:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[0], record[1]),
                                        tags=('evenrow',))
            else:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[0], record[1]),
                                        tags=('oddrow',))
            row_no += 1

    def material_quantity(self, *args):
        self.f9 = Frame(self, bg='#FFF')
        self.f9.place(x=100, y=190, width=750, height=400)
        self.scroll_y = Scrollbar(self.f9, orient=VERTICAL)
        self.storageTree = ttk.Treeview(self.f9, yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.storageTree.yview)
        self.storageTree['columns'] = ('Name', 'Quantity')
        self.storageTree.column('#0', width=0, stretch=NO)
        self.storageTree.column('Name', width=240, minwidth=180, anchor='center')
        self.storageTree.column('Quantity', width=170, minwidth=120, anchor='center')

        self.storageTree.heading('#0', text='', anchor=W)
        self.storageTree.heading('Name', text='اسم الصنف', anchor='center')
        self.storageTree.heading('Quantity', text='الـكـمـيـات', anchor='center')

        self.storageTree.pack(fill=BOTH, expand=1)

        rec_quant = mater_quant_ftchs()

        self.storageTree.tag_configure('oddrow', background='white')
        self.storageTree.tag_configure('evenrow', background='skyblue')
        row_no = 0
        for record in rec_quant:
            if row_no % 2 == 0:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[0], record[1]),
                                        tags=('evenrow',))
            else:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[0], record[1]),
                                        tags=('oddrow',))
            row_no += 1

    def clients(self, *args):
        self.f9 = Frame(self, bg='#FFF')
        self.f9.place(x=100, y=190, width=750, height=400)
        self.scroll_y = Scrollbar(self.f9, orient=VERTICAL)
        self.storageTree = ttk.Treeview(self.f9, yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.storageTree.yview)
        self.storageTree['columns'] = ('Date', 'Name', 'Kind', 'Color', 'Weight', 'Cost', 'Total')
        self.storageTree.column('#0', width=0, stretch=NO)
        self.storageTree.column('Date', width=50, minwidth=40, anchor=W)
        self.storageTree.column('Name', width=110, minwidth=80, anchor='center')
        self.storageTree.column('Kind', width=120, minwidth=50, anchor='center')
        self.storageTree.column('Color', width=60, minwidth=40, anchor='center')
        self.storageTree.column('Weight', width=50, minwidth=20, anchor='center')
        self.storageTree.column('Cost', width=40, minwidth=20, anchor='center')
        self.storageTree.column('Total', width=90, minwidth=70, anchor='center')

        self.storageTree.heading('#0', text='', anchor=W)
        self.storageTree.heading('Date', text='التاريخ', anchor=W)
        self.storageTree.heading('Name', text='اسم العملاء', anchor='center')
        self.storageTree.heading('Kind', text='الصنف', anchor='center')
        self.storageTree.heading('Color', text='اللون', anchor='center')
        self.storageTree.heading('Weight', text='الوزن', anchor='center')
        self.storageTree.heading('Cost', text='السعر', anchor='center')
        self.storageTree.heading('Total', text='الإجمالي', anchor='center')
        self.storageTree.pack(fill=BOTH, expand=1)

        rec_deal = client_ftch()

        self.storageTree.tag_configure('oddrow', background='white')
        self.storageTree.tag_configure('evenrow', background='skyblue')
        no = 0
        for record in rec_deal:
            if no % 2 == 0:
                self.storageTree.insert(parent='', index='end', iid=no, text='',
                                        values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
                                        tags=('evenrow',))
            else:
                self.storageTree.insert(parent='', index='end', iid=no, text='',
                                        values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]),
                                        tags=('oddrow',))
            no += 1

    def reviews_check(self):
        self.f9 = Frame(self, bg='#FFF')
        self.f9.place(x=100, y=190, width=750, height=400)
        self.scroll_y = Scrollbar(self.f9, orient=VERTICAL)
        self.storageTree = ttk.Treeview(self.f9, yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.storageTree.yview)
        self.storageTree['columns'] = ('Bank', 'Owner', 'From', 'To', 'Payment', 'Date')
        self.storageTree.column('#0', width=0, stretch=NO)
        self.storageTree.column('Bank', width=50, minwidth=40, anchor='center')
        self.storageTree.column('Owner', width=100, minwidth=40, anchor='center')
        self.storageTree.column('From', width=100, minwidth=30, anchor='center')
        self.storageTree.column('To', width=100, minwidth=50, anchor='center')
        self.storageTree.column('Payment', width=60, minwidth=50, anchor='center')
        self.storageTree.column('Date', width=50, minwidth=30, anchor=W)

        self.storageTree.heading('#0', text='', anchor=W)
        self.storageTree.heading('Bank', text='بـنـك', anchor='center')
        self.storageTree.heading('Owner', text='صاحب الشيك', anchor='center')
        self.storageTree.heading('From', text='إلــي', anchor='center')
        self.storageTree.heading('To', text='مــن', anchor='center')
        self.storageTree.heading('Payment', text='مـبـلـغ', anchor='center')
        self.storageTree.heading('Date', text='الـنـاريـخ', anchor=W)
        self.storageTree.pack(fill=BOTH, expand=1)

        recordy = check_ftch()

        self.storageTree.tag_configure('oddrow', background='white')
        self.storageTree.tag_configure('evenrow', background='skyblue')
        row_no = 0
        for record in recordy:
            if row_no % 2 == 0:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[5], record[4], record[3], record[2], record[1], record[0]),
                                        tags=('evenrow',))
            else:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[5], record[4], record[3], record[2], record[1], record[0]),
                                        tags=('oddrow',))
            row_no += 1
