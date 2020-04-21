import socket
import pickle
from users import Angajat

HEADERSIZE = 10 
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = {'0':'0'}

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect((socket.gethostname(),1240))
validation = 'valid'
ang = Angajat('a','a','a','a','a')
def comunicate(d):
    msg = pickle.dumps(d)
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8")+ msg
    c.send(msg)
    validation = c.recv(2048).decode(FORMAT)
    print(validation)

