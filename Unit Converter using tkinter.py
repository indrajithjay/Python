from tkinter import * #import tkinter packages
from tkinter import ttk #import ttk
from tkinter import messagebox #import messagebox


winpop= Tk() #declare the function
winpop.geometry("750x250")#Define geometry of the window
winpop.title("Distance Converter") #Title for the GUI

#data2 = input("Enter the 2nd value:")#get the user input

#Define a function to open the Popup Dialogue
def popupwin():
   #Create a Toplevel window
   top= Toplevel(winpop)
   top.geometry("750x250")



label = Label(winpop, text="Enter the distance in KM", font=('Arial 10 bold')) # create a label to display
label.pack(pady=20)
# Create an Entry widget to accept User Input
entry = Entry(winpop, width=40)
entry.focus_set()
entry.pack()


def cal_sum(): #define a function to convert KM to miles
    t1 = int(entry.get()) #get user entry
    sum = t1 * 0.6214 #convert the distance
    label.config(text=sum)
    messagebox.showinfo("Distance in Miles : ", sum)  # display a message box to get user data



# Create a Button to validate Entry Widget
ttk.Button(winpop, text="Convert to Miles", width=20, command=cal_sum).pack(pady=20)
#def on_click():


winpop.mainloop()