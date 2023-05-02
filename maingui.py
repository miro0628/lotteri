from tkinter import *
from tkinter import messagebox
import lotteri

lotter = lotteri.Lotteri()

#fönster
root = Tk()
root.title("Lotteri")

#fönster storlek
root.geometry("500x300")

#labels
label_antal = Label(root, text="Max antal lotter 3!")
label_antal.grid(row=0, column=0, sticky=E, padx=5, pady=5)


#inputs
textbox_antal = Entry(root, width=2)
textbox_antal.grid(row=0, column=1, sticky=W, padx=5, pady=5)
textbox_antal.focus_set()

def update_listbox(antal_lotter):
    #tabort gamla vinster
    listbox.delete(0, END)
    #lägg till nya vinster
    listbox.insert(1, "Grattis! Du vann detta:")

    try:
        int_antal_lotter = int(antal_lotter)
        i=0

        

        if(int_antal_lotter < 4):

            while i < int_antal_lotter +1:

                vinst = lotter.get_vinst()
                listbox.insert((i+2), vinst)
                i += i+1

        else:
            messagebox.showinfo("Max 4 lotter!")

    except ValueError:
        messagebox.showinfo("endast sifror")



def clickSlumpaButton():
    antal_lott = textbox_antal.get()
    
    textbox_antal.delete(0, END)
    textbox_antal.focus_set()

    vinst1 = lotter.get_vinst()

    update_listbox(antal_lott)

#knapp
btn_random = Button(text="lucky bastard", command= clickSlumpaButton)
btn_random.grid(row=1, column=0, sticky=E, padx=15, pady=15)


#listbox
listbox = Listbox(root, height=4, width=30, bg="white", activestyle="dotbox", font="Ariel", fg="blue")
listbox.grid(row=2, column=0, columnspan=2, padx=15, pady=15)

root.mainloop()