carrinho = []

carrinho.append(('produto 1', 20.45))
carrinho.append(('produto 2', '30'))
carrinho.append(('produto 3', 50))

valor = sum([float(y) for x, y in carrinho])
print(valor)
