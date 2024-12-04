#! python3

import webbrowser, sys, pyperclip

sys.argv # tar i mot adresse du kan skrive inn rett i windows run

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
