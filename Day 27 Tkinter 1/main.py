from tkinter import *

window = Tk()
window.title("Mile to KM Convertor")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

#buttons
def button_click():
    labelkm['text'] = round(float(input.get()) * 1.609, 2)

#label
label = Label(text= "Miles", font=("Arial", 24, "bold"))
label.grid(column=3, row= 0)

label2 = Label(text= "is equal to", font=("Arial", 24, "bold"))
label2.grid(column=1, row= 1)

labelkm = Label(text= "0", font=("Arial", 24, "bold"))
labelkm.grid(column=2, row= 1)

label3 = Label(text= "is equal to", font=("Arial", 24, "bold"))
label3.grid(column=1, row= 1)

label4 = Label(text= "Km", font=("Arial", 24, "bold"))
label4.grid(column=3, row= 1)


button = Button(text="Calculate", command = button_click)
button.grid(column=2, row=2)

#entry
input = Entry(width = 20)
input.grid(column=2, row=0)

#execute loop
window.mainloop()