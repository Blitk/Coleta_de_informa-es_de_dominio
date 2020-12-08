from scapy.all import *

conf.verb = 0
ports = [21,22,23,80,8080,9999]
destino = input("Digite o ip do destino: ")
packageIP = IP(dst=destino)
packageTCP = TCP(dport=ports, flags="S")
pacote = packageIP/packageTCP
ans, unans = sr(pacote, inter=0.1, timeout=1)
print("porta \t estado")
for pacoteRecebido in ans:
	print(f'{pacoteRecebido[1][IP]} \t {pacoteRecebido[1][TCP].sprintf("%flags%")}')
	
