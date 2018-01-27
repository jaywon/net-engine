#import config
import man_pages


def list_machines():
    for machine in config.machines:
        print(machine)

def accept_input():
    command = input("$")

    splitted = command.split()
    first_arg = splitted[0]
    second_arg = splitted[1]
    if splitted[0] == "man":
        man_pages.show_man_page(splitted[1])

    if splitted[0] == "nmap":
        list_machines()

while True:
    accept_input()
