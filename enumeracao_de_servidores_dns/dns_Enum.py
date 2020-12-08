# enumera registros A, AAAA e MX do dominio desejado

import dns.resolver

dominio = raw_input("Digite o dominio: ")
registros = ["A", "AAAA", "MX", "NS"]
for registro in registros:
	resposta = dns.resolver.query(dominio, registro, raise_on_no_answer=False)
	if resposta.rrset is not None:
		print resposta.rrset