# utility functions that deal with the computer system running the program
from os import system, name

def clear_screen():
    """ Clears the terminal screen.

    Code taken from Geeks for Geeks website: 

    https://www.geeksforgeeks.org/clear-screen-python/ 

    """

    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else:
        _ = system('clear')

def flush_input():
    """ flushes input stream.

    Copied from Rosetta Code website:

    https://rosettacode.org/wiki/Keyboard_input/Flush_the_keyboard_buffer#Python

    """
    try:
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    except ImportError:
        import sys, termios
        termios.tcflush(sys.stdin, termios.TCIOFLUSH)