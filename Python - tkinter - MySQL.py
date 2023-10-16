#import pyodbc #import pyodbc package
import tkinter as tk #import the tkinter package
from tkinter import * #import all sub packages
from tkinter import messagebox #import messagebox
from tkinter import ttk #import ttk


canvas = tk.Tk() #declare a function
canvas.title("Tkinter Test Program") #Title for the GUI
canvas.geometry("800x600+300+50") #set the dimensions of the window
#data = ("1", "2", "3", "4","5") #data to be entered in the listbox
data = input("Enter the 1st value:"),\
      input("Enter the 2nd value:"), \
      input("Enter the 3rd Value"),\
      input("Enter the 4th Value"), \
      input("Enter the 5th Value")#get user input as the data
print(data) #print the values of 'data'
lb = tk.Listbox(canvas,height=5,width=50,selectmode='single') #create listbox

for num in data:
    lb.insert(END, num)
    lb.place(\
    x=250,\
    y=150) #loop for entering the "data" into the listbox (lb)

messagebox.showinfo("Messagebox ,Click to continue") #display a message box

def sel():
   selection = "You selected " + str(var.get())
   label.config(text = selection) #define the action for the radio button
var = IntVar() #declare the variable
L1 = tk.Label(canvas,
        text="Choose a programming language:",
        justify = tk.LEFT,
        )
L1.pack( anchor= W )#Label
R1 = Radiobutton(canvas, text="1: Python", variable=var, value=1,
                  command=sel) #radio button 1
R1.pack( anchor = W )
R2 = Radiobutton(canvas, text="2: C++", variable=var, value=2,
                  command=sel) #radio button 2
R2.pack( anchor = W )
R3 = Radiobutton(canvas, text="3: Java", variable=var, value=3,
                  command=sel) #radio button 3
R3.pack( anchor = W)

cmb = ttk.Combobox(canvas, width="10", values=("Python","C++","C#","Java")) # to create checkbox # cmb = Combobox
#create simple function to check what value user select from checkbox
def checkcmbo():

    if cmb.get() == "Python":
        messagebox.showinfo("What user choose", "you choose Python")
            # if user select One show this message
    elif cmb.get() == "C++":
        messagebox.showinfo("What user choose", "you choose C++")
     # if user select Two show this message
    elif cmb.get() == "C#":
        messagebox.showinfo("What user choose", "you choose C#")
    # if user select Three show this message
    elif cmb.get() == "Java":
        messagebox.showinfo("What user choose", "you choose Java")
    # if user select Four show this message
    elif cmb.get() == "":
        messagebox.showinfo("nothing to show!", "Invalid Selection")
cmb.place(relx="0.1",rely="0.1")
cmb.pack(side="top") #box alignment

btn = ttk.Button(canvas, text="Get Value",command=checkcmbo,) #get value button
btn.place(relx="0.5",rely="0.1")#button placement
btn.pack(side="bottom") #button alignment

label = Label(canvas)
label.pack()

# #connecting to local sql server using the local SQL database
conn = pyodbc.connect('Driver={SQL Server}';
                        'Server=DESKTOP-ULB8U2M\SQLEXPRESS';#SQL host system
                        'Database=AdventureWorksLT2019';#Test Database name
                        'Trusted_connection=yes';)
cursor = conn.cursor() #Cursor class to execute SQLite statement and fetch data from the result sets of the queries
cursor.execute('SELECT * from SalesLT.ProductModel where ProductModelID = 2')##select table and Filtering the SalesLT database table
for i in cursor:
    print(i[0])
pydata = i #declare a variable
print(pydata[0]) #print the returning values

def returndata():
    messagebox.showinfo("Data",pydata[0])
    lb1=tk.Listbox(canvas, height=10, width=100, selectmode="single") #define a function "returndata" to list the query result

for num in pydata:
    lb1.insert(END, num)
    lb1.place(x=250,y=150) #loop for entering the "data" into the listbox (lb1)

button = tk.Button(canvas,text="Get SQL Data",height=10,width=10,bg="Blue",fg="White",command=returndata)
button.pack(side="left") #create a button to enable user to get the data on click


tk.mainloop() #exit