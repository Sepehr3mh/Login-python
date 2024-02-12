import os
import platform
import geocoder
import getpass
from datetime import datetime
from colorama import Fore as c

def get_os_info():
    system = platform.system()
    if system == "Darwin":
        return "macOS"
    elif system == "Windows":
        return "Windows"
    elif system == "Linux":
        return "Linux"
    else:
        return "Unknown"

def get_location():
    try:
        g = geocoder.ip('me')
        if g.city and g.country:
            return f"{g.city}, {g.country}"
        else:
            return "Location not available"
    except:
        return "Location not available"

def save_login_attempt(username, password, name, os_info, location, success):
    with open("login_details.txt", "a") as file:
        current_time = datetime.now().strftime("%Y-%m-%d  | %I:%M:%S %p")
        file.write(f"Date/Time: {current_time}\n")
        file.write(f"User Name: {name}\n")
        file.write(f"Username Entered: {username}\n")
        file.write(f"Password Entered: {password}\n")
        file.write(f"OS: {os_info}\n")
        file.write(f"Location: {location}\n")
        file.write(f"Login Success: {success}\n")
        file.write("====================================\n")

def login():
    os.system("clear" if os.name == 'posix' else "cls")
    username = "python" # Username to login
    password = "cl52" # Password to login
    name = input(f"{c.LIGHTCYAN_EX}what is your name? {c.YELLOW}")

    user_input = input(f"{c.LIGHTGREEN_EX}username : {c.LIGHTRED_EX}")
    pass_input = input(f"{c.LIGHTGREEN_EX}password : {c.LIGHTRED_EX}")
    # pass_input = getpass.getpass(f"{c.LIGHTGREEN_EX}password : {c.LIGHTRED_EX}") # If you want the password not to be visible when writing the password, remove this part from the comment.
    print(f"{c.RESET}")

    os_info = get_os_info()
    location = get_location()
    success = False

    if (user_input == username) and (pass_input == password):
        print(f"{c.GREEN}Welcome{c.LIGHTMAGENTA_EX} {name}")
        success = True
        print(f"{c.RESET}")
    else:
        print(f"{c.RED}The info is not correct")
        print(f"{c.RESET}")

    save_login_attempt(user_input, pass_input, name, os_info, location, success)

login()