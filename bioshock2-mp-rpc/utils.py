#Related Imports
import pyautogui
import psutil
import pypresence, os, re, time, sys
import pytesseract
import pygetwindow as gw
from PIL import Image
from dotenv import load_dotenv

APPLICATION_ID = "Bioshock2.exe"
PROCESS_NAME = "BioShock 2"

# Function change_directory()
# Changes the current working directory to be where the executable / Script is located.
# The script directory only matters for my end.
def change_directory():
    if sys.argv[0].endswith('.exe'):
        dir = os.path.dirname(os.path.abspath(sys.executable))
    else:
        dir = os.path.dirname(os.path.abspath(__file__))

    os.chdir(dir)

# Function get_directory()
# Gets the current working directory to be where the executable / Script is located.
# The script directory only matters for my end.
def get_directory():
    if sys.argv[0].endswith('.exe'):
        dir = os.path.dirname(os.path.abspath(sys.executable))
    else:
        dir = os.path.dirname(os.path.abspath(__file__))
    
    return dir

# Locate the Tesseract Executable
file_directory = get_directory()
tesseract_path =  os.path.join(file_directory, 'Tesseract', 'tesseract.exe')
pytesseract.pytesseract.tesseract_cmd = tesseract_path