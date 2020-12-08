# -*- coding: utf-8 -*-
import socket 

users = []

while True:
	usuario = input("Digite um usuário ou digite 'Sair': ")
	if usuario == "Sair":
		break
	users.append(usuario)

users.sort()

ip = input("Digite o ip do servidor SMTP: ")

for usuario in users:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((ip, 25))
	sock.recv(1024)
	sock.send("VRFY" + usuario + "\n")
	resposta = sock.recv(1024)
	sock.close()
	if "252" in resposta:
		print(f"{usuario} é um usuário válido! ")

	elif "520" in resposta:
		print(f"{usuario} não é um usuário válido...")

	elif "503" in resposta:
		print(f"Servidor reqauer atenção")
		break

	elif "500" in resposta:
		print("Comando VRFY não suportado pelo servidor")
		break

	else:
		print(f"Resposta do servidor: {resposta}")

