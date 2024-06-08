from pathlib import Path
import datetime

from tkinter import (
    Label, Entry, ttk,
    Button, messagebox, StringVar,
    Toplevel, LabelFrame)


from fucs import guests_ftchs, guests_pro_del, guests_store_del


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


class EditDel(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.title('التعديلات')
        self.geometry('400x550+390+50')
        self.resizable(False, False)
        self.configure(bg='#F38181')
        self.date = datetime.datetime.now().date()
        # ============= Var ======== #
        self.ccname = StringVar()
        self.ccname_1 = StringVar()
        self.kinds = StringVar()
        name_vlu = guests_ftchs()
        
        
        
        f1 = LabelFrame(self, text='مـسـح الـعـمـيـل', font=('Tajawal', 17, 'bold'), bd=10, fg='#FFF', bg='#F38181',
                        labelanchor='n')
        f1.place(x=10, y=30, width=380, height=200)
        self.label_txt(pc=f1, txt='اسم الـعـمـيـل', x=230, y=20)
        self.label_txt(pc=f1, txt='تحذير : سيتم مسح هذا الـعـمـيـل نهائياً من البرنامج', x=15, y=65)
        
        self.en_kind = ttk.Combobox(f1, font=('Cairo', 12), justify='center', state='readonly',
                                    values=name_vlu, textvariable=self.ccname)
        self.en_kind.place(x=40, y=20, width=150, height=25)
        
        self.reg_s1 = Button(self, text='مـسـح الـعـمـيـل', fg='#5E95FF', font=('arial', 12, 'bold'),
                             width=18, height=1, highlightbackground='#FFF', command=self.submit)
        self.reg_s1.place(x=105, y=175)
        
        f2 = LabelFrame(self, text='مـسـح عـمـلـيـه مـسـجـلـة', font=('Tajawal', 17, 'bold'), bd=10, fg='#FFF', bg='#F38181',
                        labelanchor='n')
        f2.place(x=10, y=260, width=380, height=250)
        self.label_txt(pc=f2, txt='اسم الـعـمـيـل', x=230, y=20)
        self.label_txt(pc=f2, txt='اختار الصنف', x=225, y=65)
        self.label_txt(pc=f2, txt='التاريخ', x=270, y=110)
        
        self.en_name = ttk.Combobox(f2, font=('Cairo', 12), justify='center', state='readonly',
                                    values=name_vlu, textvariable=self.ccname_1)
        self.en_name.place(x=40, y=20, width=150, height=25)

        self.en_kind = Entry(f2, font=('Cairo', 12), justify='center', bd=1, background='#f0f0f4',
                             textvariable=self.kinds)
        self.en_kind.place(x=40, y=65, width=150, height=25)
        
        self.en_date = Entry(f2, font=('Tajawal', 13), justify='center', bd=1, background='#f0f0f4')
        self.en_date.insert(0, str(self.date))
        self.en_date.place(x=40, y=110, width=150, height=25)
        
        self.reg_s2 = Button(f2, text='مـسـح الـعـمـلـية', fg='#5E95FF', font=('arial', 12, 'bold'),
                             width=18, height=1, highlightbackground='#FFF', command=self.submit_2)
        self.reg_s2.place(x=80, y=160)
        
    def submit(self):
        op = messagebox.askyesno("Save Data", "هـل انـت مـتـأكـد انـك تـرغـب بـمـسـح الـعـمـيـل ؟")
        if op > 0:
            guests_pro_del(name=self.ccname.get())
            messagebox.showinfo("Saved", "تـم مـسـح الـعـمـيـل بـنـجـاح")
            self.destroy()
            
    def submit_2(self):
        op = messagebox.askyesno("Save Data", "هـل انـت مـتـأكـد انـك تـرغـب بـمـسـح تـلـك الـعـمـلـيـة ؟")
        if op > 0:
            guests_store_del(name=self.ccname_1.get(), date=self.en_date.get(), prod=self.kinds.get())
            messagebox.showinfo("Saved", "تـم مـسـح الـعـمـلـيـة بـنـجـاح")
            self.destroy()
        
        
        
        
    def label_txt(self, pc, txt, x, y):
        Label(pc, font=('Tajawal', 12), fg='#FFF', bg='#F38181', text=txt).place(x=x, y=y)