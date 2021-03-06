from cmd2 import Cmd
from colorama import Fore, Back, Style


class Enumeration(Cmd):
    intro = "Forensics\n"
    prompt = "[" + Fore.YELLOW + "forensics" + Style.RESET_ALL + "]>>> "

    def do_woohoo(self, line):
        print("Woohoo this works")

    def do_exit(self, line):
        "Exits back to main menu"
        return True

    def do_back(self, line):
        "Returns back to previous prompt"
        return True

    def do_EOF(self, line):
        "Exits the application"
        return True

    def postloop(self):
        "Exiting message"
        print("Exiting back to main menu...\n")

    def emptyline(self):
        "Does nothing on emptyline"
        pass


def forExec():
    Enumeration().cmdloop()
