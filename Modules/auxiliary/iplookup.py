
#basic module description
def description() -> str:
    return "Ip lookup"

#basic module rank
def rank() -> str:
    return "Excellent"

#basic module date
def date() -> str:
    return "01.08.2026"

#set arguments
def depargs() -> dict:
    return {
        "ip": "IPv4 addr"
    }

#imports
from StrFuncs import err, evnt, timenow, beautip
import requests
from colorama import Fore, Style

#main function
def main(ip: str = "8.8.8.8") -> None:
    fields = "status,message,continent,continentCode,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
    url = f"http://ip-api.com/json/{ip}?fields={fields}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if data:
            print(f"{timenow()} Data received for ip query")
            print(f"{evnt()} Results:")
            print(f" Location:    {Fore.CYAN}{data.get('continent')} {data.get('country') if data.get('country') else ""}{Style.RESET_ALL}")
            print(f" Coordinates: {Fore.CYAN}{data.get('lat')}, {data.get('lon')}{Style.RESET_ALL}")
            print(f" Timezone:    {Fore.CYAN}{data.get('timezone')}{Style.RESET_ALL}")
            print(f" Currency:    {Fore.CYAN}{data.get('currency')}{Style.RESET_ALL}")
            print(f" ISP:         {Fore.CYAN}{data.get('isp')} ({Style.RESET_ALL}{data.get('org')}{Fore.CYAN}){Style.RESET_ALL}")
            print(f" ASN:         {Fore.CYAN}{data.get('as')} {Style.RESET_ALL}({data.get('asname')})")
            print(f" Reverse DNS: {Fore.CYAN}{beautip(data.get('reverse')) if data.get('reverse') else f"{Fore.YELLOW}None"}{Style.RESET_ALL}")
            print(f" Mobile inet: {Fore.CYAN}{f'{Fore.GREEN}Yes' if data.get('mobile') else f"{Fore.RED}No"}{Style.RESET_ALL}")
            print(f" Proxy/VPN:   {Fore.CYAN}{f'{Fore.GREEN}Yes' if data.get('proxy') else f"{Fore.RED}No"}{Style.RESET_ALL}")
            print(f" Hosing:      {Fore.CYAN}{f'{Fore.GREEN}Yes' if data.get('hosting') else f"{Fore.RED}No"}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{err()} {e}")

#launch func
def launch(args: dict) -> None:
    ip = args.get("ip", "127.0.0.1")
    print(f"{timenow()} Sending request for {beautip(ip)}")
    main(ip)
