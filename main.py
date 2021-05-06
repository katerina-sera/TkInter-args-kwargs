import tkinter

window = tkinter.Tk()
window.title("Mile to KM Converter")
window.minsize(500, 300)


def button_clicked():
    answer = int(input.get()) * 1.6
    my_km_label.config(text=round(answer))
    my_km_label.grid(column=1, row=1)
#     input.get()

# Label
# my_label = tkinter.Label(text="I'm a label", font=("Arial", 24,"italic"))
# my_label.config(text="Hope hey")
# my_label.grid(column=0, row=0)
# my_label.config(padx=50, pady=50)

button = tkinter.Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#
# new_button = tkinter.Button(text="I'm a new button")
# new_button.grid(column=2, row=0)

# Entry

input = tkinter.Entry(width=10)
input.grid(column=1, row=0)

my_label = tkinter.Label(text="Miles")
my_label.grid(column=2, row=0)

my_label_2 = tkinter.Label(text="Km")
my_label_2.grid(column=2, row=1)

my_km_label = tkinter.Label(text="0")
my_km_label.grid(column=1, row=1)


km_text_label = tkinter.Label(text="is equal to")
km_text_label.grid(column=0, row=1)

# Layouts managers:
# if there are no layout man., widget won't be shown
# pack()-we could specify side-right, bottom.
# place()-x=0,y=0-top left corner. But it's also difficult to specify precise position.
# grid()-column=0, row=0. If there is no other specified widgets, it wont change position from 0.
# You can't mix pack() and grid()





window.mainloop()