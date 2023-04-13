# Checks the clipboard for email adressess and prints them to a .txt file.

import pyperclip, re

content = pyperclip.paste() # String

emailRegex = re.compile('\w+@\w+\.\w{1,4}\.?\w{2,4}?') # regex object for email addresses.

mo = emailRegex.findall(content)

# print(mo) # Pretty print as a numbered list of names.

# Checks for successful regex search:
if not mo:
    print("Zero emails detected in clipboard.")
    quit()
    
# Generates a text file in the local directory and appends the emails to it:
with open("emails.txt", "a") as file:
    num = 1
    for i in mo:
        print(str(num) + ") " + i)
        file.write(i + "\n")
        num += 1
    print("\n" + str(len(mo)) + " emails successfully added to emails.txt") 

