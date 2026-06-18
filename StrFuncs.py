from colorama import Fore, Style
from datetime import datetime


def evnt() -> str:
    return f"[{Fore.CYAN}~{Style.RESET_ALL}]"

def err() -> str:
    return f"{Fore.RED}[{Fore.WHITE}!{Fore.RED}]{Style.RESET_ALL}"

def timenow() -> str:
    now = datetime.now()
    timee = now.strftime("%H:%M:%S")
    nowtime = (f"{Fore.YELLOW}[{Fore.WHITE}{timee}{Fore.YELLOW}]{Style.RESET_ALL}")
    return nowtime

def beautip(ip: str) -> str:
    try:
        parts = [f"{Fore.GREEN}{p}" for p in ip.split(".")]
        output = f"{Fore.WHITE}.".join(parts) + Style.RESET_ALL
        return output
    except:
        return ip
    
def current() -> str:
    from BullsploitFramework import BSC
    obj = BSC.__new__(BSC)
    
    selectmod = f" {Fore.RED}({obj.getmodule()}){Style.RESET_ALL}" if obj.getmodule() else ""
    curmodule = f"\033[4mbsc\033[0m{selectmod}>"
    return curmodule
