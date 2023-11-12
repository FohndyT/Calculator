# Pour que import marche :
#   1. Ouvrir le terminal de ce projet pis ecrire : pip install customtkinter
#   2. Ecrire apres : pip install packaging
# Pour mettre à jour : pip install customtkinter --upgrade



# Import
import tkinter
import customtkinter

# Variables
calculationText = ""
storedValues = []
indexStoredValues = len(storedValues) - 2

# Setting the theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Creating the window
window = customtkinter.CTk()
window.title("Calculator")
window.geometry("400x475")
window.resizable(width=False, height=False) # Empeche l'utilisateur de changer la taille de la fenetre

# Esthetic
frame = customtkinter.CTkFrame(master=window)
frame.pack(pady = 20, padx = 20, fill = "both", expand = True)

# Show the operation on the screen
def showElement(element) :
    global calculationText
    calculationText += str(element)
    screenFrame.configure(text = calculationText)

def calculate() :
    global calculationText
    global storedValues

    try :
        screenFrame.configure(text = str(eval(calculationText.replace(" ", ""))))
        storedValues.append(str(eval(calculationText.replace(" ", ""))))
    except :
        screenFrame.configure(text = "Error")

def clear() :
    global calculationText
    global indexStoredValues

    calculationText = ""
    screenFrame.configure(text = "")

    indexStoredValues = len(storedValues) - 1 #Maybe fix

def delete() :
    global calculationText
    calculationText = calculationText[:-1]
    screenFrame.configure(text = calculationText)

# Not working
def back() :
    global indexStoredValues
    global calculationText
    global storedValues

    try :
        calculationText = storedValues[indexStoredValues]
        screenFrame.configure(text=calculationText)
    except :
        calculationText = storedValues[0]
        screenFrame.configure(text=calculationText)

    indexStoredValues -= 1

def endProgram() :
    window.quit()

def maxNumber() :
    calculationText = "99999999999999999999999999"
    screenFrame.configure(text=calculationText)


# Create the screen
screenFrame = customtkinter.CTkLabel(master = frame,
                                     fg_color = "green",
                                     width = 300,
                                     height = 75,
                                     text = "",
                                     text_color = "black",
                                     font = ("Arial", 20),
                                     justify = "right")
screenFrame.place(relx = 0.5, rely = 0.15, anchor = tkinter.CENTER)

# Premiere range
buttonEnd = customtkinter.CTkButton(master = frame, text = "End", fg_color = "red", width = 60, height = 10, command = lambda : endProgram())
buttonEnd.place(relx = 0.165, rely = 0.3, anchor = tkinter.CENTER)
buttonBack = customtkinter.CTkButton(master = frame, text = "Back", fg_color = "dark blue", width = 60, height = 10, command = lambda : back())
buttonBack.place(relx = 0.3883, rely = 0.3, anchor = tkinter.CENTER)
buttonDel = customtkinter.CTkButton(master = frame, text = "Del", fg_color = "orange", width = 60, height = 10, command = lambda : delete())
buttonDel.place(relx = 0.6116, rely = 0.3, anchor = tkinter.CENTER)
buttonClear = customtkinter.CTkButton(master = frame, text = "Clear", fg_color = "dark grey", width = 60, height = 10, command = lambda : clear())
buttonClear.place(relx = 0.835, rely = 0.3, anchor = tkinter.CENTER)

# Deuxieme range
button7 = customtkinter.CTkButton(master = frame, text = "7", fg_color = "grey", width = 50, height = 10, command = lambda : showElement(7))
button7.place(relx = 0.1455, rely = 0.4, anchor = tkinter.CENTER)
button8 = customtkinter.CTkButton(master = frame, text = "8", fg_color = "grey", width = 50, height = 10, command = lambda : showElement(8))
button8.place(relx = 0.320625, rely = 0.4, anchor = tkinter.CENTER)
button9 = customtkinter.CTkButton(master = frame, text = "9", fg_color = "grey", width = 50, height = 10, command = lambda : showElement(9))
button9.place(relx = 0.49575, rely = 0.4, anchor = tkinter.CENTER)

buttonParaRight = customtkinter.CTkButton(master = frame, text = " ( ", fg_color = "blue", width = 50, height = 10, command = lambda : showElement(" ( "))
buttonParaRight.place(relx = 0.671875, rely = 0.4, anchor = tkinter.CENTER)
buttonParaLeft = customtkinter.CTkButton(master = frame, text = " ) ", fg_color = "blue", width = 50, height = 10, command = lambda : showElement(" ) "))
buttonParaLeft.place(relx = 0.85, rely = 0.4, anchor = tkinter.CENTER)

# Troisieme range
button4 = customtkinter.CTkButton(master = frame, text = "4", fg_color = "grey", width = 50, height = 10, command = lambda : showElement(4))
button4.place(relx = 0.1455, rely = 0.5, anchor = tkinter.CENTER)
button5 = customtkinter.CTkButton(master = frame, text = "5", fg_color = "grey", width = 50, height = 10, command = lambda : showElement(5))
button5.place(relx = 0.320625, rely = 0.5, anchor = tkinter.CENTER)
button6 = customtkinter.CTkButton(master = frame, text = "6", fg_color = "grey", width = 50, height = 10, command = lambda : showElement(6))
button6.place(relx = 0.49575, rely = 0.5, anchor = tkinter.CENTER)

buttonPlus = customtkinter.CTkButton(master = frame, text = " + ", fg_color = "blue", width = 50, height = 10, command = lambda : showElement(" + "))
buttonPlus.place(relx = 0.671875, rely = 0.5, anchor = tkinter.CENTER)
buttonMinus = customtkinter.CTkButton(master = frame, text = " - ", fg_color = "blue", width = 50, height = 10, command = lambda : showElement(" - "))
buttonMinus.place(relx = 0.85, rely = 0.5, anchor = tkinter.CENTER)

# Quatrieme range
button1 = customtkinter.CTkButton(master = frame, text = "1", fg_color = "grey", width = 50, height = 10, command = lambda : showElement(1))
button1.place(relx = 0.1455, rely = 0.6, anchor = tkinter.CENTER)
button2 = customtkinter.CTkButton(master = frame, text = "2", fg_color = "grey", width = 50, height = 10, command = lambda : showElement(2))
button2.place(relx = 0.320625, rely = 0.6, anchor = tkinter.CENTER)
button3 = customtkinter.CTkButton(master = frame, text = "3", fg_color = "grey", width = 50, height = 10, command = lambda : showElement(3))
button3.place(relx = 0.49575, rely = 0.6, anchor = tkinter.CENTER)

buttonTimes = customtkinter.CTkButton(master = frame, text = " x ", fg_color = "blue", width = 50, height = 10, command = lambda : showElement(" * "))
buttonTimes.place(relx = 0.671875, rely = 0.6, anchor = tkinter.CENTER)
buttonDivide = customtkinter.CTkButton(master = frame, text = " / ", fg_color = "blue", width = 50, height = 10, command = lambda : showElement(" / "))
buttonDivide.place(relx = 0.85, rely = 0.6, anchor = tkinter.CENTER)

# Cinquieme range
button0 = customtkinter.CTkButton(master = frame, text = "0", fg_color = "grey", width = 50, height = 10, command = lambda : showElement(0))
button0.place(relx = 0.1455, rely = 0.7, anchor = tkinter.CENTER)

buttonPoint = customtkinter.CTkButton(master = frame, text = ".", fg_color = "grey", width = 50, height = 10, command = lambda : showElement("."))
buttonPoint.place(relx = 0.320625, rely = 0.7, anchor = tkinter.CENTER)
buttonMax = customtkinter.CTkButton(master = frame, text = "Max", fg_color = "grey", width = 50, height = 10, command = lambda : maxNumber())
buttonMax.place(relx = 0.49575, rely = 0.7, anchor = tkinter.CENTER)
buttonEqual = customtkinter.CTkButton(master = frame, text = "=", fg_color = "blue", width = 115, height = 10, command = lambda : calculate())
buttonEqual.place(relx = 0.76, rely = 0.7, anchor = tkinter.CENTER)

window.mainloop()

