from customtkinter import *
import random
import datetime
import time

class App(CTk):
    def __init__(self):
        super().__init__()

        self.title("AppforGreen")
        self.geometry("800x500")
        set_default_color_theme("green")

        # -------- Energy variables --------
        self.tariff = 6.5  # ₹ per kWh
        self.current_power = 0.0  # kW
        self.total_energy = 0.0  # kWh
        self.sample_interval = 5  # seconds
        self.last_sample_time = time.time()

        self.history = []

        # -------- Layout --------
        self.sidebar = CTkFrame(self, width=160)
        self.sidebar.pack(side="left", fill="y")

        self.main_area = CTkFrame(self)
        self.main_area.pack(side="right", fill="both", expand=True)

        CTkLabel(self.sidebar, text="AppforGreen", font=CTkFont(size=20, weight="bold")).pack(pady=20)

        CTkButton(self.sidebar, text="Dashboard", command=self.show_dashboard).pack(pady=10)
        CTkButton(self.sidebar, text="History", command=self.show_history).pack(pady=10)
        CTkButton(self.sidebar, text="Billing", command=self.show_billing).pack(pady=10)
        CTkButton(self.sidebar, text="Settings", command=self.show_settings).pack(pady=10)

        self.update_energy()
        self.show_dashboard()

    # -------- Energy update loop --------
    def update_energy(self):
        now = time.time()
        dt = now - self.last_sample_time

        if dt >= self.sample_interval:
            self.current_power = round(random.uniform(0.3, 2.5), 2)
            energy_added = self.current_power * (dt / 3600)
            self.total_energy += energy_added

            self.history.append({
                "time": datetime.datetime.now().strftime("%H:%M:%S"),
                "power": self.current_power,
                "energy": round(self.total_energy, 4)
            })

            self.last_sample_time = now

        self.after(1000, self.update_energy)

    def clear_main(self):
        for w in self.main_area.winfo_children():
            w.destroy()

    # -------- DASHBOARD --------
    def show_dashboard(self):
        self.clear_main()

        CTkLabel(self.main_area, text="Dashboard", font=CTkFont(size=22, weight="bold")).pack(pady=10)

        CTkLabel(self.main_area, text=f"Current Power: {self.current_power} kW").pack(pady=10)
        CTkLabel(self.main_area, text=f"Energy Used: {round(self.total_energy,4)} kWh").pack(pady=10)

        cost = round(self.total_energy * self.tariff, 2)
        CTkLabel(self.main_area, text=f"Estimated Cost: ₹{cost}").pack(pady=10)

    # -------- HISTORY --------
    def show_history(self):
        self.clear_main()

        CTkLabel(self.main_area, text="Usage History", font=CTkFont(size=22, weight="bold")).pack(pady=10)

        if not self.history:
            CTkLabel(self.main_area, text="No data yet").pack()
            return

        for record in self.history[-10:]:
            CTkLabel(
                self.main_area,
                text=f"{record['time']} | {record['power']} kW | {record['energy']} kWh"
            ).pack(anchor="w", padx=20)

    # -------- BILLING --------
    def show_billing(self):
        self.clear_main()

        CTkLabel(self.main_area, text="Billing", font=CTkFont(size=22, weight="bold")).pack(pady=10)

        bill = round(self.total_energy * self.tariff, 2)

        CTkLabel(self.main_area, text=f"Total Energy: {round(self.total_energy,4)} kWh").pack(pady=10)
        CTkLabel(self.main_area, text=f"Estimated Bill: ₹{bill}").pack(pady=10)

    # -------- SETTINGS --------
    def show_settings(self):
        self.clear_main()

        CTkLabel(self.main_area, text="Settings", font=CTkFont(size=22, weight="bold")).pack(pady=10)

        CTkLabel(self.main_area, text="Tariff (₹/kWh)").pack(pady=5)
        entry = CTkEntry(self.main_area)
        entry.insert(0, str(self.tariff))
        entry.pack(pady=5)

        def save():
            try:
                self.tariff = float(entry.get())
            except:
                pass

        CTkButton(self.main_area, text="Save", command=save).pack(pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
