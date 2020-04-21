import socket
import pymongo
from pymongo import MongoClient
import pickle
from users import Angajat, Admin
import threading

cluster = pymongo.MongoClient('localhost',27017)
database = cluster["LantCofetarii"]
collection1 = database["Angajati"]

HEADERSIZE = 10
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = {'0':'0'}

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),1251))
s.listen(5)
 


def client_hendele(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = (conn.recv(HEADERSIZE)).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            print(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            w = collection1.delete_many({'username': msg})
            print(w)
            print(msg)
            if(msg_length == "!"):
                connected = False
        a = collection1.find({'usertype':'angajat'})
        for i in a:
            b= pickle.dumps(i)
            b = bytes(f'{len(b):<{HEADERSIZE}}', "utf-8")+ b
            conn.send(b)
    conn.close()

def start():
    s.listen()
    print(f"[LISTENING2] Server is listening")
    while True:
        conn, addr = s.accept()
        thread1 = threading.Thread(target=client_hendele, args=(conn, addr))
        thread1.start()
        print(f"[ACTIVE CONNECTIONS2] {threading.activeCount() - 1}")


print("[STARTING2] server is starting...")
start()