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

def	ex6(lista_ex06):
	triplas = 0
	for i in range (len(lista_ex06) - 2):
		if lista_ex06[i] == lista_ex06[i + 1] == lista_ex06[i + 2]:
			triplas += 1
	return triplas

def	ex7(d):
	while True:
		str = input("Qual método de loop gostaria? while ou for: ")
		if str == "for":
			for t in range (d):
				print("*", end="")
			print("")
		elif str == "while":
			count = 0
			while count < d:
				print("*", end="")
				count += 1
			print("")

def	ex8(l, c):
	matriz = []
	for i in range(l):
		linha = list(map(int, input(f"Digite os {c} valores da linha {i + 1} (separe-os por espaço): ").split()))
		if len(linha) != c:
			print(f"A linha {i + 1} deve ter exatamente {c} valores.")
			return
		matriz.append(linha)
	maior_valor = matriz[0][0]
	for linha in matriz:
		for valor in linha:
			if valor > maior_valor:
				maior_valor = valor
	print(f"O maior valor da matriz é: {maior_valor}")

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

		lista_ex06 = []
		while True:
			j = input("Digite um número ou termine: ")
			if j == "termine" and len(lista_ex06) > 2:
				break
			try:
				j = int(j)
				print("Número adicionado!")
				lista_ex06.append(j)
			except ValueError:
				print("Por favor, digite um número válido.")
		print(ex6(lista_ex06))

	if int(ex_num) == 7:
		print("--------- exercicio 7 ----------")

		while True:
			d = input("Digite um número positivo: ")
			try:
				d = int(d)
				if d > 0:
					break
				else:
					print("Por favor, digite um número positivo")
			except ValueError:
				print("Por favor, digite um número válido.")
		print(ex7(d))

	if int(ex_num) == 8:
		print("--------- exercicio 8 ----------")

		while True:
			l = input("Digite um número entre 0 e 100 para linha: ")
			try:
				l = int(l)
				if l > 0:
					break
				else:
					print("Por favor, digite um número positivo")
			except ValueError:
				print("Por favor, digite um número válido.")
		while True:
			c = input("Digite um número entre 0 e 100 para coluna: ")
			try:
				c = int(c)
				if c > 0:
					break
				else:
					print("Por favor, digite um número positivo")
			except ValueError:
				print("Por favor, digite um número válido.")
		ex8(l, c)

	print("------------- Fim --------------")



