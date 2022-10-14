from tkinter import *

root = Tk()
root.geometry('900x500')

def submit():
    try:
        a = userentry.get()
        with open('submittion.txt', 'a') as f:
            f.write(f'{a}\n')
        Label(text="Entry was successful!", fg='green').grid(row=4, column=1)
        userentry.delete(0, END)
    except:
        Label(text="Error happened!", fg='red').grid(row=4, column=1)
user = Label(root, text="Name")
user.grid()

uservalue = StringVar()

userentry = Entry(root, textvariable=uservalue)
userentry.grid(column=1, row=0)

Button(text="Submit", command=submit).grid()

root.mainloop()