from tkinter import  *

window = Tk()

window.title("My Frist GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

# lable
my_label=Label(text="india",font=("Arial Black",24,"bold"))
my_label.config(text="manoj priyanjana")
my_label.grid(column=8,row=8)
my_label.config(padx=50,pady=50)


# button
button = Button(text="Click Me",command=button_clicked)
button.grid(column=1,row=1)

new_button = Button(text="New Button")

# Entry
input = Entry(width=10)
print(input.get())
input.grid(column=3,row=2)


#-------
window.mainloop()
