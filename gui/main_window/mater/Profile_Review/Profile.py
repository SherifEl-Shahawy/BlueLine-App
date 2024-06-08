from pathlib import Path

from tkinter import (
    Frame, Label, Button,
    IntVar, StringVar, ttk,
    Toplevel, Scrollbar, VERTICAL,
    RIGHT, Y, W, NO, BOTH)

from fucs import mater_ftchs, mater_rets_f, dealers_ftch, mater_pay_ftchs

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


class Review(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.storageTree = None
        self.scroll_y = None
        self.f9 = None
        self.title('عرض تعاملات مورد')
        self.geometry('800x600+90+60')
        self.resizable(False, False)
        self.configure(bg='#5E95FF')
        # ============= Var ======== #
        self.d_name = StringVar()
        self.d_money = IntVar()
        self.restn = IntVar()
        self.name_vlu = mater_ftchs()

        Label(self, text='اختار اسم المورد', fg='#FFF', font=('Tajawal', 14, 'bold'),
              bg='#5E95FF').place(x=570, y=30)

        self.en_name = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                                    values=self.name_vlu, textvariable=self.d_name)
        self.en_name.place(x=290, y=40, width=200, height=25)

        Label(self, text='مـتـبـقـي لــه', font=('Tajawal', 13), fg='#FFF', bg='#5E95FF').place(x=150, y=550)
        Label(self, font=('Tajawal', 14), fg='red', bg='#FFF', textvariable=self.restn).place(x=40, y=550)
        self.d_name.trace_add("write", self.restin)

        self.ser_s1 = Button(self, text='بدء البحث', fg='#5E95FF', font=('arial', 12, 'bold'),
                             width=9, height=1, highlightbackground='#FFF', command=self.search_btn)
        self.ser_s1.place(x=100, y=35)
        self.dealers()
        self.deal_payment()

    def dealers(self, *args):
        self.f9 = Frame(self, bg='#FFF')
        self.f9.place(x=295, y=90, width=485, height=450)
        self.scroll_y = Scrollbar(self.f9, orient=VERTICAL)
        self.storageTree = ttk.Treeview(self.f9, yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.storageTree.yview)
        self.storageTree['columns'] = ('Date', 'Kind', 'Quant', 'Cost', 'Total')
        self.storageTree.column('#0', width=0, stretch=NO)
        self.storageTree.column('Date', width=50, minwidth=40, anchor=W)
        self.storageTree.column('Kind', width=140, minwidth=50, anchor='center')
        self.storageTree.column('Quant', width=50, minwidth=20, anchor='center')
        self.storageTree.column('Cost', width=40, minwidth=20, anchor='center')
        self.storageTree.column('Total', width=90, minwidth=70, anchor='center')

        self.storageTree.heading('#0', text='', anchor=W)
        self.storageTree.heading('Date', text='التاريخ', anchor=W)
        self.storageTree.heading('Kind', text='الصنف', anchor='center')
        self.storageTree.heading('Quant', text='الكمية', anchor='center')
        self.storageTree.heading('Cost', text='السعر', anchor='center')
        self.storageTree.heading('Total', text='الإجمالي', anchor='center')
        self.storageTree.pack(fill=BOTH, expand=1)

        rec_deal = dealers_ftch(self.d_name.get())

        self.storageTree.tag_configure('oddrow', background='white')
        self.storageTree.tag_configure('evenrow', background='skyblue')
        row_no = 0
        for record in rec_deal:
            if row_no % 2 == 0:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[0], record[1], record[2], record[3], record[4]),
                                        tags=('evenrow',))
            else:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[0], record[1], record[2], record[3], record[4]),
                                        tags=('oddrow',))
            row_no += 1
            
    def deal_payment(self, *args):
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
        self.storageTree.heading('Kind', text='الدفـعـة', anchor='center')

        self.storageTree.pack(fill=BOTH, expand=1)

        rec_deal = mater_pay_ftchs(self.d_name.get())

        self.storageTree.tag_configure('oddrow', background='white')
        self.storageTree.tag_configure('evenrow', background='skyblue')
        row_no = 0
        for record in rec_deal:
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
        self.restn.set(mater_rets_f(name_1=self.d_name.get()))

    def search_btn(self):
        self.dealers()
        self.deal_payment()
