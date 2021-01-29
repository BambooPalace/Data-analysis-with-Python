#! python3
import re
import pyperclip

#todo: create a regex for phone number
#415-555-0000 ext 12345; ....

phoneRe = re.compile(r'''
((\d\d\d)|(\(\d\d\d\)))?	#(area code)
(\s|-)	#space or - as seperator
(\d\d\d)	#3 digits
-	#-
(\d\d\d\d)	#4 digits
(((ext(\.)?\s)|x)	#(extension-word)
 (\d{2,5}))?	#(ext-num)
''', re.VERBOSE)


#todo: create a regex for email address
#some.+_@xx.com

emailRe = re.compile(r'''
[a-zA-Z0-9_.+]+	#name 1 or more digits
@	#@
[a-zA-Z0-9_.+]+\.com	#domain
''', re.VERBOSE)

ntuEmailRe = re.compile(r'[a-zA-Z0-9]+@e\.ntu\.edu\.sg')
matricRe = re.compile(r'G\d{7}[A-Z]')

#todo: get text from clipboard
#MSAI Master project info

text = pyperclip.paste()

#todo: extract the emai/phone from the text

extractPhone = phoneRe.findall(text)
extractEmail = ntuEmailRe.findall(text)
extractMatric = matricRe.findall(text)
print('\n'.join(extractPhone))
print('\n'.join(extractEmail))
print('\n'.join(extractMatric))

#todo: copy the extracted info to the clipboard


