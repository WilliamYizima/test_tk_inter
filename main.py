#!/usr/bin/python3
import tkinter as tk
from tkinter import Label, StringVar
import os

filename = os.getcwd()

# config window
root = tk.Tk()

# title
root.title('Test assao')

# open mode
# init minimize mode
# root.state('iconic')

# size windo
root.geometry('500x600+250+200')
root.resizable(False,False)
# root.configure(bg='#fcc2ae')
# root.minsize(500,600)
# root.maxsize(700,800)
# root.iconbitmap(f'images/icon.ico')

# entry
# password entry
# tk.Entry(show=*).grid(row=0,column=0)
# tk.Entry(bg='#fcc2ae').grid(row=0,column=1)

texto = StringVar()
texto.set('Meu label')

def test():
    texto.set('Texto Alterado')

# button
tk.Button(text="Send", bg='#fcc2ae', command=test).grid(row=1,column=0)
tk.Label(textvariable=texto,
         font='Arial 20',
         bd=1,
         relief='solid',
        #  width=20
        #   bg='#fcc2ae'
          ).grid(row=0,column=0)


root.mainloop()