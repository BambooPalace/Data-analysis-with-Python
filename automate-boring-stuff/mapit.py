import webbrowser, sys, pyperclip

sys.argv #['mapit.py','address2', 'address 2', 'st']

#check if command line arguments were passed

if len(sys.argv)>1:
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/Singapore+'+address)
