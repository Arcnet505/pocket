import cmd


class Crack(cmd.Cmd):
    intro = "Crack\n"
    prompt = "[crack]>>> "

    def do_woohoo(self, line):
        print("Woohoo this works")

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


def crackExec():
    Crack().cmdloop()
