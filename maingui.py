from tkinter import *
from tkinter import messagebox

#fönster
root = Tk()
root.title("Lotteri")

#fönster storlek
root.geometry("300x300")

#labels
label_antal = Label(root, text="Max antal lotter 3!")
label_antal.grid(row=0, column=0, sticky=E, padx=5, pady=5)


#inputs
textbox_antal = Entry(root, width=2)
textbox_antal.grid(row=0, column=1, sticky=W, padx=5, pady=5)
textbox_antal.focus_set()

def clickSlumpaButton():
    messagebox.showinfo("click")

#knapp
btn_random = Button(text="lucky bastard", command= clickSlumpaButton)
btn_random.grid(row=1, column=0, sticky=E, padx=15, pady=15)


#listbox
listbox = Listbox(root, height=4, width=30, bg="white", activestyle="dotbox", font="Ariel", fg="blue")
listbox.grid(row=2, column=0, padx=15, pady=15)

root.mainloop()