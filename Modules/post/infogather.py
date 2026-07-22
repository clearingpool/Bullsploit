
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
    payload = """python3 -c 'import platform, os, psutil; v = psutil.virtual_memory(); ram = f"{v.total / (1024**3):.1f}GB"; cpu = next((line.split(":")[1].strip() for line in open("/proc/cpuinfo") if "model name" in line), "Unknown") if os.path.exists("/proc/cpuinfo") else "Unknown"; print(f"os: {platform.system()} {platform.release()}\\ncpu: {cpu}\\nram: {ram}")'"""


