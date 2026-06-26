
#basic module description
def description() -> str:
    return "Asyncio port scanner"

#basic module rank
def rank() -> str:
    return "Excellent"

#basic module date
def date() -> str:
    return "29.04.2026"

#set arguments
def depargs() -> dict:
    return {
        "host": "IPv4 addr",
        "range": "Port diapasone"
    }

#imports
from StrFuncs import err, evnt, timenow
import asyncio
import os, json, time
from colorama import Fore, Style


#main function
sem = asyncio.Semaphore(1000)

async def main(host: str, ports: range, services: dict) -> None:
    result = []
    tasks = [portscan(host, p, result, services) for p in ports]
    await asyncio.gather(*tasks)
    print(f"{evnt()} Scan successfully finished! Found ports:{len(result)}")

async def portscan(host: str, port: int, result: list, services: dict) -> None:
    async with sem:
        try:
            connect = asyncio.open_connection(host, port)
            read, write = await asyncio.wait_for(connect, timeout=1.0)
            servicename = services.get(str(port), "UNKNOWN")
            print(f"{timenow()} Port{Fore.CYAN} {port} {Style.RESET_ALL}is opened on service{Fore.GREEN} {servicename}{Style.RESET_ALL}")
            result.append(port)
            write.close()
            await write.wait_closed()
        except: pass

#launch func
def launch(args: dict) -> None:
    try:
        basepath = os.path.dirname(__file__)
        servpath = os.path.join(basepath, "Services.json")
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
        portrangeraw = args.get("range", "1-1000")
        try:
            startport, endport = map(int, portrangeraw.split('-'))
        except Exception as h:
            print(f"{err()} {h}")
            startport, endport = 1, 1000
        portrange = range(startport, endport + 1)
        asyncio.run(main(target, portrange, services))
        
        
    except Exception as error:
        print(f"{err()}{error}")