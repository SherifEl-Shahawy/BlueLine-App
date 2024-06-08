import datetime
from pathlib import Path

from tkinter import (
    Frame, Label, Entry,
    LabelFrame, Button, messagebox,
    IntVar, StringVar, ttk)

from PIL import Image, ImageTk

from gui.main_window.expense.Exp_total.E_total import TotalExpenses
from gui.main_window.expense.Salary_total.S_total import Salary

from fucs import fix_store, var_store, salary_store

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def exp_fuc():
    Expenses()


class Expenses(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.configure(bg="#FFF")
        self.date = datetime.datetime.now().date()

        # ================variables================= #
        self.data_1 = {'fix_cost': IntVar(), 'var_cost': IntVar(), 'salary_cost': IntVar()}
        self.data_2 = {'fix_title': StringVar(), 'var_title': StringVar(), 'salary_title': StringVar()}
        fixed_vlu = ('كـلـور', 'كـهـربـاء', 'جــاز', 'مياه')
        var_vlu = ('مـشـالات', 'اكـيـاس', 'لــذق', 'خـيـط', 'نـثـريـات', 'مـيـكـانـيـكي')

        Label(self, text='ادارة الـمـصـاريـف', fg='#5E95FF', font=('Tajawal', 18, 'bold'), bg='#FFF').place(x=415, y=5)

        f1 = LabelFrame(self, text='مـصـاريـف ثـابـتـة', font=('Tajawal', 17, 'bold'), bd=10, fg='#5E95FF', bg='#FFF',
                        labelanchor='n')
        f1.place(x=550, y=70, width=360, height=260)

        self.label_txt('نـوع الـمـدفـوع', x=230, y=30, pl=f1)
        self.label_txt('الـقـيـمة', x=255, y=70, pl=f1)
        self.label_txt('الـتـاريـخ', x=255, y=110, pl=f1)

        self.en_kind = ttk.Combobox(f1, font=('Cairo', 12), justify='center', state='readonly',
                                    values=fixed_vlu, textvariable=self.data_2['fix_title'])
        self.en_kind.place(x=25, y=30, width=150, height=25)

        self.en_cost = Entry(f1, font=('Tajawal', 13), justify='center', bd=1, textvariable=self.data_1['fix_cost'],
                             background='#f0f0f4')
        self.en_cost.place(x=25, y=70, width=150, height=25)

        self.f_date = Entry(f1, font=('Tajawal', 13), justify='center', bd=1, background='#f0f0f4')
        self.f_date.insert(0, str(self.date))
        self.f_date.place(x=25, y=110, width=150, height=25)

        self.button_image_1 = ImageTk.PhotoImage(Image.open("exp_reg.png"))
        button_1 = Button(f1, image=self.button_image_1, borderwidth=0, highlightthickness=0,
                          relief="flat", cursor='hand2', command=self.fix_btn)
        button_1.place(x=67.0, y=160.0, width=190.0, height=48.0)

        f2 = LabelFrame(self, text='مـصـاريـف مـتـغـيـرة', font=('Tajawal', 17, 'bold'), bd=10, fg='#5E95FF', bg='#FFF',
                        labelanchor='n')
        f2.place(x=80, y=70, width=360, height=260)

        self.label_txt('اسـم الـعـمـلـية', x=230, y=30, pl=f2)
        self.label_txt('الـقـيـمة', x=255, y=70, pl=f2)
        self.label_txt('الـتـاريـخ', x=255, y=110, pl=f2)

        self.en_kind = ttk.Combobox(f2, font=('Cairo', 12), justify='center',
                                    values=var_vlu, textvariable=self.data_2['var_title'])
        self.en_kind.place(x=25, y=30, width=150, height=25)

        self.en_cost = Entry(f2, font=('Tajawal', 13), justify='center', bd=1, textvariable=self.data_1['var_cost'],
                             background='#f0f0f4')
        self.en_cost.place(x=25, y=70, width=150, height=25)

        self.v_date = Entry(f2, font=('Tajawal', 13), justify='center', bd=1, background='#f0f0f4')
        self.v_date.insert(0, str(self.date))
        self.v_date.place(x=25, y=110, width=150, height=25)

        self.button_image_2 = ImageTk.PhotoImage(Image.open("exp_reg.png"))
        button_2 = Button(f2, image=self.button_image_2, borderwidth=0, highlightthickness=0,
                          relief="flat", cursor='hand2', command=self.var_btn)
        button_2.place(x=67.0, y=160.0, width=190.0, height=48.0)

        f3 = LabelFrame(self, text='رواتـب الـعـمـال', font=('Tajawal', 17, 'bold'), bd=10, fg='#5E95FF', bg='#FFF',
                        labelanchor='n')
        f3.place(x=550, y=345, width=360, height=260)

        self.label_txt('اسـم الـعـامـل', x=230, y=30, pl=f3)
        self.label_txt('الـقـيـمة', x=255, y=70, pl=f3)
        self.label_txt('الـتـاريـخ', x=255, y=110, pl=f3)

        self.en_worker = Entry(f3, font=('Tajawal', 13), justify='center', bd=1,
                               textvariable=self.data_2['salary_title'], background='#f0f0f4')
        self.en_worker.place(x=25, y=30, width=150, height=25)

        self.en_cost = Entry(f3, font=('Tajawal', 13), justify='center', bd=1, textvariable=self.data_1['salary_cost'],
                             background='#f0f0f4')
        self.en_cost.place(x=25, y=70, width=150, height=25)

        self.s_date = Entry(f3, font=('Tajawal', 13), justify='center', bd=1, background='#f0f0f4')
        self.s_date.insert(0, str(self.date))
        self.s_date.place(x=25, y=110, width=150, height=25)

        self.button_image_3 = ImageTk.PhotoImage(Image.open("exp_reg.png"))
        button_3 = Button(f3, image=self.button_image_3, borderwidth=0, highlightthickness=0,
                          relief="flat", cursor='hand2', command=self.salary_btn)
        button_3.place(x=67.0, y=160.0, width=190.0, height=48.0)

        f4 = LabelFrame(self, text='الـحـسـابـات', font=('Tajawal', 17, 'bold'), bd=10, fg='#5E95FF', bg='#FFF',
                        labelanchor='n')
        f4.place(x=80, y=380, width=360, height=200)

        self.button_image_4 = ImageTk.PhotoImage(Image.open("total_exp.png"))
        button_4 = Button(f4, image=self.button_image_4, borderwidth=0, highlightthickness=0,
                          relief="flat", cursor='hand2', command=TotalExpenses)
        button_4.place(x=67.0, y=20.0, width=190.0, height=48.0)

        self.button_image_5 = ImageTk.PhotoImage(Image.open("salary_exp.png"))
        button_5 = Button(f4, image=self.button_image_5, borderwidth=0, highlightthickness=0,
                          relief="flat", cursor='hand2', command=Salary)
        button_5.place(x=67.0, y=90.0, width=190.0, height=48.0)

    def label_txt(self, txt, x, y, pl):
        Label(pl, font=('Tajawal', 12), fg='#5E95FF', bg='#FFF', text=txt).place(x=x, y=y)

    def fix_btn(self):
        try:
            int(self.data_1['fix_cost'].get())
        except:
            messagebox.showerror(
                "Error", "خطأ، بعض البيانات التي قمت بأدخالها غير صحيحة\nتأكد ان الارقام مكتوبه بالانجليزية")
        else:
            op = messagebox.askyesno("Save Data", "هـل انـت مـتـأكـد انـك تـرغـب بـتـخـزيـن تلـك البـيانات ؟")
            if op > 0:
                fix_store(date_1=self.f_date.get(), title=self.data_2['fix_title'].get(),
                          amount=self.data_1['fix_cost'].get())

    def var_btn(self):
        try:
            int(self.data_1['var_cost'].get())
        except:
            messagebox.showerror(
                "Error", "خطأ، بعض البيانات التي قمت بأدخالها غير صحيحة\nتأكد ان الارقام مكتوبه بالانجليزية")
        else:
            op = messagebox.askyesno("Save Data", "هـل انـت مـتـأكـد انـك تـرغـب بـتـخـزيـن تلـك البـيانات ؟")
            if op > 0:
                var_store(date_2=self.v_date.get(), title=self.data_2['var_title'].get(),
                          amount=self.data_1['var_cost'].get())

    def salary_btn(self):
        try:
            int(self.data_1['salary_cost'].get())
        except:
            messagebox.showerror(
                "Error", "خطأ، بعض البيانات التي قمت بأدخالها غير صحيحة\nتأكد ان الارقام مكتوبه بالانجليزية")
        else:
            op = messagebox.askyesno("Save Data", "هـل انـت مـتـأكـد انـك تـرغـب بـتـخـزيـن تلـك البـيانات ؟")
            if op > 0:
                salary_store(date_3=self.s_date.get(), name=self.data_2['salary_title'].get(),
                             amount=self.data_1['salary_cost'].get())
