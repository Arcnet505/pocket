import cmd
from frogs import getFrog
from categories.forensics import forExec
from categories.web import webExec
from categories.crack import crackExec

categories = [
    "  [forensics]: Forensic tools such as nmap, ping, etc.\n"
    "  [  crack  ]: Cracking tools for cracking zips, hashes, etc.\n"
    "  [   web   ]: Web based tools for DNS spoofing, sql injection, etc.\n"
]


def printIntro():
    intro = getFrog() + "\n"
    intro += "Tools: \n"
    for cat in categories:
        intro += (cat)

    intro += "\n"
    return (intro)


class Main(cmd.Cmd):

    intro = printIntro()
    prompt = "[home]>>> "

    def do_forensics(self, line):
        forExec()

    def do_crack(self, line):
        crackExec()

    def do_web(self, line):
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
