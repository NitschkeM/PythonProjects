#! python3
# mapIt.py - Launches a map in the browser
# using an address from the command line or clipboard.

import webbrowser, sys, pyperclip

def addressWasPassedAsCommandLineArgument():
    return len(sys.argv) > 1


if addressWasPassedAsCommandLineArgument():
    # Using join to turn a list of strings into a single string
    # using argv[1:] to exclude/chop-off first element of the array.
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)