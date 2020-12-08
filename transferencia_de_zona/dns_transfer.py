# -*- coding: utf-8 -*-

import dns.query
import dns.zone
import dns.resolver

dominio = raw_input("Digite o dominio: ")

registrosNS = dns.resolver.query(dominio, "NS") #Determina quais são os registros NS do dominio
lista = []

for registro in registrosNS:
	lista.append(str(registro))

for registro in lista:
	try:
		transferenciaZona = dns.zone.from_xfr(dns.query.xfr(registro, dominio)) #realiza a transferencia de zona

		

	except:
		print "Erro na transferência de zona"

	else:
		registroDNS = transferenciaZona.nodes.keys()
		registroDNS.sort()
		for n in registroDNS:
			print transferenciaZona[n].to_text(n)