import sys

from cmd2 import Cmd
from colorama import Fore, Back, Style

from pocket.utilities.frogs import getFrog
from pocket.categories.enum import forExec
from pocket.categories.shells import shellExec
from pocket.categories.privesc import priv_esc_exec

categories = [
    "   [" + Fore.RED + "enum" + Style.RESET_ALL + "]: Enumeration tools\n",
    "   [ " + Fore.BLUE + "shells" + Style.RESET_ALL +
    "  ]: Reverse Shell tools\n", "   [ " + Fore.GREEN + "privesc" +
    Style.RESET_ALL + " ]: Privilege Escalation tools\n"
]


def printIntro():
    intro = Fore.GREEN + getFrog() + Style.RESET_ALL + "\n"
    intro += " Tools: \n"
    for cat in categories:
        intro += cat

    intro += "\n"
    return intro


class Main(Cmd):
    intro = printIntro()
    prompt = "[" + Fore.YELLOW + "home" + Style.RESET_ALL + "] >>> "

    def do_enum(self, line):
        "Enumeration utilities"
        forExec()

    def do_shells(self, line):
        "Reverse shell tools"
        shellExec()

    def do_privesc(self, line):
        "Privilege Escalation tools"
        priv_esc_exec()

    def do_cmdi(self, line):
        "Command Injection utilities"
        cmdiExec()

    def do_sqli(self, line):
        "SQL Injection tools"
        sqliExec()

    def do_greet(self, line):
        "Gives a little greeting"
        print("Hello " + line)

    # def do_exit(self, line):
    #     "Exits the application"
    #     "Exit"
    #     return True

    # def do_EOF(self, line):
    #     "Exits the application"
    #     "Exit"
    #     return True

    def postloop(self):
        "Exiting message"
        print("Exiting pocket...\n")

    def emptyline(self):
        "Does nothing on emptyline"
        pass


if __name__ == '__main__':
    import sys
    sys.exit(Main().cmdloop())
