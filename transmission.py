import config
import copy
import man_pages
import signal
import sys

LANGUAGE_SELECTION = "en"
CURRENT_IP = next(iter(config.machines))

def signal_handler(signal, frame):
    exit()

def exit():
    print("\nBuh bye....")
    sys.exit(0)

def ip_config():
    print(CURRENT_IP)

def list_tools():
    current_machine = config.machines[CURRENT_IP]
    for command in current_machine["commands"].keys():
        print(command)

def list_users():
    current_machine = config.machines[CURRENT_IP]
    for user in current_machine["users"]:
        print(user["username"])

def show_history():
    current_machine = config.machines[CURRENT_IP]
    for entry in current_machine["history"]:
        print(entry)

def nmap():
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
        man_pages.show_man_page(argument)
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
    elif command == "history":
        show_history()
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
