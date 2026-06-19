#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
ver = 1.1
from colorama import Fore, Style, Back
from StrFuncs import err, evnt, timenow, current
import ast
import time
import threading
import importlib
from importlib import util
import subprocess
from SessionManager import manager
import json
import webbrowser

def turn() -> None:
    input("Press any key to continue...")

def red(text: str) -> str:
    return Fore.RED + text + Style.RESET_ALL

def white(text: str) -> str:
    return Fore.WHITE + text + Style.RESET_ALL

def yellow(text: str) -> str:
    return Fore.YELLOW + text + Style.RESET_ALL


animdone = threading.Event()
stopanim = threading.Event()

def animation() -> None:
    try:
        for i in range(2):
            chars = [".", "..", "...", "   "]
            for i in chars:
                if stopanim.is_set():
                    break
                sys.stdout.write(f"\rInitializating Bullsploit{i}")
                sys.stdout.flush()
                time.sleep(0.5)
        sys.stdout.write("\r                            ")
        sys.stdout.flush()
    finally:
        animdone.set()

def check() -> None:
    counts = {"payloads": 0, "auxiliary": 0, "post": 0, "builder": 0}
    paths = ["auxiliary", "payloads", "post", "builder"]
    errlog = []
    threading.Thread(target=animation, daemon=True).start()
    try:
        if not os.path.exists("Modules"):
            stopanim.set()
            print(f"\n{err()} Not found the Modules path")
            return
        for i in paths:
            path = os.path.join("Modules", i)
            if not os.path.exists(path):
                errlog.append(f"Not found the {i} path")
        for root, dirs, files in os.walk("Modules"):
            for file in files:
                if file.endswith(".py") and file != "__init__.py":
                    if f"{os.sep}payloads" in root:
                        counts["payloads"] += 1
                    if f"{os.sep}auxiliary" in root:
                        counts["auxiliary"] += 1
                    if f"{os.sep}post" in root:
                        counts["post"] += 1
                    if f"{os.sep}builder" in root:
                        counts["builder"] += 1
                    modul = os.path.join(root, file)
                    modulename = file[:-3]
                    try:

                        with open(modul, "r", encoding="utf-8") as fail:
                           code = fail.read()
                           ast.parse(code)
                    except Exception as f:
                        errlog.append(f"Error in file {file} in {root}")


        payloadc = counts["payloads"]
        auxiliaryc = counts["auxiliary"]
        postc = counts["post"]
        builderc = counts["builder"]

        if errlog:
            stopanim.set()
            print()
            for r in errlog:
                print(f"{err()} {r}")

        animdone.wait()
        mainmenu(payloadc, auxiliaryc, postc, builderc)
    except Exception as l:
        print(f"{err()} {l}")
    

def mainmenu(payloadc: int, auxiliaryc: int, postc: int, builderc: int) -> None:
    print(red(f"""
       ,/         \\,
      ((__,-'''-,__))
       `--)~   ~(--`
      .-'(       )`-,
      `~~`d\\   /b`~~`
          |     |
          (6___6)  {Fore.WHITE}{Back.RED}BullSploit{Style.RESET_ALL} {Fore.WHITE}{Back.RED}Framework{Style.RESET_ALL}{Fore.CYAN} dev{Fore.WHITE}#{Fore.CYAN}{ver} {Fore.RED}
           `---` {Style.RESET_ALL}"""))
    print(f"""
+- --=[ {f"{Fore.YELLOW}https://github.com/clearingpool{Style.RESET_ALL}":<53} ]-
+- --=[ {f"{payloadc} payload - {auxiliaryc} auxiliary - {postc} post - {builderc} builders":<45}]-
""")
    BSC(payloadc, auxiliaryc, postc, builderc)
    
class BSC:
    def __init__(self, payload: int, auxiliary: int, post: int, builder: int) -> None:
        self.post = post
        self.payload = payload
        self.aux = auxiliary
        self.builder = builder
        self.options = {}
        self.rank = {"Bad": Fore.RED, "Good": Fore.GREEN, "Normal": Fore.YELLOW, "Excellent": Fore.CYAN}
        self.folders = ["auxiliary", "payloads", "post", "builder"]
        self.rules = {}
        self.corrkey = []
        self.modules = []
        self.analyse()
        self.clearmodule()
        self.run()


    def parse(self, args=None) -> dict:
        if not args: return {}
        params = {}
        for i in args:
            if ":" in i:
                key, value = i.split(":", 1)
                params[key.lower()] = value
        return params


        

    def analyse(self) -> None:
        try:
            for folder in self.folders:
                path = os.path.join("Modules", folder)
                if os.path.exists(path):
                    for file in os.listdir(path):
                        if file.endswith(".py"):
                            modulepath = os.path.join(path, file)
                            self.modules.append({
                                "name": file.replace(".py", ""),
                                "type": folder,
                                "description": self.getdesc(modulepath),
                                "date": self.getdate(modulepath),
                                "rank": self.getrank(modulepath)
                                })
                else:
                    print(f"{err()} Folder {folder} was not found")
        except Exception as k:
            print(f"{err()} {k}")

    def getmeta(self, path: str, meta: str) -> str:
        try:
            with open(path, "r", encoding="utf-8") as f:
                parsed = ast.parse(f.read())
                for modul in parsed.body:
                    if isinstance(modul, ast.FunctionDef) and modul.name == meta:
                        for line in modul.body:
                            if isinstance(line, ast.Return) and isinstance(line.value, ast.Constant):
                                return line.value.value
            return f"No {meta}"
        except Exception as c:
            return "Read error"

    def getrank(self, path: str) -> str:
        return self.getmeta(path, "rank")

    def getdate(self, path: str) -> str:
        return self.getmeta(path, "date")

    def getdesc(self, path: str) -> str:
        return self.getmeta(path, "description")




    def clear(self) -> None:
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")
        self.run()

    def table(self, modultype=None) -> None:
        try:
            if modultype is None:
                filtered = self.modules
            else:
                mtype = modultype.lower()
                if mtype == "payload": mtype = "payloads"
                if mtype == "aux": mtype = "auxiliary"
                if mtype == "builders": mtype = "builder"
                filtered = [m for m in self.modules if m["type"].lower() == mtype.lower()]
            if not filtered:
                print(f"{err()} Not found modules for type: {mtype}")
                return
            print(f"\n  {evnt()}Founded modules {len(filtered)}")
            print(" ", "="*21, "\n")
            print("    #  Name                           Date         Rank      Description")
            print("  ", "-"*80)
            for cnt, mod in enumerate(filtered):
                rankcol = self.rank.get(mod["rank"], Fore.WHITE)
                if rankcol == Fore.WHITE:
                    ranktxt = f"{Fore.WHITE}None{Style.RESET_ALL}"
                else:
                    ranktxt = f"{rankcol}{mod["rank"]}{Style.RESET_ALL}"
                name = f"{mod["type"]}/{mod["name"]}"
                if len(name) >= 30:
                    name = name[:31] + "..."
                print(f"    {cnt:<2} {name:<30} {mod["date"]:<12} {ranktxt:<18} {mod["description"]} ")
            print()
        except Exception as y:
            print(f"{err()} {y}")
        
    
    def run(self) -> None:
        try:
            while True:
                
                rawcmd = input(f"{current()}").lower().strip().split()
                
                if not rawcmd:
                    continue
                cmd = rawcmd[0]

                args = rawcmd[1:] if len(rawcmd) > 1 else []

                match cmd:
                    case "exit": sys.exit()
                    case "help":
                        print(""" Usage: bsc>[options]

Common options:
    help                           --View help
    search <moduletype>            --Search module
    usagr                          --View useragreement
    github                         --Open the bullsploit repository on github
    site                           --Open the bullsploit site
    clear                          --Clear console
    use <module path>              --Use some module
    set <arguments>                --Add settings
    run                            --Start module
    exit                           --Exit bullsploit

                    """)

                    case "search":
                        self.table(args[0] if args else None)

                    case "run":
                        if not self.selectmod:
                            print(f"{err()} No module selected")
                        else:
                            mtype, mname = self.selectmod.split("/")
                            path = os.path.join("Modules", mtype, mname + ".py")
                            if not os.path.exists(path):
                                print(f"{err()} Module file not found {path}")
                        try:
                            spec = importlib.util.spec_from_file_location(mname, path)
                            modul = importlib.util.module_from_spec(spec)
                            spec.loader.exec_module(modul)
                            modul.launch(self.options)
                        except RuntimeError:
                            pass
                        except Exception as b:
                            print(f"{err()} {b}")



                    case "use":
                        if not args:
                            print(f"{err()} Usage: use <type>/<module>")
                            continue
                        module = args[0]
                        found = False
                        
                        
                        for m in self.modules:
                            mpath = f"{m["type"]}/{m["name"]}".lower()
                            if module == mpath:
                                found = True
                                data = {"Module": module}
                                with open("CurrentModule.json", "w", encoding="utf-8") as f:
                                    json.dump(data, f, indent=4, ensure_ascii=False)
                                self.selectmod = self.getmodule()
                        if not found: 
                            print(f"{err()} Not found module {module}")
                            return
                        
                        scheme = self.selectmod
                        finallyscheme = "Modules." + scheme.replace("/", ".")
                        m = importlib.import_module(finallyscheme)
                        self.rules = m.depargs()
                        
                        for key, value in self.rules.items():
                            self.corrkey.append(str(key.lower()))


                    case "set":
                        if not args: 
                            print(f"{err()} Usage: set <args>")
                            continue
                        if not self.selectmod: 
                            print(f"{err()} No select module!")
                            return
                        
                        newparams = self.parse(args)
                        if not newparams:
                            print(f"{err()} Usage: set <key>:<value>")
                        for key, value in newparams.items():
                            if key in self.corrkey:
                                print(f"{evnt()} {key.capitalize()} => {value}")
                            else:
                                print(f"{err()} Invalid parameter!")
                        self.options.update(newparams)

                    case "options":
                        if self.selectmod != "":
                            print(f" {evnt()} These parameters are available for {self.selectmod}: \n")
                            print(f"  Parameter      Data type\n  {"-"*26}")
                            for key, value in self.rules.items():
                                print(f"  {key:<10}     {str(value)}")
                            print()

                    case "sessions":
                        manager.show()

                    case "interact":
                        if args:
                            mtype, mname = self.selectmod.split("/")
                            result = os.path.join("Modules", mtype, mname + ".py")
                            try:
                                        sid = int(args[0])
                                        spec = importlib.util.spec_from_file_location(mname, result)
                                        modul = importlib.util.module_from_spec(spec)
                                        spec.loader.exec_module(modul)
                                        modul.interact(sid)
                            except Exception as h:
                                print(err(), h)
                        else:
                            print(f"{err()} No session select")


                    case "github":
                        webbrowser.open("https://github.com/clearingpool/Bullsploit")

                    case "site":
                        webbrowser.open("https://bullsploit.ru")

                    case "show":
                        if self.selectmod is not None:
                            for key, value in self.options.items():
                                print(f"{evnt()} {key.capitalize()} => {value}")


                    case "back":
                        self.selectmod = ""
                        self.options = {}
                        self.clearmodule()

                    case "check":
                        print(self.modules)



                    case "clear":
                        self.clear()
                    case _:
                        print(f"{err()} Error")
                
        except KeyboardInterrupt:
            choice = input(f"\nAre you sure you want to exit? (y/n)>").lower()
            if choice == "y": sys.exit()
            else: self.run()
        except Exception as h:
            print(f"{err()} {h}")
            turn()

    def clearmodule(self) -> None:
        with open("CurrentModule.json", "w", encoding="utf-8") as file:
            json.dump({}, file)

    def getmodule(self) -> str:
        with open("CurrentModule.json", "r", encoding="utf-8") as file:
            data = json.load(file)
        return data.get("Module") if data else ""
    


if __name__ == "__main__":
    check()
