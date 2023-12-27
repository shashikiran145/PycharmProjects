# def add(*args):
#     sume = 0
#     for n in args:
#         sume = sume + n
#     print(sume)
#
#
# add(1, 2, 3, 4)

# def calculate(n, **kwargs):
#     print(kwargs)
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(3, add=3, multiply=5)


# class Car:
    # def __init__(self, **kw):
    #     self.make = kw["make"]
    #     self.model = kw["model"]

    # my_car = Car(make="Mercedes")
    # print(my_car.model)
    # If any of the keyword isn't specified, we get an error
    # So we use get() to get rid of that error. Even if we don't specify, we get "None" as the output.
#     def __init__(self, **kw):
#         self.make = kw.get("make")
#         self.model = kw.get("model")
#
#
# my_car = Car(make="Mercedes")
# print(my_car.model)


# def bar(spam, eggs, toast='yes please!', ham=0):
#     print(spam, eggs, toast, ham)
#
#
# bar(1, 2)

# def test(*args):
#     print(args)
#     print(type(args))
#
#
# test(1, 2, 3, 5)


# def all_aboard(a, *args, **kw):
#     print(a, args, kw)
#
#
# all_aboard(4, 7, 3, 0, x=10, y=64)


# from tkinter import *
#
# window = Tk()
# window.title("My first tk program")
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)    # some space will be left out along the edges
#
# # Create a label
#
# my_label = Label(text="I am a label", font=("Arial", 30, "bold"))
# # pack is required to get the label on the screen
# # my_label.pack()
# # place is used for precise placement, Top left is (0,0)
# # my_label.place(x=10, y=80)
# # Takes input according to grids (rows and columns), but needs a reference for (0,0)
# my_label.grid(column=0, row=0)
#
#
# my_label["text"] = "I label"
# my_label.config(text='I am label')
#
#
# # Create a button_1
#
# def button_clicked():
#     print("I clicked a button_1")
#     my_label["text"] = input.get()
#
#
# button_1 = Button(text="Click me for the update", command=button_clicked)
# # button_1.pack()
# # button_1.place(x=0, y=0)
# button_1.grid(row=1, column=1)
#
# button_2 = Button(text="I am a second button")
# # button_2.pack()
# # button_2.place(x=0, y=0)
# button_2.grid(row=0, column=2)
#
#
# # Create an entry
#
# input = Entry(width=55)
# # input.pack()
# # input.place(x=50, y=50)
# input.grid(row=2, column=3)
#
# window.mainloop()



