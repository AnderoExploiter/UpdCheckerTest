#imports
import time
import os
#start screen
os.system("cls")
print("                                    Made by Tim")
print("")
print("                                 Created on Python")
print("")
time.sleep(3)
#clearing console
os.system("cls")
def check_password_in_txt(file_path, password):

    with open(file_path, 'r', encoding='utf-8') as file:
        full_text = file.read()

    if password in full_text:
        return True
    else:
        return False

file_path = 'megasploit_password.txt'
password = 'MegaSploit'
if check_password_in_txt(file_path, password):
    os.system("cls")
    print("Password is correct!")
    print("")
    print("Launching...")
    time.sleep(5)
    os.system("cls")
    os.chdir("bin")
    os.system("python __init__.py")
else:                 
    os.system("cls")
    print("Invalid password")