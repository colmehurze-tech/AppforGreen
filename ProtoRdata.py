from customtkinter import *
from PIL import Image
import os
import subprocess
import platform
import random


class App(CTk):

    # DATA FETCH FUNCTION 
    def fetch(self):
        system = platform.system()

        # For LINUX MODE (real sensor data) 
        if system == "Linux":
            try:
                cmd = "sensors | grep -iE 'vcore|volt|curr|in[0-9]'"
                data = subprocess.run(
                    cmd, shell=True, capture_output=True, text=True
                )
                result = data.stdout if data.stdout else "No sensor data detected."
            except Exception as e:
                result = f"Error fetching data:\n{e}"

        # For WINDOWS MODE (simulated data) 
        else:
            voltage = random.randint(220, 240)
            current = round(random.uniform(2.0, 6.0), 2)
            power = round(voltage * current, 2)
            cost = round(power * 0.008, 2)  # simulated ₹ cost
            co2 = round(power * 0.0007, 2)  # simulated CO₂ kg

            result = (
                "⚡ Simulated Energy Data (Prototype Mode)\n\n"
                f"Voltage      : {voltage} V\n"
                f"Current      : {current} A\n"
                f"Power Usage  : {power} W\n"
                f"Est. Cost    : ₹ {cost}\n"
                f"CO₂ Impact   : {co2} kg"
            )

        self.LABEL_FRAME2.configure(text=result)

    # GUI SETUP 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # FRAME 0 : WELCOME 
        self.frame0 = CTkFrame(master=self, fg_color="transparent")
        self.frame0.pack(pady=(48, 0), fill="both", expand=True)

        self.LABEL1 = CTkLabel(
            master=self.frame0,
            font=CTkFont(size=22, weight="bold"),
            text="Welcome to AppforGreen"
        )
        self.LABEL1.pack(pady=(20, 0))

        self.LABEL4 = CTkLabel(
            master=self.frame0,
            font=CTkFont(size=15),
            text="Track electricity usage & promote sustainable living"
        )
        self.LABEL4.pack(pady=(40, 0))

        self.BUTTON3 = CTkButton(
            master=self.frame0,
            text="Next →",
            width=140,
            height=38,
            corner_radius=20,
            command=self.show_frame1
        )
        self.BUTTON3.pack(pady=(50, 0))

        # FRAME 1 : DATA 
        self.frame1 = CTkFrame(master=self, fg_color="transparent")

        self.LABEL_FRAME1 = CTkLabel(
            master=self.frame1,
            font=CTkFont(size=18),
            text="Click below to check energy stats"
        )
        self.LABEL_FRAME1.pack(pady=(40, 0))

        self.LABEL_FRAME2 = CTkLabel(
            master=self.frame1,
            text="No data",
            wraplength=420,
            justify="left",
            height=180,
            corner_radius=20,
            padx=12,
            pady=12
        )
        self.LABEL_FRAME2.pack(pady=(30, 0))

        self.CHECK_BUTTON = CTkButton(
            master=self.frame1,
            text="Check",
            width=140,
            height=38,
            corner_radius=20,
            command=self.fetch
        )
        self.CHECK_BUTTON.pack(pady=(30, 0))

        self.BACK_BUTTON = CTkButton(
            master=self.frame1,
            text="← Back",
            width=140,
            height=38,
            corner_radius=20,
            command=self.show_frame0
        )
        self.BACK_BUTTON.pack(pady=(40, 0))

    # FRAME SWITCHING 
    def show_frame0(self):
        self.frame1.pack_forget()
        self.frame0.pack(pady=(48, 0), fill="both", expand=True)

    def show_frame1(self):
        self.frame0.pack_forget()
        self.frame1.pack(pady=(48, 0), fill="both", expand=True)


# MAIN WINDOW 
set_default_color_theme("green")
root = App()
root.geometry("500x520")
root.title("AppforGreen")
root.mainloop()
