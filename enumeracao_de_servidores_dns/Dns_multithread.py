""" Usando multithread para agilizar o processo de brute force """

from Queue import Queue
import threading
import socket

dominio = raw_input("Digite o dominio")
lock = threading.lock() #cria um objeto lock, usado para exibir na tela os resultados da brute force DNS de forma organizada

def brute_force():
	while not q.empty(): #verifica se o objeto Queue está vazio, caso esteja, todas as palavras já foram testadas
		
		DNS = q.get() + "." + gethostbyname(DNS) #o get é usado para obter item do objeto Queue. (um objeto Queue é da forma First in First out)
		try: 
			IP = socket.gethostbyname(DNS)
			lock.acquire()
			print DNS + ":\t" + IP

		except socket.gaierror:
			pass

		else:
			lock.release()
		q.task_done()


q = Queue()
for i in range(20):
	t = threading.Thread(target=brute_force)
	t.daemon = True
	t.start()
with open("brute_force.txt") as lista:
	while True:
		nome = lista.readline().strip("\n")
		if not nome:
			break
		q.put(nome)
q.join()
print "\nMapeamento completo"