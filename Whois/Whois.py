#pip install python-whois
import whois

domain = input("Digite o dominio: ")
dados = whois.whois(domain)

for k, v in dados.items():
	print(f"\n{k}:  {v}")


ask = input("Deseja salvar os dados? ").lower()
if ask == "sim":
	with open("Whois_dados.txt", "w") as arquivo:
		for k, v in dados.items():
			temp = f"\n{k}:  {v}\n"
			arquivo.write(temp)

else:
	pass
