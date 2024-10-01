def	ex1(lista_ex01):
	aux = lista_ex01[0]
	for i in lista_ex01:
		if i > aux:
			aux = i
	return aux

def ex2(n):
	print(n)


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
		ex2(n)

	if int(ex_num) == 3:
		print("--------- exercicio 3 ----------")

	if int(ex_num) == 4:
		print("--------- exercicio 4 ----------")

	if int(ex_num) == 5:
		print("--------- exercicio 5 ----------")

	if int(ex_num) == 6:
		print("--------- exercicio 6 ----------")

	if int(ex_num) == 7:
		print("--------- exercicio 7 ----------")

	if int(ex_num) == 8:
		print("--------- exercicio 8 ----------")

		print("------------- Fim --------------")



