from tkinter import  *

window = Tk()

window.title("My Frist GUI Program")
window.minsize(width=500,height=300)

my_label=Label(text="india",font=("Arial Black",24,"bold"))
my_label.pack(side="left")



my_label.config(text="manoj priyanjana")
# ------
# button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)



button = Button(text="Click Me",command=button_clicked)
button.pack()

input = Entry(width=10)
input.pack()
print(input.get())

#-------
window.mainloop()
