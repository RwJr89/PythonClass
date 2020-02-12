# Programmer: Rawle Williams
# Date: 2/11/2020
# File name: wifi_diagnostics_tree_williams.py

# Pseudocode:
# WiFi diagnostics tree

# Wifi walkthrough fix
rebootPc = input(
    "Reboot the computer and try to connect. \nDid that fix the problem?:").strip().lower()
if rebootPc == "yes":
    print("Glad to be of help.")

# Reboot router
else:
    routerReboot = input(
        "Reboot the router and try to connect. \nDid that fix the problem?: ").strip().lower()
    if routerReboot == "yes":
        print("Glad to be of help.")

# Cable check
    else:
        cableCheck = input(
            "Make sure the cables between the router and modem are plugged in firmly. \nDid that fix the problem?:").strip().lower()
        if cableCheck == "yes":
            print("Glad to be of help.")

# Move location of router
        else:
            routerMove = input(
                "Move the router to a new location and try to connect. \nDid that fix the problem?").strip().lower()
            if routerMove == "yes":
                print("Glade to be of help.")
            else:
                print("Get a new router.")
