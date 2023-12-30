from tkinter import *


def button_clicked():
    miles = float(ip.get())
    kms = round((miles * 1.609), 3)
    print(kms)
    op["text"] = kms


window = Tk()
window.title("Miles to kms converter")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)    # some space will be left out along the edges

mile = Label(text="miles")
mile.grid(row=1, column=3)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=2, column=1)

op = Label(text="0")
op.grid(row=2, column=2)

km = Label(text="kms")
km.grid(row=2, column=3)

button_1 = Button(text="Calculate", command=button_clicked)
button_1.grid(row=3, column=2)

ip = Entry(width=20)
ip.insert(0, "0")
ip.grid(row=1, column=2)

window.mainloop()
