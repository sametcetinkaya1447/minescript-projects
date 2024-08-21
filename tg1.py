import minescript as ms # type: ignore
import time
import random
print("§cTriggerbot is running")
def hit():
    ms.player_press_attack(pressed=True)
    ms.player_press_attack(pressed=False)
last_hit_time = 0

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
    
