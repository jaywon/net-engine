import man

def show_man_page(command):
    if command is None:
        return print("Specify command")

    print(man.pages[command]["description"])
