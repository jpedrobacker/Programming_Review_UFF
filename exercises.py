def	ex1(lista_ex01):
	aux = lista_ex01[0]
	for i in lista_ex01:
		if i > aux:
			aux = i
	return aux

def	is_prime(n):
	if n < 1:
		return False
	for div in range (2, int(n**0.5) + 1):
		if n % div == 0:
			return False
	return True

def	ex2(n):
	primos = []
	num = 2
	while len(primos) < n:
		if is_prime(num):
			primos.append(num)
		num += 1
	return primos

#def	ex3():

#def	ex4():

#def	ex5():

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

		#ex3()

	if int(ex_num) == 4:
		print("--------- exercicio 4 ----------")

		#ex4()

	if int(ex_num) == 5:
		print("--------- exercicio 5 ----------")

		#ex5()

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



