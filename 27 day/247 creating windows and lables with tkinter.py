import tkinter

window = tkinter.Tk()

window.title("My Frist GUI Program")
window.minsize(width=500,height=300)

my_label=tkinter.Label(text="india",font=("Arial Black",24,"bold"))
my_label.pack(side="left")



my_label.config(text="manoj priyanjana")

window.mainloop()