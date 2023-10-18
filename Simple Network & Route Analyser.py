import tkinter as tk
from tkinter import messagebox
import subprocess

def validate_host(host):
    # Check if the host is in the format "www.website.com"
    if not host.startswith("www.") or not host.endswith(".com"):
        messagebox.showerror("Invalid Host", "Please enter a valid host in the format www.website.com")
        return False
    return True

def run_ping():
    host = ping_entry.get()
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    messagebox.showinfo("Ping Result", result.stdout)

def run_traceroute():
    host = traceroute_entry.get()
    result = subprocess.run(['tracert', host], capture_output=True, text=True)
    messagebox.showinfo("Traceroute Result", result.stdout)

def check_nic():
    result = subprocess.run(['ping', '-n', '1', '127.0.0.1'], capture_output=True, text=True)
    if "Reply" in result.stdout:
        nic_window = tk.Toplevel(analyser)
        nic_window.title("NIC Check")
        nic_window.geometry("300x100")  # Adjust size as needed
        message_label = tk.Label(nic_window, text="No Hardware problem detected")
        message_label.pack(pady=20)

    else:
        nic_window = tk.Toplevel(analyser)
        nic_window.title("NIC Check")
        nic_window.geometry("300x100")  # Adjust size as needed
        message_label = tk.Label(nic_window, text="Hardware problem detected, check your NIC")
        message_label.pack(pady=20)

# Create main window
analyser = tk.Tk()
analyser.title("Network Diagnostics Tool")
analyser.geometry("300x300")  # Set the dimensions here

# Ping Section
ping_label = tk.Label(analyser, text="Enter host for Ping:")
ping_label.pack()
ping_entry = tk.Entry(analyser)
ping_entry.pack()
ping_button = tk.Button(analyser, text="Run Ping", command=run_ping)
ping_button.pack()

# Traceroute Section
traceroute_label = tk.Label(analyser, text="Enter host for Traceroute:")
traceroute_label.pack()
traceroute_entry = tk.Entry(analyser)
traceroute_entry.pack()
traceroute_button = tk.Button(analyser, text="Run Traceroute", command=run_traceroute)
traceroute_button.pack()

spacer = tk.Label(analyser, text="")
spacer.pack()
nic_button = tk.Button(analyser, text="Check NIC", command=check_nic)
nic_button.pack()

# Start the main event loop
analyser.mainloop()