import socket
import pickle
from users import Angajat

HEADERSIZE = 10 
FORMAT = 'utf-8'

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((socket.gethostname(),1251))
ang = Angajat('a','a','a','a','a')
angajat1={}
def comunica(m):
    print(m)
    message = m.encode(FORMAT)
    msg_len = len(message)
    send_length = str(msg_len).encode(FORMAT)
    send_length += b' ' * (HEADERSIZE - len(send_length))
    c.send(send_length)
    c.send(message)
    #c.send(m.encode(FORMAT))
    msg_len = c.recv(HEADERSIZE).decode(FORMAT)
    if msg_len:
            msg_len = int(msg_len)
            b = c.recv(msg_len)
            angajat1 = pickle.loads(b)
            print("Data recv:",angajat1)
            return angajat1
#comunica('ba')