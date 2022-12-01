from tkinter import *
window = Tk()

label1=Label(window, text="Title")
label1.grid(row=0, column=0)

label2=Label(window, text="Author")
label2.grid(row=0, column=2)

label3=Label(window, text="Year")
label3.grid(row=1, column=0)

label4=Label(window, text="ISBN")
label4.grid(row=1, column=2)

window.mainloop()