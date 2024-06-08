from pathlib import Path

from tkinter import (
    Label, Entry,
    Button, messagebox,
    IntVar, StringVar,
    Toplevel)


from fucs import mater_pro

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


class AddDealer(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.title('إضافة مورد جديد')
        self.geometry('400x300+490+260')
        self.resizable(False, False)
        self.configure(bg='#5E95FF')

        # ============= Var ======== #
        self.d_name = StringVar()
        self.d_money = IntVar()

        Label(self, text='ادخل اسم المورد / الشركة', fg='#FFF', font=('Tajawal', 14, 'bold'),
              bg='#5E95FF').place(x=90, y=30)

        self.del_name = Entry(self, font=('Tajawal', 13), justify='right', bd=1, textvariable=self.d_name)
        self.del_name.place(x=105, y=80, width=200, height=25)

        Label(self, font=('Tajawal', 10), fg='#5E95FF', bg='#FFF',
              text='اذا ترغب بفتح الحساب بقيمة فلوس متبقيه عليه').place(x=70, y=120)
        Label(self, font=('Tajawal', 10), fg='#5E95FF', bg='#FFF',
              text='ادخلها في المربع التالي').place(x=145, y=150)

        self.del_money = Entry(self, font=('Tajawal', 13), justify='center', bd=1, textvariable=self.d_money)
        self.del_money.place(x=130, y=190, width=150, height=25)

        self.reg_s1 = Button(self, text='إضافة المورد', fg='#5E95FF', font=('arial', 12, 'bold'),
                             width=9, height=1, highlightbackground='#FFF', command=self.submit)
        self.reg_s1.place(x=160, y=230)

    def submit(self):
        try:
            int(self.d_money.get())
        except:
            messagebox.showerror(
                "Error", "خطأ، بعض البيانات التي قمت بأدخالها غير صحيحة\nتأكد ان الارقام مكتوبه بالانجليزية")
        else:
            op = messagebox.askyesno("Save Data", "هـل انـت مـتـأكـد انـك تـرغـب بإضافة مورد جديد ؟")
            if op > 0:
                mater_pro(name_1=self.d_name.get(), total=self.d_money.get())
                messagebox.showinfo("Saved", "تـم إضـافـة الـمـورد بـنـحـاح")
                self.destroy()
