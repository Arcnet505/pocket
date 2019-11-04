import cmd
from frogs import getFrog


class main(cmd.Cmd):

    intro = getFrog()
    prompt = ">>> "

    def do_greet(self, line):
        "Gives a little greeting"
        print("hello")

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
        print("Exiting.....\n")

    def emptyline(self):
        "Does nothing on emptyline"
        pass


if __name__ == '__main__':
    main().cmdloop()
