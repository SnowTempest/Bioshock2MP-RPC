__author__ = "SnowTempest"
__copyright__ = "Copyright (C) 2022 SnowTempest"
__license__ = "NONE"
__version__= "1.0"


from utils import *
from bioshock2 import *

pytesseract.pytesseract.tesseract_cmd = 'bioshock2-mp-rpc\\Tesseract\\tesseract.exe'  # your path may be different


def start():
    print("*****************************************************************************")
    print(" \nBioshock 2 Multiplayer Discord RPC by SnowTempest (ADTempest on YT/Twitch)\n")
    print("*****************************************************************************")

    print("\nYou Can Close the Program at Any Time Using Ctrl + C.\n")

    print("\nChecking if Multiplayer is Active...")

    active = check_if_active()

    try:
        while not active:
            print("\nMultiplayer Is Not Active. Please Open Bioshock 2 Multiplayer and Try Again.")
            input("Press Any Key To Check Again...")
            active = check_if_active()
    except KeyboardInterrupt:
        error_handler("User Has Chosen To Close.", True)

    

# Function print_error()
# param error = The error message to be printed.
# param close = A flag which indicates if the error should cause the program to close for safety.
def error_handler(error, close):
    print("\nError: " + error)
    if close:
        input("\nPress Any Key To Exit...")
        sys.exit()


# Function: main()
# The main function of the program.
def main():
    start()


# Safe Function Calling.
if __name__ == "__main__":
    main()