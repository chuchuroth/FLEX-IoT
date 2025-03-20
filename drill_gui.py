import tkinter as tk
from bluetooth import *  # PyBluez
import time

# Bluetooth setup (fake data for now—replace with real)
def get_drill_data():
    return 1500  # RPM placeholder—swap with HC-05 read

# GUI
root = tk.Tk()
root.title("FLEX Drill Tracker")
root.geometry("300x200")

label = tk.Label(root, text="Drill Status", font=("Arial", 16))
label.pack(pady=10)

rpm_display = tk.Label(root, text="RPM: 0", font=("Arial", 12))
rpm_display.pack()

health_display = tk.Label(root, text="Health: Good", font=("Arial", 12))
health_display.pack()

def update_gui():
    rpm = get_drill_data()
    rpm_display.config(text=f"RPM: {rpm}")
    if rpm < 1000:  # Fake threshold—tune later
        health_display.config(text="Health: Slow—Check Motor", fg="red")
    else:
        health_display.config(text="Health: Good", fg="green")
    root.after(1000, update_gui)  # Update every 1s

update_gui()
root.mainloop()
