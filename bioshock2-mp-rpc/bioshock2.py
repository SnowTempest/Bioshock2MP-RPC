# Name: bioshock2.py
# A Bioshock 2 Local Information Extraction Layer.
# Meant for storing information about a player currently playing Multiplayer.

from utils import *

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
# 
def check_if_priority():
    priority = False
    current_tab = gw.getActiveWindow()

    if current_tab is not None and current_tab.title == PROCESS_NAME:
        priority = True
        return priority

def get_current_screen():

    # 675 675
    try:
        change_directory()
        priority = check_if_priority()

        while not priority:
            print("Waiting for Bioshock 2 to be the Current Tab...")
            time.sleep(3)
            priority = check_if_priority()

        if priority:
            print("Tab is Active")
            bioshock2_window = get_bioshock2_window()
            win_left, win_top, win_width, win_height = bioshock2_window.left, bioshock2_window.top, bioshock2_window.width, bioshock2_window.height
            screenshot = pyautogui.screenshot(region=(230, 173, 155, 30))
            screenshot.save("testscreen.png")

            test = Image.open("testscreen.png")
            text = pytesseract.image_to_string(test)

            test2 = Image.open("testscreen2.png")
            text2 = pytesseract.image_to_string(test2)

            test3 = Image.open("testscreen3.png")
            text3 = pytesseract.image_to_string(test3)

            test4 = Image.open("testscreen4.png")
            text4 = pytesseract.image_to_string(test4)

            test5 = Image.open("bioshock2-mp-rpc\\assets\\weapons\\pistol.png")
            text4 = pytesseract.image_to_string(test4)

            print("1" + text)
            print("2" + text2)
            print("3" + text3)
            print("4" + text4)
        else:
            print("game is not priority.")
    except IndexError:
        print("Window Not Found")

def get_bioshock2_window():
    return gw.getWindowsWithTitle(PROCESS_NAME)[0]
