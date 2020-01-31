import socket
import threading
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def sendMsg():
    while True:
        try:
            s.send(bytes(input(''), "utf-8"))
        except Exception as e:
            print("Error {}".format(str(e)))
            break
        sys.exit()


def client(address):
    port = int(input('port: '))
    s.connect((address, port))

    iThread = threading.Thread(target=sendMsg)
    iThread.deamon = True
    iThread.start()

    while True:
        try:
            data = s.recv(1024)
            print(str(data, 'utf-8'))
        except:
            iThread.stop()
            sys.exit()

if len(sys.argv) > 1:
    client(sys.argv[1])
else:
    print("Nie można połączyć z serwerem. Sprawdź IP serwera")
    sys.exit()
