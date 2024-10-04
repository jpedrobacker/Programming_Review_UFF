def	ex1(lista_ex01):
	aux = lista_ex01[0]
	for i in lista_ex01:
		if i > aux:
			aux = i
	return aux

def	ex2(n):
	primos = []
	num = 2
	if n < 1:
		return False
	while len(primos) < n:
		is_prime = True
		for div in range (2, int(num**0.5) + 1):
			if num % div == 0:
				is_prime = False
				break
		if is_prime:
			primos.append(num)
		num += 1
	return primos

def	ex3(q):
	sum = 0
	for x in range (1, q + 1, 2):
		p_cond = False
		sum += x
		if sum == q:
			p_cond = True
			break
	for x in range (1, q + 1, 1):
		s_cond = False
		if x ** 2 == q:
			s_cond = True
			break
	if p_cond and s_cond:
		return "É quadrado perfeito"
	else:
		return "Não é um quadrado perfeito"

def	ex4(lista_ex04):
	zer = 0
	pos = 0
	neg = 0
	for x in lista_ex04:
		if x == 0:
			zer += 1
		elif x > 0:
			pos += 1
		elif x < 0:
			neg += 1
	print(f"Zeros = {zer}\nPositivos = {pos}\nNegativos = {neg}")

def	ex5(lista_ex05):
	zer2 = 0
	pos2 = 0
	neg2 = 0
	total = len(lista_ex05)
	for x in lista_ex05:
		if x == 0:
			zer2 += 1
		elif x > 0:
			pos2 += 1
		elif x < 0:
			neg2 += 1
	print(f"Zeros = {(zer2 * 100) / total}%\nPositivos = {(pos2 * 100) / total}%\nNegativos = {(neg2 * 100) / total}%")

#def	ex6():

#def	ex7():

#def	ex8():

if __name__ == "__main__":
	ex_num = input("Qual ex?: ")

	if int(ex_num) == 1:
		print("--------- exercicio 1 ----------")

		lista_ex01 = []
		for x in range (3):
			while True:
				a = input("Digite um número: ")
				try:
					a = int(a)
					print("Número adicionado!")
					lista_ex01.append(a)
					break
				except ValueError:
					print("Por favor, digite um número válido.")
		print(ex1(lista_ex01))

	if int(ex_num) == 2:
		print("--------- exercicio 2 ----------")

		while True:
			n = input("Digite um número positivo: ")
			try:
				n = int(n)
				if n > 0:
					break
				else:
					print("Por favor, digite um número positivo")
			except ValueError:
				print("Por favor, digite um número válido.")
		print(ex2(n))

	if int(ex_num) == 3:
		print("--------- exercicio 3 ----------")
		while True:
			q = input("Digite um número positivo: ")
			try:
				q = int(q)
				if q > 0:
					break
				else:
					print("Por favor, digite um número positivo")
			except ValueError:
				print("Por favor, digite um número válido.")
		print(ex3(q))

	if int(ex_num) == 4:
		print("--------- exercicio 4 ----------")
		lista_ex04 = []
		while True:
			h = input("Digite um número ou termine: ")
			if h == "termine":
				break
			try:
				h = int(h)
				print("Número adicionado!")
				lista_ex04.append(h)
			except ValueError:
				print("Por favor, digite um número válido.")
		ex4(lista_ex04)

	if int(ex_num) == 5:
		print("--------- exercicio 5 ----------")
		lista_ex05 = []
		while True:
			j = input("Digite um número ou termine: ")
			if j == "termine":
				break
			try:
				j = int(j)
				print("Número adicionado!")
				lista_ex05.append(j)
			except ValueError:
				print("Por favor, digite um número válido.")
		ex5(lista_ex05)

	if int(ex_num) == 6:
		print("--------- exercicio 6 ----------")

		#ex6()

	if int(ex_num) == 7:
		print("--------- exercicio 7 ----------")

		#ex7()

	if int(ex_num) == 8:
		print("--------- exercicio 8 ----------")

		#ex8()

	print("------------- Fim --------------")



