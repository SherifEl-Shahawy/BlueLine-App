from pathlib import Path
from tkinter import (
    Frame, Label, Button,
    IntVar, StringVar, ttk,
    Toplevel, Scrollbar, VERTICAL,
    RIGHT, Y, W, NO, BOTH)

from fucs import guests_ftchs, client_rets_f, client_ftch, guests_pay_ftchs

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


class Review(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.storageTree = None
        self.scroll_y = None
        self.f9 = None
        self.title('عرض تعاملات عميل')
        self.geometry('800x600+90+60')
        self.resizable(False, False)
        self.configure(bg='#F38181')
        # ============= Var ======== #
        self.d_name = StringVar()
        self.d_money = IntVar()
        self.restn = IntVar()
        self.name_vlu = guests_ftchs()

        Label(self, text='اختار اسم المورد', fg='#FFF', font=('Tajawal', 14, 'bold'),
              bg='#F38181').place(x=570, y=30)

        self.en_name = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                                    values=self.name_vlu, textvariable=self.d_name)
        self.en_name.place(x=290, y=40, width=200, height=25)

        Label(self, text='مـتـبـقـي عـلـيـه', font=('Tajawal', 13), fg='#FFF', bg='#F38181').place(x=150, y=550)
        Label(self, font=('Tajawal', 14), fg='#FFF', bg='#F38181', textvariable=self.restn).place(x=40, y=550)
        self.d_name.trace_add("write", self.restin)

        self.ser_s1 = Button(self, text='بدء البحث', fg='#F38181', font=('arial', 12, 'bold'),
                             width=9, height=1, highlightbackground='#FFF', command=self.search_btn)
        self.ser_s1.place(x=100, y=35)
        self.clients()
        self.client_payment()

    def clients(self, *args):  # TODO : Need Fix Fetchs Data
        self.f9 = Frame(self, bg='#FFF')
        self.f9.place(x=295, y=90, width=485, height=450)
        self.scroll_y = Scrollbar(self.f9, orient=VERTICAL)
        self.storageTree = ttk.Treeview(self.f9, yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.storageTree.yview)
        self.storageTree['columns'] = ('Date', 'Prod', 'Color', 'Weight', 'Price', 'Total')
        self.storageTree.column('#0', width=0, stretch=NO)
        self.storageTree.column('Date', width=50, minwidth=40, anchor=W)
        self.storageTree.column('Prod', width=40, minwidth=30, anchor='center')
        self.storageTree.column('Color', width=40, minwidth=30, anchor='center')
        self.storageTree.column('Weight', width=40, minwidth=20, anchor='center')
        self.storageTree.column('Price', width=40, minwidth=20, anchor='center')
        self.storageTree.column('Total', width=50, minwidth=30, anchor='center')

        self.storageTree.heading('#0', text='', anchor=W)
        self.storageTree.heading('Date', text='التاريخ', anchor=W)
        self.storageTree.heading('Prod', text='الصنف', anchor='center')
        self.storageTree.heading('Color', text='اللون', anchor='center')
        self.storageTree.heading('Weight', text='الوزن', anchor='center')
        self.storageTree.heading('Price', text='السعر', anchor='center')
        self.storageTree.heading('Total', text='الإجمالي', anchor='center')
        self.storageTree.pack(fill=BOTH, expand=1)

        rec_client = client_ftch(self.d_name.get())

        self.storageTree.tag_configure('oddrow', background='white')
        self.storageTree.tag_configure('evenrow', background='#F38181')
        row_no = 0
        for record in rec_client:
            if row_no % 2 == 0:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                                        tags=('evenrow',))
            else:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[0], record[1], record[2], record[3], record[4], record[5]),
                                        tags=('oddrow',))
            row_no += 1

    def client_payment(self, *args):
        self.f9 = Frame(self, bg='#FFF')
        self.f9.place(x=20, y=90, width=240, height=450)
        self.scroll_y = Scrollbar(self.f9, orient=VERTICAL)
        self.storageTree = ttk.Treeview(self.f9, yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.storageTree.yview)
        self.storageTree['columns'] = ('Date', 'Kind')
        self.storageTree.column('#0', width=0, stretch=NO)
        self.storageTree.column('Date', width=80, minwidth=40, anchor=W)
        self.storageTree.column('Kind', width=80, minwidth=40, anchor='center')

        self.storageTree.heading('#0', text='', anchor=W)
        self.storageTree.heading('Date', text='التاريخ', anchor=W)
        self.storageTree.heading('Kind', text='الـدفـعـة', anchor='center')

        self.storageTree.pack(fill=BOTH, expand=1)

        rec_client = guests_pay_ftchs(self.d_name.get())

        self.storageTree.tag_configure('oddrow', background='white')
        self.storageTree.tag_configure('evenrow', background='skyblue')
        row_no = 0
        for record in rec_client:
            if row_no % 2 == 0:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[0], record[1]),
                                        tags=('evenrow',))
            else:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[0], record[1]),
                                        tags=('oddrow',))
            row_no += 1

    def restin(self, *args):
        self.restn.set(client_rets_f(name_1=self.d_name.get()))

    def search_btn(self):
        self.clients()
        self.client_payment()
