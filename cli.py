from socket import *

def send_message (txt):
    client = socket(AF_INET,SOCK_STREAM)
    client.connect(("ip","socket"))
    client.send(txt.encode('utf-8'))
    response = client.recv(1024).decode('utf-8')
    print(f" random: {response}")
    client.close()

while 1:
    txt = input(" random: ")
    send_message(txt)