__author__ = "SnowTempest"
__copyright__ = "Copyright (C) 2022 SnowTempest"
__license__ = "GNU GENERAL PUBLIC LICENSE"
__version__= "1.0"


from utils import *
from bioshock2 import *

def start():
    print("*****************************************************************************")
    print(" \nBioshock 2 Multiplayer Discord RPC by SnowTempest (ADTempest on YT/Twitch)\n")
    print("*****************************************************************************")

    print("\nYou Can Close the Program at Any Time Using Ctrl + C.\n")

    print("\nWaiting for Multiplayer To Be Open and Current Tab...")

    active = check_if_active()
    priority = check_if_priority()

    try:
        while not active or not priority:
            active = check_if_active()
            priority = check_if_priority()

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