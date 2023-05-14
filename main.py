from src.modules import encripto
from src.modules import decripto
import tkinter as tk
from tkinter import *

# colors
color1 = "#BBB09B" #Khaki
color2 = "#D7BBA8" #Desert Sand
color3 = "#EFA8B8" #Cherry Blossom Pink
color4 = "#E26D5A" #Burned Sienna
color5 = "#3E2A35" #Dark Purple

# Create main window
mainScreen = Tk()
mainScreen.title("Cripto App")
mainScreen.geometry("600x400")
mainScreen.resizable(width=False, height=False)
mainScreen.config(bg=color1)

# label title
label_title = Label(mainScreen, width=20, text= "Cripto App", font='Times 25',  fg=color5, bg=color1)
label_title.place(x=125, y=20)

# Fields to put the and receive the texts
field_cript = Entry(mainScreen, width=50, relief='sunken', font='Times 15')
field_cript.place(x=60, y=110)

field_decript = Entry(mainScreen, width=50, relief='sunken', font='Times 15')
field_decript.place(x=60, y=260)

# Buttons to cripto and decripto text's 
button1 = Button(mainScreen, width=15, height=2, text="Cripto", command= lambda: encripto.crip(str(field_cript)), relief='raised', bg=color3)
button1.place(x=250, y=150)
button2 = Button(mainScreen, width=15, height=2, text="Decripto", relief='raised', bg=color3)
button2.place(x=250, y=300)



mainScreen.mainloop()


"""entry_crip = input("Digite o texto a ser criptografado: ")

encripto.crip(entry_crip)

selectTf = input("Deseja descriptografar y/n: ")

try:
        if selectTf  == "y":
                entry_decr = input("Digite o texto a ser descriptografado: ")
                decripto.decrip(entry_decr)
        elif selectTf == "n":
                print("__Encerrado__") 
        else:
                print("__Escolha_Inválida__")
except:
        print("Erro (01): selectTf não cumpre os pré-requisitos")
"""