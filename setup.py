import json

def load_settings():
    try:
        with open('settings.json', 'r') as file:
            settings = json.load(file)

        return settings
    
    except FileNotFoundError:
        print("Settings file not found, using default settings.")
        return None
    
def save_settings(b1_key, b2_key, b1_pos, b2_pos):
    settings = {
        "button_keys": [
            {
                "button1_key": b1_key,
                "button2_key": b2_key
            }
        ],
        "positions": [
            {
                "button1_pos": b1_pos,
                "button2_pos": b2_pos
            }
        ]
    }

    with open('settings.json','w') as file:
        json.dump(settings, file, indent=4)

# def show_name():
#     print(
# '''  _  __     _                      
#  | |/ /__ _| |_ __ _ _ _  __ _     
#  | ' </ _` |  _/ _` | ' \/ _` |    
#  |_|\_\__,_|\__\__,_|_||_\__,_|    
#  / __|_ __ _(_) |_ __| |_  ___ _ _ 
#  \__ \ V  V / |  _/ _| ' \/ -_) '_|
#  |___/\_/\_/|_|\__\__|_||_\___|_|'''
#     )

def show_name():
    print(
'''
█▄▀ ▄▀█ ▀█▀ ▄▀█ █▄░█ ▄▀█
█░█ █▀█ ░█░ █▀█ █░▀█ █▀█

█▀ █░█░█ █ ▀█▀ █▀▀ █░█ █▀▀ █▀█
▄█ ▀▄▀▄▀ █ ░█░ █▄▄ █▀█ ██▄ █▀▄
'''

    )