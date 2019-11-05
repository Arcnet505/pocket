import cmd
from utilities.frogs import getFrog
from categories.forensics import forExec
from categories.web import webExec
from categories.crack import crackExec
from categories.shells import shellExec
from colorama import Fore, Back, Style

categories = [
    "   [" + Fore.RED + "forensics" + Style.RESET_ALL +
    "]: Forensic tools such as nmap, ping, etc.\n"
    "   [  " + Fore.RED + "crack" + Style.RESET_ALL +
    "  ]: Cracking tools for cracking zips, hashes, etc.\n"
    "   [   " + Fore.RED + "web" + Style.RESET_ALL +
    "   ]: Web based tools for DNS spoofing, sql injection, etc.\n"
]


def printIntro():
    intro = ""

    intro += Fore.GREEN + getFrog() + Style.RESET_ALL + "\n"
    intro += " Tools: \n"
    for cat in categories:
        intro += (cat)

    intro += "\n"
    return (intro)


class Main(cmd.Cmd):

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
        privEscExec()

    def do_cmdi(self, line):
        "Command Injection utilities"

    def do_sqli(self, line):
        "SQL Injection tools"

    def do_crack(self, line):
        "Cracking utilities"
        crackExec()

    def do_web(self, line):
        "Web based utilities"
        webExec()

    def do_greet(self, line):
        "Gives a little greeting"
        print("Hello " + line)

    def do_exit(self, line):
        "Exits the application"
        "Exit"
        return True

    def do_EOF(self, line):
        "Exits the application"
        "Exit"
        return True

    def postloop(self):
        "Exiting message"
        print("Exiting pocket...\n")

    def emptyline(self):
        "Does nothing on emptyline"
        pass


if __name__ == '__main__':
    Main().cmdloop()
