import datetime
from pathlib import Path
from tkinter import (
    Label, Entry, Button,
    messagebox, IntVar, StringVar,
    ttk, Toplevel)
from fucs import guests_ftchs, client_rets_f, guests_client_pay, client_upd_rt, guests_dealer_deleted, client_upd_del

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


class AddPayment(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.title('إضافة / مسح دفعة سداد')
        self.geometry('400x300+370+250')
        self.resizable(False, False)
        self.configure(bg='#F38181')
        self.date = datetime.datetime.now().date()
        # ============= Var ======== #
        self.d_name = StringVar()
        self.d_money = IntVar()
        self.restn = IntVar()
        self.name_vlu = guests_ftchs()

        Label(self, text='اختار اسم العميل', fg='#FFF', font=('Tajawal', 14, 'bold'),
              bg='#F38181').place(x=120, y=20)

        self.en_name = ttk.Combobox(self, font=('Cairo', 11), justify='center', state='readonly',
                                    values=self.name_vlu, textvariable=self.d_name)
        self.en_name.place(x=105, y=60, width=200, height=25)
        Label(self, text='مـتـبـقـي عليه', font=('Tajawal', 11), fg='#FFF', bg='#F38181').place(x=170, y=100)
        Label(self, font=('Tajawal', 14), fg='black', bg='#F38181', textvariable=self.restn).place(x=175, y=115)
        self.d_name.trace_add("write", self.restin)

        self.del_money = Entry(self, font=('Tajawal', 13), justify='center', bd=1, textvariable=self.d_money)
        self.del_money.place(x=150, y=150, width=100, height=25)

        self.en_date = Entry(self, font=('Tajawal', 13), justify='center', bd=1, background='#f0f0f4')
        self.en_date.insert(0, str(self.date))
        self.en_date.place(x=150, y=190, width=100, height=25)

        self.reg_s1 = Button(self, text='تسجيل الدفعة', fg='#F38181', font=('arial', 12, 'bold'),
                             width=9, height=1, highlightbackground='#FFF', command=self.submit)
        self.reg_s1.place(x=220, y=235)

        self.reg_s2 = Button(self, text='مسح الدفعة', fg='#5E95FF', font=('arial', 12, 'bold'),
                             width=9, height=1, highlightbackground='#FFF', command=self.del_sup)
        self.reg_s2.place(x=91, y=235)

    def restin(self, *args):
        self.restn.set(client_rets_f(name_1=self.d_name.get()))

    def del_sup(self):
        try:
            int(self.d_money.get())
        except:
            messagebox.showerror(
                "Error", "خطأ، بعض البيانات التي قمت بأدخالها غير صحيحة\nتأكد ان الارقام مكتوبه بالانجليزية")
        else:
            op = messagebox.askyesno("Save Data", "هـل انـت مـتـأكـد انـك تـرغـب بمسح دفعة سداد ؟")
            if op > 0:
                guests_dealer_deleted(name=self.d_name.get(), pay=self.d_money.get(), date=self.en_date.get())
                client_upd_del(name_1=self.d_name.get(), pay=self.d_money.get())
                messagebox.showinfo("Saved", "تـم مــســح الدفعة بـنـجـاح")
                self.destroy()

    def submit(self):
        try:
            int(self.d_money.get())
        except:
            messagebox.showerror(
                "Error", "خطأ، بعض البيانات التي قمت بأدخالها غير صحيحة\nتأكد ان الارقام مكتوبه بالانجليزية")
        else:
            op = messagebox.askyesno("Save Data", "هـل انـت مـتـأكـد انـك تـرغـب بتسحيل دفعة سداد ؟")
            if op > 0:
                guests_client_pay(name_1=self.d_name.get(), payment=self.d_money.get(), date=self.date)
                client_upd_rt(name_1=self.d_name.get(), pay=self.d_money.get())
                messagebox.showinfo("Saved", "تـم إضـافـة الدفعة بـنـجـاح")
                self.destroy()
