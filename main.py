import os #Importing the 'os' package to run os commands
import tkinter as tk #Importing tkinter with an alias 'tk'
from tkinter import * #Import all tkinter libraries
import subprocess #Import the 'subprocess' package, which allows us to store the data 

#Defining a function that collects data and stores it into a variable
def fetch():
    cmd="sensors | grep -iE 'vcore|volt|curr|in[0-9]'"
    data=subprocess.run(cmd,shell=True,capture_output=True,text=True)
    result=data.stdout
    output.config(text=result)
   
#Creating the window
app=tk.Tk()
app.title("AppforGreen")
app.geometry("900x900")
app.config(bg='light green')
label=tk.Label(app,text="Welcome to AppforGreen",font=('FantasqueSansM Nerd Font Propo',20))
label.pack(padx=20,pady=100)
label.config(bg='light green')
output=tk.Label(app,text="",font=('FantasqueSansM Nerd Font Propo',15))
output.pack(padx=20,pady=100)
output.config(bg='light green')
button=tk.Button(app,text="Check current load",font=('FantasqueSansM Nerd Font Propo',12),command=fetch)
button.pack()
button.config(bg='light blue')
app.mainloop()
