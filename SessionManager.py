from StrFuncs import timenow, err, evnt, beautip
import threading

class sessions:
    def __init__(self) -> None:
        self.sessions = {}
        self.lock = threading.Lock()
        self.currentId = 1

    def add(self, conn: socket.socket, addr: tuple[str, int]) -> int:
        with self.lock:
            sid = self.currentId
            self.sessions[sid] = {"conn": conn, "addr": addr}
            self.currentId += 1
            return sid
    
    def show(self) -> None:
        with self.lock:
            if not self.sessions:
                print(f"{err()} Manager has no sessions.")
                return
            print(f"  {evnt()} Available sessions: ")
            print(f"  {"-" * 32}")
            print(f"  | № | Host             | port  |")
            print(f"  {"-" * 32}")
            for sid, sdata in self.sessions.items():
                ip, port = sdata["addr"]
                print(f"  | {sid:<2}| {beautip(ip):<15}  | {port} |")
            print(f"  {"-" * 32}")
            print()
            
    def getsession(self, sid: int) -> dict:
        with self.lock:
            return self.session.get(sid)
        
    def remove(self, sid: int) -> None:
        with self.lock:
            if sid in self.sessions:
                try:
                    self.session[sid]["conn"].close()
                except:
                    pass
            del self.sessions[sid]

manager = sessions()


