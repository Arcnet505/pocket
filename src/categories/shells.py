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
        PORT = int(line)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(('localhost', PORT))

        sock.sendall(('GET / HTTP/1.1\nHost: google.com\n\n').encode())
        time.sleep(0.5)
        sock.shutdown(socket.SHUT_WR)

        res = ""

        while True:
            data = sock.recv(1024)
            if (not data):
                break
            res += data.decode()

        print(res)

        print("Connection closed.")
        sock.close()

        while 1:
            buf = ""
            shouldClose = False

            # collect the request
            inp = input("")
            while inp != "":
                # stop processing if we want the conneciton to close
                if (inp == "Connection: close"):
                    shouldClose = True
                buf += inp + "\n"
                inp = input("")

            buf += "\n"

            # do_listen(port buf.encode())

            if (shouldClose):
                break

    def do_webserver(self, line):
        "Start a python HTTP web server by running 'webserver PORT'"
        PORT = int(line)

        Handler = http.server.SimpleHTTPRequestHandler

        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("Serving at port: " + str(PORT))
            httpd.serve_forever()

    def do_exit(self, line):
        "Exits back to main menu"
        return True

    def do_back(self, line):
        "Returns back to previous prompt"
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
