import psutil
import requests
import time

SERVER = "http://localhost:5000/log"

suspicious = ["mimikatz", "powershell -enc", "nc.exe"]

def check_processes():
    for proc in psutil.process_iter(['pid','name','cmdline']):
        try:
            cmd = " ".join(proc.info['cmdline'])
            for bad in suspicious:
                if bad in cmd.lower():
                    send_alert(proc.info)
        except:
            pass

def send_alert(proc):
    data = {
        "process": proc['name'],
        "pid": proc['pid'],
        "cmdline": str(proc['cmdline'])
    }
    requests.post(SERVER, json=data)

while True:
    check_processes()
    time.sleep(10)
