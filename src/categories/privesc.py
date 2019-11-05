import cmd
from colorama import Fore, Back, Style
import subprocess


class PrivEsc(cmd.Cmd):
    intro = "Tools for Priviledge Escalation\n"
    prompt = "[" + Fore.YELLOW + "shells" + Style.RESET_ALL + "]>>> "

    def do_exit(self, line):
        "Exits back to main menu"
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


def privEscExec():
    PrivEsc().cmdloop()
