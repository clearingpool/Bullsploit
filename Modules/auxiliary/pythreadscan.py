
#basic module description
def description() -> str:
    return "Standard auxiliary (Multithread scaner)"

#basic module rank
def rank() -> str:
    return "Good"

#basic module date
def date() -> str:
    return "08.03.2026"

#set arguments
def depargs() -> dict:
    return {
        "host": "IPv4 addr",
        "range": "Port diapasone",
        "threads": "Number of threads"
    }

#imports
from StrFuncs import evnt, err, timenow, beautip
import socket
from colorama import Fore, Style
from threading import Semaphore, Thread
import json
import os

#main a
def main(ip: str, port: int, semaphore, services: dict) -> None:
    with semaphore:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            res = s.connect_ex((ip, port))
            if res == 0:
                servicename = services.get(str(port), "UNKNOWN")
                print(f"{Fore.YELLOW}{Style.RESET_ALL}{timenow()}{Fore.YELLOW} {Style.RESET_ALL}Port{Fore.CYAN} {port} {Style.RESET_ALL}is opened on service{Fore.GREEN} {servicename}{Style.RESET_ALL}")
            s.close()
        except Exception as er:
            print(f"{err()} {er}")

        
#launch func
def launch(args: dict) -> None:
    try:
        servpath = os.path.join(os.path.dirname(__file__), "Services.json")
        if not os.path.exists(servpath):
            print(f"{err()} Services data not found!")
            return
        try:
            with open(servpath, "r", encoding="utf-8") as f:
                services = json.load(f)
        except Exception as b:
            print(f"{err()} {b}")
            services = {}
        target = args.get("host", "127.0.0.1")
        portrange = args.get("range", "1-1000")
        threadcount = int(args.get("threads", 100))
        try:
            startp, endp = map(int, portrange.split("-"))
        except:
            print(f"{err()} Invalid range format")
            return
        print(f"{evnt()} Starting scan on {beautip(target)} at {Fore.GREEN}{timenow()}{Style.RESET_ALL}")
        sem = Semaphore(threadcount)
        threads = []
        for port in range(startp, endp + 1):
            sem.acquire()
            t = Thread(target=main, daemon=True, args=(target, port, sem, services))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()
        print(f"{evnt()} Scan successfully finished!")
    except Exception as error:
        print(f"{err()} {error}")