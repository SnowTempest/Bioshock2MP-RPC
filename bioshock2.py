
# Name: bioshock2.py
# A Bioshock 2 Local Information Extraction Layer.
# Meant for storing information about a player currently playing Multiplayer.

from utils import *


# Function check_if_active()
# This function checks if the Bioshock 2 Mutiplayer Process is open on the users System.
# Checks the directory of the currently Running Bioshock 2 Process and checks if either Singleplayer is Open or Multiplayer is Open.
def check_if_active():
    for proc in psutil.process_iter(['pid', 'name', 'exe']):
        if proc.info['name'] == "Bioshock2.exe":
            directory = proc.info['exe']

            if "\\MP\\" in directory:
                return True
            
    return False

