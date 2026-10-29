from tkinter import *
from tkinter import messagebox
import cv2
import os

root = Tk()
root.geometry('290x500')
root.title('screen lock [yousef]')
root.iconbitmap('')
root.resizable(False, False)
root.attributes('-alpha', 0.8)

error1 = None

#=======Define==========

def one(event = None):
    En1.insert(END, 1)
def tow(event = None):
    En1.insert(END, 2)
def three(event = None):
    En1.insert(END, 3)
def four(event = None):
    En1.insert(END, 4)
def five(event = None):
    En1.insert(END, 5)
def six(event = None):
    En1.insert(END, 6)
def seven(event = None):
    En1.insert(END, 7)
def eight(event = None):
    En1.insert(END, 8)
def nine(event = None):
    En1.insert(END, 9)
def zero(event = None):
    En1.insert(END, 0)

def reset(event = None):
    En1.delete('0', END)
    global error1
    if error1:
        error1.place(x=1200, y=1200)

def OK():
    global error1
    passow = En1.get()
    if passow == '123456':
        win = Tk()
        win.geometry('290x20')
        win.title('Yousef')
        text = Label(win, text = '🔓welcome to program🔓')
        text.pack()
        win.mainloop()
    else:
        if error1:
            error1.destroy()
        error1 = Label(F1, text='Error password !!', fg='red', bg='white', font=('stencil', 12))
        error1.place(x=80, y=90)
       
        # التقاط صورة عند إدخال كلمة مرور خاطئة
        s = cv2.VideoCapture(0)
        ret, image = s.read()
        if ret:
            cv2.imwrite('look.png', image)
        s.release()
        del(s)


title = Label(root, text='screen lock', fg='white', bg='#D82148', font=('stencil', 21))
title.pack(fill=X)

F1 = Frame(root, bg='white')
F1.place(x=1, y=38, width=298, height=460)

title_pass = Label(F1, text='Enter Password', fg='black', bg='white', font=('stencil', 15))
title_pass.place(x=55, y=10)

En1 = Entry(F1, justify=CENTER, font=('impact', 25), relief=RIDGE, width=10, bg='white', fg='#D82148')
En1.place(x=50, y=50)

# الأصفار والأزرار
b1 = Button(F1, text='1', font=('stencil', 25), bg='white', bd=0, relief=GROOVE, width=3, cursor='hand2', command=one)
b1.place(x=20, y=130)
b2 = Button(F1, text='2', font=('stencil', 25), bg='white', bd=0, relief=GROOVE, width=3, cursor='hand2', command=tow)
b2.place(x=110, y=130)
b3 = Button(F1, text='3', font=('stencil', 25), bg='white', bd=0, relief=GROOVE, width=3, cursor='hand2', command=three)
b3.place(x=200, y=130)

b4 = Button(F1, text='4', font=('stencil', 25), bg='white', bd=0, relief=GROOVE, width=3, cursor='hand2', command=four)
b4.place(x=20, y=215)
b5 = Button(F1, text='5', font=('stencil', 25), bg='white', bd=0, relief=GROOVE, width=3, cursor='hand2', command=five)
b5.place(x=110, y=215)
b6 = Button(F1, text='6', font=('stencil', 25), bg='white', bd=0, relief=GROOVE, width=3, cursor='hand2', command=six)
b6.place(x=200, y=215)

b7 = Button(F1, text='7', font=('stencil', 25), bg='white', bd=0, relief=GROOVE, width=3, cursor='hand2', command=seven)
b7.place(x=20, y=300)
b8 = Button(F1, text='8', font=('stencil', 25), bg='white', bd=0, relief=GROOVE, width=3, cursor='hand2', command=eight)
b8.place(x=110, y=300)
b9 = Button(F1, text='9', font=('stencil', 25), bg='white', bd=0, relief=GROOVE, width=3, cursor='hand2', command=nine)
b9.place(x=200, y=300)

# الصف الأخير (مفتاح الحذف، الصفر، ومفتاح الموافقة مع تعديل أماكنها لتجنب التداخل)
bR = Button(F1, text='❌', fg='red', font=('stencil', 25), bg='white', bd=0, relief=GROOVE, width=3, cursor='hand2', command=reset)
bR.place(x=20, y=385)

b0 = Button(F1, text='0', font=('stencil', 25), bg='white', bd=0, relief=GROOVE, width=3, cursor='hand2', command=zero)
b0.place(x=110, y=385)

bOK = Button(F1, text='🔑', fg='yellow', font=('stencil', 25), bg='white', bd=0, relief=GROOVE, width=3, cursor='hand2', command=OK)
bOK.place(x=200, y=385)

root.mainloop()
