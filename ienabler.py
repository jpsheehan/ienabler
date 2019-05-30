#!/usr/bin/env python3

# ienabler.py
# Written by JP Sheehan, 2019
# Licensed under the GNU GPLv3

# Allows the internet connection to be enabled on the Linux COSC machines via a
# terminal/ssh connection.
#
# Based on:
#   Python Internet Enabler for Linux version 0.042, 12-07-2013
#   Written by Steven Sykes with help from Graham Furniss

import telnetlib
import getpass


def connect(username, password, info):

    if info == "enable":
        choice = "1"
    else:
        choice = "2"

    tn = telnetlib.Telnet("ienabler.canterbury.ac.nz",  259)
    tn.read_until("User: ".encode())
    tn.write((username + "\n").encode())
    tn.read_until("password: ".encode())
    tn.write((password + "\n").encode())
    response = tn.expect(["choice".encode(), "denied".encode()],  5)
    if response[0] == 0:
        tn.write(choice.encode())
        return True
    else:
        return False


def main():

    print("Internet Enabler (http://github.com/jpsheehan/ienabler)")

    username = getpass.getuser()
    if username:
        print("Username: " + username)
    else:
        username = input("Username: ")
    password = getpass.getpass("Password: ")

    decision = input("[E]nable/[D]isable: ").lower()

    if decision == "e":
        info = "enable"
        status = "Internet connection established"
    elif decision == "d":
        info = "disable"
        status = "Internet connection deactivated"
    else:
        print("Cancelled")
        return

    if connect(username, password, info):
        print(status)
    else:
        print("Bad username or password provided")


if __name__ == "__main__":
    main()
