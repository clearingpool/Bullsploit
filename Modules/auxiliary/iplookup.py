
#basic module description
def description():
    return "Ip lookup"

#basic module rank
def rank():
    return "Excellent"

#basic module date
def date():
    return "01.08.2026"

#set arguments
def depargs():
    return {
        "ip": "IPv4 addr"
    }

#imports
from StrFuncs import err, evnt, timenow, beautip
from ipwhois import IPWhois

#main function
def main(ip):
    try:
        query = IPWhois(ip)
        result = query.lookup_rdap
    except Exception as k:
        print(k)

#launch func
def launch(args):
    ip = args.get("ip", "127.0.0.1")
    print(f"{evnt()} Sending request for {beautip(ip)}")
    main(ip)
