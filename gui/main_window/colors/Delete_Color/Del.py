from pathlib import Path
from tkinter import (
    Label, Button,
    StringVar, ttk,
    Toplevel, messagebox)

from fucs import colors_ftchs, color_del

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


class Delete(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.title('مـسـح لــون')
        self.geometry('400x240+370+250')
        self.resizable(False, False)
        self.configure(bg='#F38181')
        # ============= Var ======== #
        self.col_name = StringVar()
        self.colors_vlu = colors_ftchs()

        Label(self, text='اختار اللون', fg='#FFF', font=('Tajawal', 14, 'bold'),
              bg='#F38181').place(x=160, y=30)

        self.en_name = ttk.Combobox(self, font=('Cairo', 11), justify='center', state='readonly',
                                    values=self.colors_vlu, textvariable=self.col_name)
        self.en_name.place(x=105, y=80, width=200, height=25)
        
        Label(self, text='تحذير سيتم مسح اللون نهائياً من السيستم', fg='#FFF', font=('Tajawal', 11, 'bold'),
              bg='#F38181').place(x=50, y=120)

        self.reg_s1 = Button(self, text='مـسـح اللـون', fg='#F38181', font=('arial', 12, 'bold'),
                             width=9, height=1, highlightbackground='#FFF', command=self.submit)
        self.reg_s1.place(x=151, y=170)

    def submit(self):
        try:
            pass
        except:
            messagebox.showerror(
                "Error", "خطأ، بعض البيانات التي قمت بأدخالها غير صحيحة\nتأكد ان الارقام مكتوبه بالانجليزية")
        else:
            op = messagebox.askyesno("Save Data", "هـل انـت مـتـأكـد انـك تـرغـب بمسح اللون ؟")
            if op > 0:
                color_del(name=self.col_name.get())
                messagebox.showinfo("Saved", "تـم مسح اللون بـنـجـاح")
                self.destroy()
