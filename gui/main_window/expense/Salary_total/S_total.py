from pathlib import Path
from tkinter import (
    Label,
    Button, Frame, Scrollbar,
    IntVar, StringVar, VERTICAL,
    ttk, Toplevel,
    RIGHT, BOTH, NO, Y, W)

from fucs import salary_ftch

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


class Salary(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.title('إجـمـالـي الـرواتــب')
        self.geometry('460x650+130+45')
        self.resizable(False, False)
        self.configure(bg='#393e47')
        self.storageTree = None
        self.scroll_y = None
        self.f9 = None
        # ============= Var ======== #
        self.month_n = StringVar()
        self.m_vlu = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
        self.totalz = IntVar()

        Label(self, text='حـدد الـشـهـر', fg='#5E95FF', font=('Tajawal', 12, 'bold'),
              bg='#393e47').place(x=320, y=40)

        self.en_month = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                                     values=self.m_vlu, textvariable=self.month_n)
        self.en_month.place(x=200, y=40, width=50, height=25)

        self.ser_s1 = Button(self, text='بدء البحث', fg='#5E95FF', font=('arial', 12, 'bold'),
                             width=9, height=1, highlightbackground='#FFF', command=self.search_btn)
        self.ser_s1.place(x=30, y=35)

        Label(self, text='رواتــب الـعـمـال', fg='#5E95FF', font=('Tajawal', 12, 'bold'),
              bg='#393e47').place(x=170, y=110)
        Label(self, text='إجـمـالـي رواتـب  الـشـهـر', fg='#5E95FF', font=('Tajawal', 12, 'bold'),
              bg='#393e47').place(x=230, y=600)

        Label(self, font=('Tajawal', 12), fg='#FFF', bg='#393e47', textvariable=self.totalz).place(x=100, y=600)

        self.rec_sly = salary_ftch(self.month_n.get())
        self.salary()

    def label_txt(self, txt, x, y):
        Label(self, font=('Tajawal', 12), fg='#5E95FF', bg='#FFF', text=txt).place(x=x, y=y)

    def salary(self, *args):
        self.f9 = Frame(self, bg='#FFF')
        self.f9.place(x=30, y=140, width=400, height=430)
        self.scroll_y = Scrollbar(self.f9, orient=VERTICAL)
        self.storageTree = ttk.Treeview(self.f9, yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.storageTree.yview)
        self.storageTree['columns'] = ('Date', 'name', 'Amount')
        self.storageTree.column('#0', width=0, stretch=NO)
        self.storageTree.column('Date', width=60, minwidth=40, anchor=W)
        self.storageTree.column('name', width=80, minwidth=50, anchor='center')
        self.storageTree.column('Amount', width=40, minwidth=20, anchor='center')

        self.storageTree.heading('#0', text='', anchor=W)
        self.storageTree.heading('Date', text='التاريخ', anchor=W)
        self.storageTree.heading('name', text='اسـم الـعـامـل', anchor='center')
        self.storageTree.heading('Amount', text='الـمـدفـوع', anchor='center')

        self.storageTree.pack(fill=BOTH, expand=1)

        self.storageTree.tag_configure('oddrow', background='white')
        self.storageTree.tag_configure('evenrow', background='skyblue')
        row_no = 0
        for record in self.rec_sly:
            if row_no % 2 == 0:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[0], record[1], record[2]),
                                        tags=('evenrow',))
            else:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[0], record[1], record[2]),
                                        tags=('oddrow',))
            row_no += 1

    def search_btn(self):
        self.rec_sly = salary_ftch(self.month_n.get())
        self.salary()
        t_salary = 0
        for item in self.rec_sly:
            t_salary += item[2]
        self.totalz.set(t_salary)
