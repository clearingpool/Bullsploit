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
        "module": "Golang module"
    }

#imports
from StrFuncs import err, evnt, timenow, current
import subprocess

#main function
def main(type: str="auxiliary", name: str="gothreadscan"):
    try:
        subprocess.run(["go", "build", f"{name}.go"], check=True)
        print(f"{evnt()} Go binary file successfully compiled")
    except subprocess.CalledProcessError as e:
        print(f"{err()} Compilation failed")
        print(f"Error log: {e}")


#launch func
def launch(args: dict):
    module = str(args.get("module"))
    type, name = module.split("/")
    main(type, name)
    



