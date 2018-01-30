#!/usr/bin/env python

import config
import copy
import man_pages
import signal
import sys

LANGUAGES_SUPPORTED = ["en", "es"]
LANGUAGE_SELECTION = "en"
CURRENT_IP = next(iter(config.machines))
CURRENT_MACHINE_CONFIG = {}
CMDS = {
    "man": {
        "num_params": 1,
        "run": lambda arg: man_pages.show_man_page(arg, LANGUAGE_SELECTION)
    },
    "ssh": {
        "num_params": 1,
        "run": lambda arg: ssh(arg)
    },
    "nmap": {
        "num_params": 0,
        "run": lambda arg: nmap()
    },
    "tools": {
        "num_params": 0,
        "run": lambda arg: list_tools()
    },
    "ifconfig": {
        "num_params": 0,
        "run": lambda arg: ip_config()
    },
    "users": {
        "num_params": 0,
        "run": lambda arg: list_users()
    },
    "groups": {
        "num_params": 0,
        "run": lambda arg: list_groups()
    },
    "history": {
        "num_params": 0,
        "run": lambda arg: show_history()
    },
    "language": {
        "num_params": 0,
        "run": lambda arg: set_language()
    },
    "exit": {
        "num_params": 0,
        "run": lambda arg: exit()
    }
}

def signal_handler(signal, frame):
    exit()

def exit():
    print("\nBuh bye....")
    sys.exit(0)

def get_current_machine_config():
    current_machine = config.machines[CURRENT_IP]
    return current_machine

def is_supported_language(lang):
    global LANGUAGES_SUPPORTED
    return lang is not None and lang in LANGUAGES_SUPPORTED

def set_language():
    global LANGUAGE_SELECTION
    language = None
    # validate input
    while not is_supported_language(language):
        language = input(copy.copy_text["LANGUAGE_CHOICE"][LANGUAGE_SELECTION] + " ")
        if not is_supported_language(language):
            print(copy.copy_text["LANGUAGE_UNSUPPORTED"][LANGUAGE_SELECTION])

    LANGUAGE_SELECTION = language
    print(copy.copy_text["LANGUAGE_CHANGED"][LANGUAGE_SELECTION])

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
        print(copy.copy_text["INVALID_IP"][LANGUAGE_SELECTION])
    else:
        CURRENT_IP = ip_address

def process_command(command, argument):
    global CMDS
    if command not in CMDS.keys():
        print(copy.copy_text["INVALID_CMD"][LANGUAGE_SELECTION])
    elif CMDS[command]["num_params"] > 0 and not argument:
        print(copy.copy_text["INVALID_PARAM_NUM"][LANGUAGE_SELECTION])
    else:
        CMDS[command]["run"](argument)

def input_loop():
    #print(copy.copy_text["SELECT_TOOL"][LANGUAGE_SELECTION] + ": ")
    user_input = input("user@" + CURRENT_IP + ":~$ ")

    parsed_input = user_input.split()
    command = parsed_input[0]

    if len(parsed_input) > 0:
        if len(parsed_input) > 1:
            argument  = parsed_input[1]
        else:
            argument = None

        process_command(command, argument)
    else:
        print(copy.copy_text["INVALID_PARAM_NUM"][LANGUAGE_SELECTION])
        return


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    lang = None
    while not is_supported_language(lang):
        lang = input("Select your language: ")
        if not is_supported_language(lang):
            print("We're sorry, your choice is currently unavailable.")

    LANGUAGE_SELECTION = lang

    while True:
        input_loop()
