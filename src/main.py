import cmd
from frogs import getFrog
from categories.forensics import forExec

class Main(cmd.Cmd):

    intro = getFrog()
    prompt = "[home]>>> "

    def do_forensics(self, line):
        forExec()

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
