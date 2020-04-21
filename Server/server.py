import socket
import pymongo
from pymongo import MongoClient
import pickle
from users import Angajat, Admin
import threading
#import server2
cluster = pymongo.MongoClient('localhost',27017)
database = cluster["LantCofetarii"]
collection1 = database["Angajati"]

HEADERSIZE = 10
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = {'0':'0'}

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1240))
s.listen(5)



def client_hendeler(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    ok = 'no'
    connected = True
    while connected:
        # m = "Welcome to the server!"
        # m = bytes(f'{len(m):<{HEADERSIZE}}', "utf-8") + m
        # clientsocket.send(m)
        msg_len = conn.recv(HEADERSIZE).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len)
            angajat = pickle.loads(msg)
            print(angajat)
            if len(angajat) == 6:
                collection1.insert_one(angajat)
            if len(angajat) == 3:
                collection1.find_one(angajat)
                ok = 'valid'
            if angajat == {'0':'0'}:
                connected = False
            conn.send(ok.encode(FORMAT))
            # a = pickle.dumps(angajat)
            # a = bytes(f'{len(a):<{HEADERSIZE}}', "utf-8")+ a
            # conn.send(a)
    conn.close()

def start():
    s.listen()
    print(f"[LISTENING] Server is listening")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=client_hendeler, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


print("[STARTING] server is starting...")
start()
#server2.start()