import cmd
from colorama import Fore, Back, Style
import subprocess
import http.server
import socketserver


class Shells(cmd.Cmd):
    intro = "Common Tools for Reverse Shells\n"
    prompt = "[" + Fore.YELLOW + "shells" + Style.RESET_ALL + "]>>> "

    def do_listen(self, line):
        PORT = line
        subprocess.call('nc -lvnp {}'.format(PORT))

    def do_pythonws(self, line):
        PORT = int(line)

        Handler = http.server.SimpleHTTPRequestHandler

        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("Serving at port: " + str(PORT))
            httpd.serve_forever()

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


def shellExec():
    Shells().cmdloop()
