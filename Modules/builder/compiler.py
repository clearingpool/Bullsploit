#basic module description
def description():
    return "Go module compiler"

#basic module rank
def rank():
    return "Excellent"

#basic module date
def date():
    return "27.06.2026"

#set arguments
def depargs():
    return {
        "type": "Module type: auxiliary/payload"
    }

#imports
from StrFuncs import err, evnt, timenow, current
import subprocess

#main function
def main():
    pass

#launch func
def launch(args: dict):
    module = args["type"]
    if module.startswith("payloads"):
        print("In development...")
    elif module.startswith("auxiliary"):
        try:
            subprocess.run(["go", "build", "gothreadscan.go"], check=True)
            print(f"{evnt()} Go binary file successfully compiled")
        except subprocess.CalledProcessError as e:
            print(f"{err()} Compilation failed")
            print(f"Error log: {e}")
    else:
        print(f"{err()} No situable module found")



