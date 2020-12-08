import socket

Dominio = raw_input("Digite o dominio: ")
Nomes = ["www", "mail", "mx", "ns", "ftp", "webmail", "web", "gateway", "secure", "intranet", "extranet", "smtp", "pop", "ns1", "mx1", "email", "admin", "dmz", "blog", "dns", "forum", "ntp", "pub", "route", "sql", "ssh", "webaccess", "xml", "imap"]


for nome in Nomes:
	DNS = nome + "." + Dominio
	try:
		print DNS + ": " + socket.gethostbyname(DNS)

	except socket.gaierror:
		pass
