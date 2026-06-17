
#basic module description
def description() -> str:
    return "OS fingerprinter"

#basic module rank
def rank() -> str:
    return "Good"

#basic module date
def date() -> str:
    return "17.04.2026"

#set arguments
def depargs() -> dict:
    return {
        "host": "IPv4 addr"
    }

#imports
from scapy.all import IP, ICMP, sr1
from StrFuncs import evnt, err, timenow
from colorama import Fore, Style

#main function
def main(ip: str) -> str:
    packet = IP(dst=ip)/ICMP()
    resp = sr1(packet, timeout=2, verbose=False)
    if resp:
        ttl = resp.getlayer(IP).ttl
        if ttl <= 64: return "Linux/Unix/macOS"
        if ttl <= 128: return "Windows"
        if ttl <= 255: return "Cisco/Network Device"
    return "unknown"

#launch func
def launch(args: dict) -> None:
    target = args.get("host", "127.0.0.1")
    print(f"{evnt()} Starting scan on {Fore.CYAN}{target}{Style.RESET_ALL} at {Fore.GREEN}{timenow()}{Style.RESET_ALL}")
    opersys = main(target)
    if opersys:
        print(" OS:", opersys)
