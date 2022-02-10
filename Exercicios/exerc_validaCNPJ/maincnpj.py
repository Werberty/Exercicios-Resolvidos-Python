import exer_validaCNPJ

cnpj = input(str('Digite o CNPJ: '))
valido = exer_validaCNPJ.valida_cnpj(cnpj)
if valido:
    print('CNPJ Válido')
else:
    print('CNPJ Inválido')
