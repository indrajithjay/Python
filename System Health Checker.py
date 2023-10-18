import tkinter as tk
import psutil

# Define threshold values
CPU_THRESHOLD = 80  # 80% CPU usage
MEMORY_THRESHOLD = 80  # 80% memory usage
DISK_THRESHOLD = 80  # 80% disk usage

# Function to update labels with current system stats
def update_stats():
    cpu_percent = psutil.cpu_percent(interval=1)
    memory_percent = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent

    cpu_label.config(text=f'CPU Usage: {cpu_percent}%')
    memory_label.config(text=f'Memory Usage: {memory_percent}%')
    disk_label.config(text=f'Disk Usage: {disk_percent}%')

    if cpu_percent > CPU_THRESHOLD:
        alert_label.config(text='ALERT: High CPU Usage!', fg='red')
    elif memory_percent > MEMORY_THRESHOLD:
        alert_label.config(text='ALERT: High Memory Usage!', fg='red')
    elif disk_percent > DISK_THRESHOLD:
        alert_label.config(text='ALERT: High Disk Usage!', fg='red')
    else:
        alert_label.config(text='', fg='black')

    root.after(1000, update_stats)

# Create GUI
root = tk.Tk()
root.title('System Monitoring Script')

cpu_label = tk.Label(root, font=('Arial', 14))
memory_label = tk.Label(root, font=('Arial', 14))
disk_label = tk.Label(root, font=('Arial', 14))
alert_label = tk.Label(root, font=('Arial', 14))

cpu_label.pack(pady=10)
memory_label.pack(pady=10)
disk_label.pack(pady=10)
alert_label.pack(pady=10)

update_stats()

root.mainloop()
