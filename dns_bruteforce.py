import builtins
import socket

dominio = input("Alvo: ")

with open("bruteforce.txt", "r") as arquivo:
    bruteforce = arquivo.readlines()

for nome in bruteforce:
    DNS = nome.strip("\n") + "." + dominio

    try:
        print(DNS + ": " + socket.gethostbyname(DNS))
    except socket.gaierror:
        pass