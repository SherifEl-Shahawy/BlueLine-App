from pathlib import Path

from tkinter import (
    Label,
    Button, Frame, Scrollbar,
    IntVar, StringVar, VERTICAL,
    ttk, Toplevel,
    RIGHT, BOTH, NO, Y, W)

from fucs import fix_ftch, var_ftch

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


class TotalExpenses(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.title('إجـمـالـي الـمـصـاريـف')
        self.geometry('900x650+130+45')
        self.resizable(False, False)
        self.configure(bg='#393e47')
        self.storageTree = None
        self.scroll_y = None
        self.f9 = None

        # ============= Var ======== #
        self.month_n = StringVar()
        self.m_vlu = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
        self.f_data = {'elect': IntVar(), 'clor': IntVar(), 'gaz': IntVar(), 'salt': IntVar(), 'mshal': IntVar(),
                       'kyas': IntVar(), 'lazk': IntVar(), 'khet': IntVar(), 'mkink': IntVar(), 'etc': IntVar()}
        self.totals = {'f_t': IntVar(), 'v_t': IntVar(), 'full': IntVar()}

        Label(self, text='حـدد الـشـهـر', fg='#5E95FF', font=('Tajawal', 12, 'bold'),
              bg='#393e47').place(x=670, y=30)

        self.en_month = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                                     values=self.m_vlu, textvariable=self.month_n)
        self.en_month.place(x=415, y=40, width=150, height=25)

        self.ser_s1 = Button(self, text='بدء البحث', fg='#5E95FF', font=('arial', 12, 'bold'),
                             width=11, height=1, highlightbackground='#FFF', command=self.search_btn)
        self.ser_s1.place(x=200, y=35)

        Label(self, text='الـمـصاريـف الـمتـغيـرة', fg='#5E95FF', font=('Tajawal', 12, 'bold'),
              bg='#393e47').place(x=90, y=115)
        Label(self, text='الـمـصاريـف الـثـابـتـة', fg='#5E95FF', font=('Tajawal', 12, 'bold'),
              bg='#393e47').place(x=410, y=115)
        Label(self, text='إجـمـالـي مـصـاريـف الـشـهر', fg='#5E95FF', font=('Tajawal', 12, 'bold'),
              bg='#393e47').place(x=690, y=115)
        self.label_txt('الـكـهـربـاء', x=700, y=170), self.label_txt('الـكـلـور', x=700, y=200)
        self.label_txt('الـجـاز', x=700, y=230), self.label_txt('الـمـلـح', x=700, y=260)
        self.label_txt('الـمـشـالات', x=700, y=290), self.label_txt('اكـيـاس', x=700, y=320)
        self.label_txt('لــذق', x=700, y=350), self.label_txt('خـيـط', x=700, y=380)
        self.label_txt('الـمـيكانـيكي', x=700, y=410), self.label_txt('نـثـريـات', x=700, y=440)
        self.label_txt('اجمالـي الثابت', x=700, y=540), self.label_txt('اجمالـي المتغير', x=700, y=580)
        self.label_txt('الاجمالي', x=700, y=620)
        Label(self, font=('Tajawal', 14), fg='#FFF', bg='#393e47', textvariable=self.f_data['elect']).place(x=810,
                                                                                                            y=170)
        Label(self, font=('Tajawal', 14), fg='#FFF', bg='#393e47', textvariable=self.f_data['clor']).place(x=810, y=200)
        Label(self, font=('Tajawal', 14), fg='#FFF', bg='#393e47', textvariable=self.f_data['gaz']).place(x=810, y=230)
        Label(self, font=('Tajawal', 14), fg='#FFF', bg='#393e47', textvariable=self.f_data['salt']).place(x=810, y=260)
        Label(self, font=('Tajawal', 14), fg='#FFF', bg='#393e47', textvariable=self.f_data['mshal']).place(x=810,
                                                                                                            y=290)
        Label(self, font=('Tajawal', 14), fg='#FFF', bg='#393e47', textvariable=self.f_data['kyas']).place(x=810, y=320)
        Label(self, font=('Tajawal', 14), fg='#FFF', bg='#393e47', textvariable=self.f_data['lazk']).place(x=810, y=350)
        Label(self, font=('Tajawal', 14), fg='#FFF', bg='#393e47', textvariable=self.f_data['khet']).place(x=810, y=380)
        Label(self, font=('Tajawal', 14), fg='#FFF', bg='#393e47', textvariable=self.f_data['mkink']).place(x=810,
                                                                                                            y=410)
        Label(self, font=('Tajawal', 14), fg='#FFF', bg='#393e47', textvariable=self.f_data['etc']).place(x=810, y=440)
        Label(self, font=('Tajawal', 14), fg='#FFF', bg='#393e47', textvariable=self.totals['f_t']).place(x=810, y=540)
        Label(self, font=('Tajawal', 14), fg='#FFF', bg='#393e47', textvariable=self.totals['v_t']).place(x=810, y=580)
        Label(self, font=('Tajawal', 14), fg='#FFF', bg='#393e47', textvariable=self.totals['full']).place(x=810, y=620)

        self.rec_fix = fix_ftch(self.month_n.get())
        self.rec_var = var_ftch(self.month_n.get())
        self.fixed()
        self.vars()

    def label_txt(self, txt, x, y):
        Label(self, font=('Tajawal', 12), fg='#5E95FF', bg='#393e47', text=txt).place(x=x, y=y)

    def fixed(self, *args):
        self.f9 = Frame(self, bg='#FFF')
        self.f9.place(x=340, y=160, width=300, height=430)
        self.scroll_y = Scrollbar(self.f9, orient=VERTICAL)
        self.storageTree = ttk.Treeview(self.f9, yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.storageTree.yview)
        self.storageTree['columns'] = ('Date', 'Opera', 'Amount')
        self.storageTree.column('#0', width=0, stretch=NO)
        self.storageTree.column('Date', width=60, minwidth=40, anchor=W)
        self.storageTree.column('Opera', width=80, minwidth=50, anchor='center')
        self.storageTree.column('Amount', width=40, minwidth=20, anchor='center')

        self.storageTree.heading('#0', text='', anchor=W)
        self.storageTree.heading('Date', text='التاريخ', anchor=W)
        self.storageTree.heading('Opera', text='اسـم الـعـملـية', anchor='center')
        self.storageTree.heading('Amount', text='الـمـدفـوع', anchor='center')

        self.storageTree.pack(fill=BOTH, expand=1)

        self.storageTree.tag_configure('oddrow', background='white')
        self.storageTree.tag_configure('evenrow', background='skyblue')
        row_no = 0
        for record in self.rec_fix:
            if row_no % 2 == 0:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[0], record[1], record[2]),
                                        tags=('evenrow',))
            else:
                self.storageTree.insert(parent='', index='end', iid=row_no, text='',
                                        values=(record[0], record[1], record[2]),
                                        tags=('oddrow',))
            row_no += 1

    def vars(self, *args):
        self.f9 = Frame(self, bg='#FFF')
        self.f9.place(x=20, y=160, width=300, height=430)
        self.scroll_y = Scrollbar(self.f9, orient=VERTICAL)
        self.storageTree = ttk.Treeview(self.f9, yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_y.config(command=self.storageTree.yview)
        self.storageTree['columns'] = ('Date', 'Opera', 'Amount')
        self.storageTree.column('#0', width=0, stretch=NO)
        self.storageTree.column('Date', width=60, minwidth=40, anchor=W)
        self.storageTree.column('Opera', width=80, minwidth=50, anchor='center')
        self.storageTree.column('Amount', width=40, minwidth=20, anchor='center')

        self.storageTree.heading('#0', text='', anchor=W)
        self.storageTree.heading('Date', text='التاريخ', anchor=W)
        self.storageTree.heading('Opera', text='اسـم الـعـملـية', anchor='center')
        self.storageTree.heading('Amount', text='الـمـدفـوع', anchor='center')

        self.storageTree.pack(fill=BOTH, expand=1)

        self.storageTree.tag_configure('oddrow', background='white')
        self.storageTree.tag_configure('evenrow', background='skyblue')
        row_no = 0
        for record in self.rec_var:
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
        self.rec_fix = fix_ftch(self.month_n.get())
        self.rec_var = var_ftch(self.month_n.get())
        self.fixed()
        self.vars()
        elc, clo, gz, slt = 0, 0, 0, 0
        mshl, kesa, lzg, khet, nacr, mknk = 0, 0, 0, 0, 0, 0
        f_total, v_total = 0, 0
        for item in self.rec_fix:
            f_total += item[2]
            if item[1] == 'كـهـربـاء':
                elc += item[2]
                self.f_data['elect'].set(elc)
            elif item[1] == 'كـلـور':
                clo += item[2]
                self.f_data['clor'].set(clo)
            elif item[1] == 'جــاز':
                gz += item[2]
                self.f_data['gaz'].set(gz)
            elif item[1] == 'مـلـح':
                slt += item[2]
                self.f_data['salt'].set(slt)
        for item in self.rec_var:
            v_total += item[2]
            if item[1] == 'مـشـالات':
                mshl += item[2]
                self.f_data['mshal'].set(mshl)
            elif item[1] == 'اكـيـاس':
                kesa += item[2]
                self.f_data['kyas'].set(kesa)
            elif item[1] == 'لــذق':
                lzg += item[2]
                self.f_data['lazk'].set(lzg)
            elif item[1] == 'خـيـط':
                khet += item[2]
                self.f_data['khet'].set(khet)
            elif item[1] == 'نـثـريـات':
                nacr += item[2]
                self.f_data['etc'].set(nacr)
            elif item[1] == 'مـيـكـانـيـكي':
                mknk += item[2]
                self.f_data['mkink'].set(mknk)
        self.totals['f_t'].set(f_total)
        self.totals['v_t'].set(v_total)
        self.totals['full'].set(f_total + v_total)
