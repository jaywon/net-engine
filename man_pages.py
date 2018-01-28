import man

def show_man_page(command):
    if command is None:
        print("Specify command")
        return

    if command not in man.pages:
        print("No man page exists for this command")
        return

    print(man.pages[command]["description"])
