from pathlib import Path
import datetime
from tkinter import (
    Label, Entry,
    Button, messagebox,
    IntVar, StringVar,
    Toplevel, ttk)


from fucs import check_owner_ftch, check_delete

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


class DelCheck(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.title('مــســح شــيــك')
        self.geometry('400x300+490+260')
        self.resizable(False, False)
        self.configure(bg='#5E95FF')
        self.date = datetime.datetime.now().date()
        # ============= Var ======== #
        self.owner_name = StringVar()
        owners_ftch = check_owner_ftch()

        Label(self, text='ادخل اسم صاحب الشيك', fg='#FFF', font=('Tajawal', 14, 'bold'),
              bg='#5E95FF').place(x=90, y=30)

        self.en_owner = ttk.Combobox(self, font=('Cairo', 12), justify='center', state='readonly',
                                    values=owners_ftch, textvariable=self.owner_name)
        self.en_owner.place(x=105, y=80, width=200, height=25)

        Label(self, font=('Tajawal', 10), fg='#5E95FF', bg='#FFF', text='حدد التاريخ').place(x=170, y=120)

        self.en_date = Entry(self, font=('Tajawal', 13), justify='center', bd=1, background='#f0f0f4')
        self.en_date.insert(0, str(self.date))
        self.en_date.place(x=130, y=190, width=150, height=25)

        self.del_s1 = Button(self, text='مـسـح الـشـيـك', fg='#5E95FF', font=('arial', 12, 'bold'),
                             width=9, height=1, highlightbackground='#FFF', command=self.submit)
        self.del_s1.place(x=160, y=230)

    def submit(self):
        try:
            str(self.owner_name.get())
        except:
            messagebox.showerror(
                "Error", "خطأ، بعض البيانات التي قمت بأدخالها غير صحيحة\nتأكد ان الارقام مكتوبه بالانجليزية")
        else:
            op = messagebox.askyesno("Save Data", "هـل انـت مـتـأكـد انـك تـرغـب بمسح هذا الشيك ؟")
            if op > 0:
                check_delete(name=self.owner_name.get(), date=self.en_date.get())
                messagebox.showinfo("Saved", "تـم مـسـح الـشـيـك بـنـحـاح")
                self.destroy()
