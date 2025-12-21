import psutil
import shutil

def cpu_utilization():
    cpu = psutil.cpu_percent(interval=1)
    return cpu

def memory_utilization():
    memory = psutil.virtual_memory().percent
    return memory

def disk_utilization():
    total, used, free = shutil.disk_usage("/")
    disk = (used / total) * 100
    return disk

# Get thresholds from user

cpu_threshold = int(input("Enter CPU usage threshold (%): "))
memory_threshold = int(input("Enter Memory usage threshold (%): "))
disk_threshold = int(input("Enter Disk usage threshold (%): "))

def system_health_check():

    issues_found = False   # We will consider the system safe unless we find issues

    cpu = cpu_utilization()
    memory = memory_utilization()
    disk = disk_utilization()

    if cpu > cpu_threshold:
        print("CPU usage is above threshold, Current CPU utilization is", cpu)
        issues_found = True
    
    if memory > memory_threshold:
        print("Memory usage is above threshold, Current Memory utilization is", memory)
        issues_found = True

    if disk > disk_threshold:
        print("Disk usage is above threshold, Current Disk utilization is", disk)
        issues_found = True
        
    if not issues_found:    # If no issues were found, the system is safe
        print("You Are Safe")

# Call the function
system_health_check()