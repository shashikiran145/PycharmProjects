from tkinter import *

window = Tk()
window.title("Miles to kms converter")
window.minsize(width=200, height=200)
window.config(padx=20, pady=20)    # some space will be left out along the edges

# Create a label

mile = Label(text="miles")
mile.grid(row=1, column=3)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=2, column=1)

op = Label(text="")
op.grid(row=2, column=2)

km = Label(text="kms")
km.grid(row=2, column=3)


# my_label = Label(text="I am a label", font=("Arial", 30, "bold"))
# pack is required to get the label on the screen
# my_label.pack()
# place is used for precise placement, Top left is (0,0)
# my_label.place(x=10, y=80)
# Takes input according to grids (rows and columns), but needs a reference for (0,0)
# my_label.grid(column=0, row=0)


# my_label["text"] = "I label"
# my_label.config(text='I am label')
#

# Create a button_1

def button_clicked():
    miles = int(ip.get())
    kms = round((miles * 1.6), 2)
    print(kms)
    op["text"] = kms


button_1 = Button(text="Calculate", command=button_clicked)
# button_1.pack()
# button_1.place(x=0, y=0)
button_1.grid(row=3, column=2)


# Create an entry

ip = Entry(width=20)
# input.insert(0, "Enter the number")
# input.pack()
# input.place(x=50, y=50)
ip.grid(row=1, column=2)

window.mainloop()
