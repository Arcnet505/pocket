import cmd


class Web(cmd.Cmd):
    intro = "Web\n"
    prompt = "[web]>>> "

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


def webExec():
    Web().cmdloop()
