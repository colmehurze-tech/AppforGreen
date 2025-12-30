from customtkinter import *
from PIL import Image #In case we want to use an image logo
import os #Importing the 'os' package to run os commands
import subprocess #Import the 'subprocess' package, which allows us to store the data 

class App(CTk):
    #Defining a function that collects data and stores it into a variable
    def fetch(self):
        cmd="sensors | grep -iE 'vcore|volt|curr|in[0-9]'"
        data=subprocess.run(cmd,shell=True,capture_output=True,text=True)
        result=data.stdout
        self.LABEL_FRAME2.configure(text=result)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # --- Frame 0: The initial screen ---
        # Storing frames as instance attributes (self.frame0, self.frame1)
        # makes them accessible throughout the class methods.
        self.frame0 = CTkFrame(master=self, fg_color="transparent", bg_color="transparent")
        # Initially pack FRAME0 so it's visible when the app starts.
        # Using fill="both" and expand=True allows the frame to resize with the window.
        self.frame0.pack(pady=(48, 0), fill="both", expand=True) 

        self.LABEL1 = CTkLabel(master=self.frame0, font=CTkFont(family="FantasqueSansM Nerd Font Propo", size=21), text="Welcome to AppforGreen")
        self.LABEL1.pack(pady=(20,0)) # Added some padding for better initial layout

        self.LABEL4 = CTkLabel(master=self.frame0, font=CTkFont(size=15, weight="normal", family="FantasqueSansM Nerd Font Propo"), text="An app that helps you keep track of your electricity usage")
        self.LABEL4.pack(pady=(50, 0)) # Adjusted padding for better spacing

        self.BUTTON3 = CTkButton(master=self.frame0, font=CTkFont(size=16, weight="normal", family="FantasqueSansM Nerd Font Propo"), text="Next →", width=140, height=38, corner_radius=20, fg_color=['#797979', '#000000'], hover_color=['#4e4e4e', '#434343'], border_color=['#000000', '#a2a2a2'], border_width=3, command=self.show_frame1)
        self.BUTTON3.pack(pady=(50, 0)) # Adjusted padding to place the button nicely

        # --- Frame 1: The new screen ---
        self.frame1 = CTkFrame(master=self, fg_color="transparent", bg_color="transparent")

        self.LABEL_FRAME1 = CTkLabel(master=self.frame1, font=CTkFont(family="FantasqueSansM Nerd Font Propo", size=21), text="Click the button below to check stats")
        self.LABEL_FRAME1.pack(pady=(50, 0)) # Padding for the label within the new frame 

        self.LABEL_FRAME2 = CTkLabel(master=self.frame1,font=CTkFont(family="FantasqueSansM Nerd Font Propo", size=21), text="No data",text_color="blue",fg_color=['pink', 'pink'],corner_radius=20, wraplength=400,justify="left",height=150,padx=10,pady=10)
        self.LABEL_FRAME2.pack(pady=(50, 0)) # Padding for the label within the new frame 

        self.CHECK_BUTTON = CTkButton(master=self.frame1, font=CTkFont(size=16, weight="normal", family="FantasqueSansM Nerd Font Propo"), text="Check",text_color="dark orange", width=140, height=38, corner_radius=20, fg_color=['#797979', '#000000'], hover_color=['#49F012', '#38E744'], border_color=['#000000', '#a2a2a2'], border_width=3, command=self.fetch)
        self.CHECK_BUTTON.pack(pady=(50, 0)) # Padding for the back button

        # Add a "Back" button to FRAME1 to navigate back to FRAME0
        self.BACK_BUTTON = CTkButton(master=self.frame1, font=CTkFont(size=16, weight="normal", family="FantasqueSansM Nerd Font Propo"), text="← Back", width=140, height=38, corner_radius=20, fg_color=['#797979', '#000000'], hover_color=['#4e4e4e', '#434343'], border_color=['#000000', '#a2a2a2'], border_width=3, command=self.show_frame0)
        self.BACK_BUTTON.pack(pady=(100, 0)) # Padding for the back button


    def show_frame0(self):
        self.frame1.pack_forget() # Hide the second frame
        self.frame0.pack(pady=(48, 0), fill="both", expand=True) # Show the first frame

    def show_frame1(self):
        self.frame0.pack_forget() # Hide the first frame
        self.frame1.pack(pady=(48, 0), fill="both", expand=True) # Show the second frame


#Main Window Setup
set_default_color_theme("green")
root = App()
root.geometry("500x500")
root.title("AppforGreen")
root.configure(fg_color=['gray92', 'gray14']) 
root.mainloop()
