import man
import copy

def show_man_page(command, lang):
    if command is None:
        print(copy.copy_text["MAN_SPECIFY"][lang])
        return

    if command not in man.pages:
        print(copy.copy_text["MAN_DNE"][lang])
        return

    print(man.pages[command]["description"][lang])
