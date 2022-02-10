
from os import write


def extracting_data(arquivo):
    with open(arquivo, "r") as arquivos:
        usuarios = arquivos.readlines()
    usuario_lista = []
    cont = 0
    disk = 0
    for line in usuarios:
        usuario_lista.append(line.split(' '))
        user_list = [list(filter(('').__ne__, user)) for user in usuario_lista]
        for user in user_list:
            user[1] = int(user[1])
        disk += user_list[cont][1]
        cont += 1
    return user_list, disk


def converter(byte):
    return byte / 1000000


def calculate_percentage(disk, size):
    disk = converter(disk)
    return 100*(size/disk)


lista_usuarios = extracting_data("Exercicios/exerc_criarRelatorio/usuarios.txt")
with open("Exercicios/exerc_criarRelatorio/relatorio.txt", "w") as arquivo:
    arquivo.write(
        'ACME Inc.               Uso do espaço em disco pelos usuários\n')
    arquivo.write(
        '----------------------------------------------------------------\n')
    arquivo.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
    for n, usuario in enumerate(lista_usuarios[0], 1):
        size = converter(usuario[1])
        percent = calculate_percentage(lista_usuarios[1], size)
        disk = converter(lista_usuarios[1])
        arquivo.write(
            f'{n:<4} {usuario[0]:<15} {size:>8.2f} MB {percent:>14.2f} %\n')
    disk_med = disk/len(lista_usuarios[0])
    arquivo.write(f'\nEspaço total ocupado: {disk:.2f} MB\n')
    arquivo.write(f'Espaço médio ocupado: {disk_med:.2f} MB')
