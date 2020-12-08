# -*- coding: utf-8 -*-

""" lê nomes de dominios a partir de um arquivo de texto"""

import socket 

dominio = raw_input("Digite o dominio: ")
with open("brute_force.txt") as arq:
	nomes = arq.readlines()
for nome in nomes:
	DNS = nome.strip("\n") + "." + dominio
	try:
		print DNS + ": " + socket.gethostbyname(DNS) #caso o host use mais de um ip para um nome, use socket.gethostbyname_ex()

	except socket.gaierror:
		pass