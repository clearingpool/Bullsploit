import socket
from SessionManager import manager
from StrFuncs import evnt, timenow, current, err
import threading

def Listen(ip: str, port: int) -> None:
    try:
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((ip, port))
        s.listen(10)
        print(f"{evnt()} Listening for incoming connection...")
        def loop():
            while True:
                try:
                    conn, addr = s.accept()
                    sid = manager.add(conn, addr)
                    print(f"\r\n{evnt()} {timenow()} New session [{sid}]")
                    print(f"{current()}", end="", flush=True)
                except Exception as h:
                    print(h)
        threading.Thread(target=loop, daemon=True).start()
    except Exception as error:
        print(f"{err()} {error}")
        import traceback
        print(f"\n{err()} Error:")
        traceback.print_exc()
