cpf = str(input('Digite o CPF: '))
cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')
novo_cpf = cpf[:9]
if len(cpf) == 11:
    if cpf.isnumeric():
        # Primeira soma:
        soma1 = 0
        cont = 0
        digito_1 = 0
        for c in range(10, 1, -1):
            soma1 = soma1 + (int(cpf[cont]) * c)
            cont += 1
        func1 = 11 - (soma1 % 11)
        if func1 > 9:
            digito_1 = 0
        else:
            digito_1 = func1
        novo_cpf += str(digito_1)
        # Segunda soma:
        soma2 = 0
        cont = 0
        for c in range(11, 1, -1):
            soma2 = soma2 + (int(novo_cpf[cont]) * c)
            cont += 1
        func2 = 11 - (soma2 % 11)
        if func2 > 9:
            digito_2 = 0
        else:
            digito_2 = func2
        novo_cpf += str(digito_2)

        if cpf == novo_cpf:
            print('\033[32mValido\033[m')
        else:
            print('\033[31mInvalido\033[m')
else:
    print('\033[31mDigite o CPF corretamente...\033[m')
