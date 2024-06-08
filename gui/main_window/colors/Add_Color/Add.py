from pathlib import Path

from tkinter import (
    Label, Entry,
    Button, messagebox,
    IntVar, StringVar, DoubleVar,
    Toplevel, ttk)

from fucs import kind_ftchs, rg_color_t, rg_color_1x, rg_color_2x, rg_color_3x, rg_color_4x, rg_color_5x, rg_color_6x, \
    rg_color_7x, rg_color_8x, rg_color_9x, rg_color_10x

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


class AddColor(Toplevel):
    def __init__(self, *args, **kwargs):
        Toplevel.__init__(self, *args, **kwargs)
        self.title('إضافة لون جديد')
        self.geometry('800x500+90+60')
        self.resizable(False, False)
        self.configure(bg='#FF2E63')

        # ============= Var ======== #
        self.col_name = StringVar()
        self.col_qun = IntVar()
        color_vlu = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
        self.material_vlu = kind_ftchs()
        self.rows = {'raw1': DoubleVar(), 'raw2': DoubleVar(), 'raw3': DoubleVar(), 'raw4': DoubleVar(),
                     'raw5': DoubleVar(), 'raw6': DoubleVar(), 'raw7': DoubleVar(),
                     'raw8': DoubleVar(), 'raw9': DoubleVar(), 'raw10': DoubleVar()}

        self.mts = {'mts1': StringVar(), 'mts2': StringVar(), 'mts3': StringVar(), 'mts4': StringVar(),
                    'mts5': StringVar(), 'mts6': StringVar(), 'mts7': StringVar(),
                    'mts8': StringVar(), 'mts9': StringVar(), 'mts10': StringVar()}

        Label(self, text='ادخل اسم اللـون', fg='#FFF', font=('Tajawal', 12, 'bold'),
              bg='#FF2E63').place(x=590, y=30)

        self.col_name = Entry(self, font=('Tajawal', 13), justify='right', bd=1, textvariable=self.col_name)
        self.col_name.place(x=400, y=30, width=100, height=25)

        Label(self, font=('Tajawal', 12, 'bold'), fg='#FFF', bg='#FF2E63', text='عـدد مـواده').place(x=240, y=30)

        Label(self, font=('Tajawal', 12, 'bold'), fg='#FFF', bg='#FF2E63', text='الـمـاده').place(x=540, y=80)
        Label(self, font=('Tajawal', 12, 'bold'), fg='#FFF', bg='#FF2E63', text='الـنـسـبـه').place(x=250, y=80)

        self.col_no = ttk.Combobox(self, font=('Cairo', 12), justify='center', state='readonly',
                                   values=color_vlu, textvariable=self.col_qun)
        self.col_no.place(x=120, y=30, width=50, height=25)
        self.col_qun.trace_add("write", self.rewi)

        self.reg_s1 = Button(self, text='إضافة اللون', fg='#FF2E63', font=('arial', 12, 'bold'),
                             width=9, height=1, highlightbackground='#FFF', command=self.submit)
        self.reg_s1.place(x=382, y=450)

    def row_1x(self):
        row1 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts1'])
        row1.place(x=525, y=130, width=100, height=25)

        perc_row1 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw1'])
        perc_row1.place(x=238, y=130, width=80, height=25)

    def row_2x(self):
        row1 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts1'])
        row1.place(x=525, y=130, width=100, height=25)

        perc_row1 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw1'])
        perc_row1.place(x=238, y=130, width=80, height=25)

        row2 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts2'])
        row2.place(x=525, y=160, width=100, height=25)

        perc_row2 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw2'])
        perc_row2.place(x=238, y=160, width=80, height=25)

    def row_3x(self):
        row1 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts1'])
        row1.place(x=525, y=130, width=100, height=25)
        perc_row1 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw1'])
        perc_row1.place(x=238, y=130, width=80, height=25)
        row2 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts2'])
        row2.place(x=525, y=160, width=100, height=25)
        perc_row2 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw2'])
        perc_row2.place(x=238, y=160, width=80, height=25)
        row3 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts3'])
        row3.place(x=525, y=190, width=100, height=25)
        perc_row3 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw3'])
        perc_row3.place(x=238, y=190, width=80, height=25)

    def row_4x(self):
        row1 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts1'])
        row1.place(x=525, y=130, width=100, height=25)
        perc_row1 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw1'])
        perc_row1.place(x=238, y=130, width=80, height=25)
        row2 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts2'])
        row2.place(x=525, y=160, width=100, height=25)
        perc_row2 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw2'])
        perc_row2.place(x=238, y=160, width=80, height=25)
        row3 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts3'])
        row3.place(x=525, y=190, width=100, height=25)
        perc_row3 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw3'])
        perc_row3.place(x=238, y=190, width=80, height=25)
        row4 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts4'])
        row4.place(x=525, y=220, width=100, height=25)
        perc_row4 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw4'])
        perc_row4.place(x=238, y=220, width=80, height=25)

    def row_5x(self):
        row1 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts1'])
        row1.place(x=525, y=130, width=100, height=25)
        perc_row1 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw1'])
        perc_row1.place(x=238, y=130, width=80, height=25)
        row2 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts2'])
        row2.place(x=525, y=160, width=100, height=25)
        perc_row2 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw2'])
        perc_row2.place(x=238, y=160, width=80, height=25)
        row3 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts3'])
        row3.place(x=525, y=190, width=100, height=25)
        perc_row3 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw3'])
        perc_row3.place(x=238, y=190, width=80, height=25)
        row4 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts4'])
        row4.place(x=525, y=220, width=100, height=25)
        perc_row4 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw4'])
        perc_row4.place(x=238, y=220, width=80, height=25)
        row5 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts5'])
        row5.place(x=525, y=250, width=100, height=25)
        perc_row5 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw5'])
        perc_row5.place(x=238, y=250, width=80, height=25)

    def row_6x(self):
        row1 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts1'])
        row1.place(x=525, y=130, width=100, height=25)
        perc_row1 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw1'])
        perc_row1.place(x=238, y=130, width=80, height=25)
        row2 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts2'])
        row2.place(x=525, y=160, width=100, height=25)
        perc_row2 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw2'])
        perc_row2.place(x=238, y=160, width=80, height=25)
        row3 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts3'])
        row3.place(x=525, y=190, width=100, height=25)
        perc_row3 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw3'])
        perc_row3.place(x=238, y=190, width=80, height=25)
        row4 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts4'])
        row4.place(x=525, y=220, width=100, height=25)
        perc_row4 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw4'])
        perc_row4.place(x=238, y=220, width=80, height=25)
        row5 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts5'])
        row5.place(x=525, y=250, width=100, height=25)
        perc_row5 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw5'])
        perc_row5.place(x=238, y=250, width=80, height=25)
        row6 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts6'])
        row6.place(x=525, y=280, width=100, height=25)
        perc_row6 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw6'])
        perc_row6.place(x=238, y=280, width=80, height=25)

    def row_7x(self):
        row1 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts1'])
        row1.place(x=525, y=130, width=100, height=25)
        perc_row1 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw1'])
        perc_row1.place(x=238, y=130, width=80, height=25)
        row2 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts2'])
        row2.place(x=525, y=160, width=100, height=25)
        perc_row2 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw2'])
        perc_row2.place(x=238, y=160, width=80, height=25)
        row3 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts3'])
        row3.place(x=525, y=190, width=100, height=25)
        perc_row3 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw3'])
        perc_row3.place(x=238, y=190, width=80, height=25)
        row4 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts4'])
        row4.place(x=525, y=220, width=100, height=25)
        perc_row4 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw4'])
        perc_row4.place(x=238, y=220, width=80, height=25)
        row5 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts5'])
        row5.place(x=525, y=250, width=100, height=25)
        perc_row5 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw5'])
        perc_row5.place(x=238, y=250, width=80, height=25)
        row6 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts6'])
        row6.place(x=525, y=280, width=100, height=25)
        perc_row6 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw6'])
        perc_row6.place(x=238, y=280, width=80, height=25)
        row7 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts7'])
        row7.place(x=525, y=310, width=100, height=25)
        perc_row7 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw7'])
        perc_row7.place(x=238, y=310, width=80, height=25)

    def row_8x(self):
        row1 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts1'])
        row1.place(x=525, y=130, width=100, height=25)
        perc_row1 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw1'])
        perc_row1.place(x=238, y=130, width=80, height=25)
        row2 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts2'])
        row2.place(x=525, y=160, width=100, height=25)
        perc_row2 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw2'])
        perc_row2.place(x=238, y=160, width=80, height=25)
        row3 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts3'])
        row3.place(x=525, y=190, width=100, height=25)
        perc_row3 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw3'])
        perc_row3.place(x=238, y=190, width=80, height=25)
        row4 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts4'])
        row4.place(x=525, y=220, width=100, height=25)
        perc_row4 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw4'])
        perc_row4.place(x=238, y=220, width=80, height=25)
        row5 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts5'])
        row5.place(x=525, y=250, width=100, height=25)
        perc_row5 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw5'])
        perc_row5.place(x=238, y=250, width=80, height=25)
        row6 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts6'])
        row6.place(x=525, y=280, width=100, height=25)
        perc_row6 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw6'])
        perc_row6.place(x=238, y=280, width=80, height=25)
        row7 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts7'])
        row7.place(x=525, y=310, width=100, height=25)
        perc_row7 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw7'])
        perc_row7.place(x=238, y=310, width=80, height=25)
        row8 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts8'])
        row8.place(x=525, y=340, width=100, height=25)
        perc_row8 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw8'])
        perc_row8.place(x=238, y=340, width=80, height=25)

    def row_9x(self):
        row1 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts1'])
        row1.place(x=525, y=130, width=100, height=25)
        perc_row1 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw1'])
        perc_row1.place(x=238, y=130, width=80, height=25)
        row2 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts2'])
        row2.place(x=525, y=160, width=100, height=25)
        perc_row2 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw2'])
        perc_row2.place(x=238, y=160, width=80, height=25)
        row3 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts3'])
        row3.place(x=525, y=190, width=100, height=25)
        perc_row3 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw3'])
        perc_row3.place(x=238, y=190, width=80, height=25)
        row4 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts4'])
        row4.place(x=525, y=220, width=100, height=25)
        perc_row4 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw4'])
        perc_row4.place(x=238, y=220, width=80, height=25)
        row5 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts5'])
        row5.place(x=525, y=250, width=100, height=25)
        perc_row5 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw5'])
        perc_row5.place(x=238, y=250, width=80, height=25)
        row6 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts6'])
        row6.place(x=525, y=280, width=100, height=25)
        perc_row6 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw6'])
        perc_row6.place(x=238, y=280, width=80, height=25)
        row7 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts7'])
        row7.place(x=525, y=310, width=100, height=25)
        perc_row7 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw7'])
        perc_row7.place(x=238, y=310, width=80, height=25)
        row8 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts8'])
        row8.place(x=525, y=340, width=100, height=25)
        perc_row8 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw8'])
        perc_row8.place(x=238, y=340, width=80, height=25)
        row9 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts9'])
        row9.place(x=525, y=370, width=100, height=25)
        perc_row9 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw9'])
        perc_row9.place(x=238, y=370, width=80, height=25)

    def row_10x(self):
        row1 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts1'])
        row1.place(x=525, y=130, width=100, height=25)
        perc_row1 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw1'])
        perc_row1.place(x=238, y=130, width=80, height=25)
        row2 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts2'])
        row2.place(x=525, y=160, width=100, height=25)
        perc_row2 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw2'])
        perc_row2.place(x=238, y=160, width=80, height=25)
        row3 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts3'])
        row3.place(x=525, y=190, width=100, height=25)
        perc_row3 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw3'])
        perc_row3.place(x=238, y=190, width=80, height=25)
        row4 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts4'])
        row4.place(x=525, y=220, width=100, height=25)
        perc_row4 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw4'])
        perc_row4.place(x=238, y=220, width=80, height=25)
        row5 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts5'])
        row5.place(x=525, y=250, width=100, height=25)
        perc_row5 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw5'])
        perc_row5.place(x=238, y=250, width=80, height=25)
        row6 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts6'])
        row6.place(x=525, y=280, width=100, height=25)
        perc_row6 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw6'])
        perc_row6.place(x=238, y=280, width=80, height=25)
        row7 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts7'])
        row7.place(x=525, y=310, width=100, height=25)
        perc_row7 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw7'])
        perc_row7.place(x=238, y=310, width=80, height=25)
        row8 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts8'])
        row8.place(x=525, y=340, width=100, height=25)
        perc_row8 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw8'])
        perc_row8.place(x=238, y=340, width=80, height=25)
        row9 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                            values=self.material_vlu, textvariable=self.mts['mts9'])
        row9.place(x=525, y=370, width=100, height=25)
        perc_row9 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw9'])
        perc_row9.place(x=238, y=370, width=80, height=25)
        row10 = ttk.Combobox(self, font=('Cairo', 10), justify='center', state='readonly',
                             values=self.material_vlu, textvariable=self.mts['mts10'])
        row10.place(x=525, y=400, width=100, height=25)
        perc_row10 = Entry(self, font=('Tajawal', 12), justify='center', bd=1, textvariable=self.rows['raw10'])
        perc_row10.place(x=238, y=400, width=80, height=25)

    def rewi(self, *args, **kwargs):
        if self.col_qun.get() == 1:
            self.row_1x()
        if self.col_qun.get() == 2:
            self.row_2x()
        if self.col_qun.get() == 3:
            self.row_3x()
        if self.col_qun.get() == 4:
            self.row_4x()
        if self.col_qun.get() == 5:
            self.row_5x()
        if self.col_qun.get() == 6:
            self.row_6x()
        if self.col_qun.get() == 7:
            self.row_7x()
        if self.col_qun.get() == 8:
            self.row_8x()
        if self.col_qun.get() == 9:
            self.row_9x()
        if self.col_qun.get() == 10:
            self.row_10x()

    def submit(self):
        try:
            pass
        except:
            messagebox.showerror(
                "Error", "خطأ، بعض البيانات التي قمت بأدخالها غير صحيحة\nتأكد ان الارقام مكتوبه بالانجليزية")
        else:
            op = messagebox.askyesno("Save Data", "هـل انـت مـتـأكـد انـك تـرغـب بإضافة لــون جديد ؟")
            if op > 0:
                if self.col_qun.get() == 1:
                    rg_color_t(name=self.col_name.get(), t_n='M_1x')
                    rg_color_1x(name=self.col_name.get(), con_1=self.mts['mts1'].get(), con_p_1=self.rows['raw1'].get())
                if self.col_qun.get() == 2:
                    rg_color_t(name=self.col_name.get(), t_n='M_2x')
                    rg_color_2x(name=self.col_name.get(), con_1=self.mts['mts1'].get(), con_p_1=self.rows['raw1'].get(),
                                con_2=self.mts['mts2'].get(), con_p_2=self.rows['raw2'].get())
                if self.col_qun.get() == 3:
                    rg_color_t(name=self.col_name.get(), t_n='M_3x')
                    rg_color_3x(name=self.col_name.get(), con_1=self.mts['mts1'].get(), con_p_1=self.rows['raw1'].get(),
                                con_2=self.mts['mts2'].get(), con_p_2=self.rows['raw2'].get(),
                                con_3=self.mts['mts3'].get(), con_p_3=self.rows['raw3'].get())
                if self.col_qun.get() == 4:
                    rg_color_t(name=self.col_name.get(), t_n='M_4x')
                    rg_color_4x(name=self.col_name.get(), con_1=self.mts['mts1'].get(), con_p_1=self.rows['raw1'].get(),
                                con_2=self.mts['mts2'].get(), con_p_2=self.rows['raw2'].get(),
                                con_3=self.mts['mts3'].get(), con_p_3=self.rows['raw3'].get(),
                                con_4=self.mts['mts4'].get(), con_p_4=self.rows['raw4'].get())
                if self.col_qun.get() == 5:
                    rg_color_t(name=self.col_name.get(), t_n='M_5x')
                    rg_color_5x(name=self.col_name.get(), con_1=self.mts['mts1'].get(), con_p_1=self.rows['raw1'].get(),
                                con_2=self.mts['mts2'].get(), con_p_2=self.rows['raw2'].get(),
                                con_3=self.mts['mts3'].get(), con_p_3=self.rows['raw3'].get(),
                                con_4=self.mts['mts4'].get(), con_p_4=self.rows['raw4'].get(),
                                con_5=self.mts['mts5'].get(), con_p_5=self.rows['raw5'].get())
                if self.col_qun.get() == 6:
                    rg_color_t(name=self.col_name.get(), t_n='M_6x')
                    rg_color_6x(name=self.col_name.get(), con_1=self.mts['mts1'].get(), con_p_1=self.rows['raw1'].get(),
                                con_2=self.mts['mts2'].get(), con_p_2=self.rows['raw2'].get(),
                                con_3=self.mts['mts3'].get(), con_p_3=self.rows['raw3'].get(),
                                con_4=self.mts['mts4'].get(), con_p_4=self.rows['raw4'].get(),
                                con_5=self.mts['mts5'].get(), con_p_5=self.rows['raw5'].get(),
                                con_6=self.mts['mts6'].get(), con_p_6=self.rows['raw6'].get())
                if self.col_qun.get() == 7:
                    rg_color_t(name=self.col_name.get(), t_n='M_7x')
                    rg_color_7x(name=self.col_name.get(), con_1=self.mts['mts1'].get(), con_p_1=self.rows['raw1'].get(),
                                con_2=self.mts['mts2'].get(), con_p_2=self.rows['raw2'].get(),
                                con_3=self.mts['mts3'].get(), con_p_3=self.rows['raw3'].get(),
                                con_4=self.mts['mts4'].get(), con_p_4=self.rows['raw4'].get(),
                                con_5=self.mts['mts5'].get(), con_p_5=self.rows['raw5'].get(),
                                con_6=self.mts['mts6'].get(), con_p_6=self.rows['raw6'].get(),
                                con_7=self.mts['mts7'].get(), con_p_7=self.rows['raw7'].get())
                if self.col_qun.get() == 8:
                    rg_color_t(name=self.col_name.get(), t_n='M_8x')
                    rg_color_8x(name=self.col_name.get(), con_1=self.mts['mts1'].get(), con_p_1=self.rows['raw1'].get(),
                                con_2=self.mts['mts2'].get(), con_p_2=self.rows['raw2'].get(),
                                con_3=self.mts['mts3'].get(), con_p_3=self.rows['raw3'].get(),
                                con_4=self.mts['mts4'].get(), con_p_4=self.rows['raw4'].get(),
                                con_5=self.mts['mts5'].get(), con_p_5=self.rows['raw5'].get(),
                                con_6=self.mts['mts6'].get(), con_p_6=self.rows['raw6'].get(),
                                con_7=self.mts['mts7'].get(), con_p_7=self.rows['raw7'].get(),
                                con_8=self.mts['mts8'].get(), con_p_8=self.rows['raw8'].get())
                if self.col_qun.get() == 9:
                    rg_color_t(name=self.col_name.get(), t_n='M_9x')
                    rg_color_9x(name=self.col_name.get(), con_1=self.mts['mts1'].get(), con_p_1=self.rows['raw1'].get(),
                                con_2=self.mts['mts2'].get(), con_p_2=self.rows['raw2'].get(),
                                con_3=self.mts['mts3'].get(), con_p_3=self.rows['raw3'].get(),
                                con_4=self.mts['mts4'].get(), con_p_4=self.rows['raw4'].get(),
                                con_5=self.mts['mts5'].get(), con_p_5=self.rows['raw5'].get(),
                                con_6=self.mts['mts6'].get(), con_p_6=self.rows['raw6'].get(),
                                con_7=self.mts['mts7'].get(), con_p_7=self.rows['raw7'].get(),
                                con_8=self.mts['mts8'].get(), con_p_8=self.rows['raw8'].get(),
                                con_9=self.mts['mts9'].get(), con_p_9=self.rows['raw9'].get())
                if self.col_qun.get() == 10:
                    rg_color_t(name=self.col_name.get(), t_n='M_10x')
                    rg_color_10x(name=self.col_name.get(), con_1=self.mts['mts1'].get(),
                                 con_p_1=self.rows['raw1'].get(),
                                 con_2=self.mts['mts2'].get(), con_p_2=self.rows['raw2'].get(),
                                 con_3=self.mts['mts3'].get(), con_p_3=self.rows['raw3'].get(),
                                 con_4=self.mts['mts4'].get(), con_p_4=self.rows['raw4'].get(),
                                 con_5=self.mts['mts5'].get(), con_p_5=self.rows['raw5'].get(),
                                 con_6=self.mts['mts6'].get(), con_p_6=self.rows['raw6'].get(),
                                 con_7=self.mts['mts7'].get(), con_p_7=self.rows['raw7'].get(),
                                 con_8=self.mts['mts8'].get(), con_p_8=self.rows['raw8'].get(),
                                 con_9=self.mts['mts9'].get(), con_p_9=self.rows['raw9'].get(),
                                 con_10=self.mts['mts10'].get(), con_p_10=self.rows['raw10'].get())
                messagebox.showinfo("Saved", "تـم إضـافـة الـلـون بـنـجـاح")
                self.destroy()
