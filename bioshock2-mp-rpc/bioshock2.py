# Name: bioshock2.py
# A Bioshock 2 Local Information Extraction Layer.
# Meant for storing information about a player currently playing Multiplayer.

from utils import *


class Bioshock2:
    def __init__ (self, PLAYER, CHARACTER, PLASMID, WEAPON, MAP, SCREEN):
        self.PLAYER = PLAYER
        self.CHARACTER = CHARACTER
        self.PLASMID = PLASMID
        self.WEAPON = WEAPON
        self.MAP = MAP
        self.SCREEN = SCREEN

class Bio2MPAccess:

    BIOSHOCK2MP = {
        "Plasmids": ["Electro Bolt", "Incinterate", "Winter Blast", "Aero Dash", "Geyser Trap", "Telekinesis", "Houdini", "Insect Swarm"],
        "Weapons": ["Pistol", "Shotgun", "Machine Gun", "Grenade Launcher", "Crossbow", "Nail Gun", "Elephant Gun"],
        "Maps": ["Arcadia", "Farmer's Market", "Fort Frolic", "Hephaestus", "Home For The Poor", "Kashmir Restaurant", "Medical Pavilion", "Mercury Suites", "Neptune's Bounty","Point Prometheus"],
        "DLCMaps": ["Fontain Fisheries", "Pauper's Drop", "Smuggler's Hideout", "Fighting McDonagh's","Dionysus Park", "Siren Alley"],
        "Characters" : ["Jacob Norris", "Barbara Johnson", "Buck Raleigh", "Danny Wilkins", "Suresh Sheti", "Naledi Atkins", "Zigo d'Acosta", "Mlle Blanche de Glace", "Oscar Calraca", "Louie McGraff"]
    }

    def __init__ (self, PLASMID_CORDS, WEAPON_CORDS, MAP_CORDS, SCREEN_CORDS):
        self.PLASMID_CORDS = PLASMID_CORDS
        self.WEAPON_CORDS = WEAPON_CORDS
        self.MAP_CORDS = MAP_CORDS
        self.SCREEN_CORDS = SCREEN_CORDS


# Function check_if_active()
# This function checks if the Bioshock 2 Mutiplayer Process is open on the users System.
# Checks the directory of the currently Running Bioshock 2 Process and checks if either Singleplayer is Open or Multiplayer is Open.
def check_if_active():
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        if proc.info['name'] == APPLICATION_ID:
            directory = proc.info['exe']

            if "\\MP\\" in directory:
                return True
            
    return False

# Function check_if_priority()
# This function checks if the Bioshock 2 Mutiplayer Process is the Priority Application Open. AKA Current Opened Tab.
def check_if_priority():
    priority = False
    current_tab = gw.getActiveWindow()

    if current_tab is not None and current_tab.title == PROCESS_NAME:
        priority = True
        return priority

def get_current_screen():
    return None

def get_bioshock2_window():
    return gw.getWindowsWithTitle(PROCESS_NAME)[0]
