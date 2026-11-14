#readsites.py -read websites from sites.txt and print them 
import subprocess
import sys
import requests
down_count=0
up_count=0
try:

    with open("sites.txt") as f:
        for line in f:
            site =line.strip()
            if site == "":
                continue
            try:
                response = requests.get(f"https://{site}", timeout=5)
                if response.status_code < 400:
                    print(f"{site}  is UP ({response.status_code})")
                    up_count +=1
                else:
                    down_count +=1
                    print(f"{site} is DOWN ({response.status_code})")
            except requests.exceptions.RequestException:
                down_count +=1
                print(f"{site} is DOWN (could not connect)")
except FileNotFoundError:
    print("sites.txt not found")
    sys.exit(2)
print(up_count, ":UP",down_count, ":Down")
if down_count >0:
    sys.exit(1)
sys.exit(0)    
