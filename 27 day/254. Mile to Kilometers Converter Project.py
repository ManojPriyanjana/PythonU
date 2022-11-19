from tkinter import *
def miles_to_km():
    miles=float(miles_input.get())
    km =round(miles*1.689)
    kilometer_result_label.config(text=f"{km}")



window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=28,pady=28)

miles_input = Entry(width=7)
miles_input.grid(column=2,row=0)

miles_label =Label(text="Miles")
miles_label.grid(column=3,row=0)

is_equal_label =Label(text="is equal to")
is_equal_label.grid(column=1,row=1)

kilometer_result_label =Label(text="0")
kilometer_result_label.grid(column=2,row=1)

kilometer_label =Label(text="km")
kilometer_label.grid(column=3,row=1)

calculater_button = Button(text="Calculate",command=miles_to_km)
calculater_button.grid(column=2,row=2)





window.mainloop()