
#Iniciando Estudos em Python: Bubble Sort Interativo 1
#Partindo do princípio de que o user vai fornecer o input correto
lista = []
flag = True
#Estrutura para receber o input do usuário (recebe números floats)
lista_len = int(input("Quantos números pretende sortear?"))
for i in range(lista_len):
	if i == 0:
		new_num = float(input("Digite o primeiro número:"))
	elif i > 0 and i != (lista_len - 1):
		new_num = float(input("Digite o próximo número:"))
	elif i == (lista_len - 1):
		new_num = float(input("Digite o último número:"))
	lista.append(new_num)
#impressão da lista passada
print("lista fornecida:{}".format(lista))
print("*** organizando lista ***")
#Estrutura que organiza a lista passada
while (flag):
	flag = False
	for i in range(len(lista) - 1):
		if lista[i] > lista[i + 1]:
			lista[i], lista[i + 1] = lista[i + 1], lista [i]
			flag = True
print(lista)