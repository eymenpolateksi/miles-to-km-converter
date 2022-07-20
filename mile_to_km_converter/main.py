from tkinter import *


def miles_to_km():
    miles = mile_input.get()
    km = float(miles) * 1.609
    km_text.config(text=f"{km}")


window = Tk()
window.title("Miles+ to Km Converter")
window.config(padx=20, pady=20)

#Entry

mile_input = Entry(width=7)
mile_input.insert(END, "0")
mile_input.grid(column=1, row=0)

#text
mile_text = Label(text="Miles", font=("Arial", 15))
mile_text.grid(column=2, row=0)

text2 = Label(text="is equal to", font=("Arial", 15))
text2.grid(column=0, row=1)

km_text = Label(text="0", font=("Arial", 15))
km_text.grid(column=1, row=1)

km_text2 = Label(text="Km", font=("Arial", 15))
km_text2.grid(column=2, row=1)

#button
button = Button(text="Calculate", font=("Arial", 15), command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()