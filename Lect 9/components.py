from tkinter import *

hello_label = Label(text='hello')
hello_label.grid(row=0, column=0)

hello_label = Label(text='hello', font=('Verdana', 24, 'bold'),
bg='blue', fg='white')

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=0, columnspan=2)
label4.grid(row=1, column=2)
label5.grid(row=2, column=2)

entry = Entry()
entry.grid(row=0, column=0)

string_value = entry.get()
num_value = eval(entry.get())