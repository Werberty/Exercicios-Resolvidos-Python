lista_a = [10, 2, 3, 40, 5, 6, 7]
lista_b = [1, 2, 3, 4]

listas = zip(lista_a, lista_b)
soma_lista = [x + y for x, y in zip(lista_a, lista_b)]
print(soma_lista)
