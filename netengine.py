#!/usr/bin/env python

import config
import copy
import man_pages
import signal
import sys

LANGUAGE_SELECTION = "en"
CURRENT_IP = next(iter(config.machines))
CURRENT_MACHINE_CONFIG = {}

def signal_handler(signal, frame):
    exit()

def exit():
    print("\nBuh bye....")
    sys.exit(0)

def get_current_machine_config():
    current_machine = config.machines[CURRENT_IP]
    return current_machine

def set_language():
    global LANGUAGE_SELECTION
    language = input("What language would you like to use?")
    # validate input
    LANGUAGE_SELECTION = language

def ip_config():
    print(CURRENT_IP)

def list_tools():
    current_machine = get_current_machine_config()
    for command in current_machine["commands"].keys():
        print(command)

def list_users():
    current_machine = get_current_machine_config()
    for user in current_machine["users"]:
        print(user["username"])

def list_groups():
    current_machine = get_current_machine_config()
    for group in current_machine["groups"]:
        print(group)

def show_history():
    current_machine = get_current_machine_config()
    for entry in current_machine["history"]:
        print(entry)

def nmap():
    current_machine = get_current_machine_config()
    firewall_rules = current_machine["firewall_rules"]
    for egress_deny in firewall_rules["egress"]["deny"]:
        if egress_deny["port"] == "*":
            print(copy.copy_text["FIREWALL_RULE_VIOLATION"][LANGUAGE_SELECTION] + ": ")
            return

    for machine in config.machines:
        print(machine)

def ssh(ip_address):
    global CURRENT_IP
    if not ip_address in config.machines:
        print("Not a valid IP address")
    else:
        CURRENT_IP = ip_address

def process_command(command, argument):

    if command == "man":
        if not command or not argument:
            print("Invalid number of inputs")
            return
        man_pages.show_man_page(argument, LANGUAGE_SELECTION)
    elif command == "nmap":
        nmap()
    elif command == "tools":
        list_tools()
    elif command == "ssh":
        if not command or not argument:
            print("Invalid number of inputs")
            return
        ssh(argument)
    elif command == "ifconfig":
        ip_config()
    elif command == "users":
        list_users()
    elif command == "groups":
        list_groups()
    elif command == "history":
        show_history()
    elif command == "language":
        set_language()
    elif command == "exit":
        exit()
    else:
        print("Not a valid command, please try again")

def input_loop():
    #print(copy.copy_text["SELECT_TOOL"][LANGUAGE_SELECTION] + ": ")
    user_input = input("user@" + CURRENT_IP + ":~$")

    parsed_input = user_input.split()
    command = parsed_input[0]

    if len(parsed_input) > 0:
        if len(parsed_input) > 1:
            argument  = parsed_input[1]
        else:
            argument = None

        process_command(command, argument)
    else:
        print("Invalid number of inputs")
        return


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    LANGUAGE_SELECTION = input("Select your language: ")

    while True:
        input_loop()
