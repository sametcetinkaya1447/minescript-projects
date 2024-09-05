import os
import urllib.request

# URLs of the files to download
mod_url = "https://github.com/sametcetinkaya1447/minescript-projects/raw/main/mod.jar"
json_files = {
    "general.json5": "https://github.com/sametcetinkaya1447/minescript-projects/raw/main/general.json5",
    "friends.json5": "https://github.com/sametcetinkaya1447/minescript-projects/raw/main/friends.json5"
}

# Define the target directories in %appdata%
mods_folder_path = os.path.join(os.getenv('APPDATA'), '.minecraft', 'mods')
config_folder_path = os.path.join(os.getenv('APPDATA'), '.minecraft', 'config', 'remote_player_waypoints_for_xaero')

# Ensure the mods and config directories exist
os.makedirs(mods_folder_path, exist_ok=True)
os.makedirs(config_folder_path, exist_ok=True)

# Download the mod file and save it to the mods folder
mod_path = os.path.join(mods_folder_path, 'mod.jar')
urllib.request.urlretrieve(mod_url, mod_path)
print(f"Mod indirildi ve kaydedildi")

# Download each JSON file and save it to the config folder
for filename, url in json_files.items():
    file_path = os.path.join(config_folder_path, filename)
    urllib.request.urlretrieve(url, file_path)
    (print(f"Ayarlar ve kaydedildi"))
