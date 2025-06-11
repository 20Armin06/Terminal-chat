#192.168.174.196

from socket import *

def start_server():
    server = socket(AF_INET , SOCK_STREAM)
    server.bind(("ip","socket"))
    server.listen(5)
    print("با موفقیت وصل شد")
    while 1 :
        client , add =server.accept()
        print(f"{add} به سرور متصل شد")
        message = client.recv(1024).decode('utf-8')
        print(f'{message}پیام دریافت شد')
        client.send("✔✔".encode('utf-8'))
        client.close()

start_server()