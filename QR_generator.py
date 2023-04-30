#Ian Meister-QR code generator

#libraries
import qrcode
from tkinter import *

#Box for qr code scanner
root = Tk()
root.title('Ian\'s QR Code Generator')
root.geometry('1000x550')
root.config(bg='#AE2321')
root.resizable(False,False)

#Get Info output code

def generate():
    name=title.get()
    text=entry.get()
    qr=qrcode.make(text)
    qr.save("QR_"+str(name)+".png")


    global Image
    Image=PhotoImage(file="QR_"+str(name)+".png")
    Image_view.config(image=Image)


Image_view=Label(root,bg='#AE2321')
Image_view.pack(padx=50,pady=10,side=RIGHT)

Label(root,text="Title",fg='white',bg='#AE2321',font=15).place(x=50,y=170)
Label(root,text="Link",fg='white',bg='#AE2321',font=15).place(x=50,y=225)

title=Entry(root,width=13,font='arial 15')
title.place(x=50,y=200)

entry=Entry(root,width=13,font='arial 15')
entry.place(x=50,y=250)

Button(root,text='Generate',width=20,heigh=2,bg='black',fg='white',command=generate).place(x=50,y=300)

root.mainloop()

