import random


def play_dice():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    return dice_1, dice_2

def check(moved, cont, p):
    result = sum(moved)
    natural = [7,11]
    craps = [2,3,12]
    ponto = [4,5,6,8,9,10]
    print(f'soma {result}')
    if cont == 1:
        if result in natural:
            return ['natural', result]
        elif result in craps:
            return ['crap', result]
        elif result in ponto:
            return ['ponto', result]
    else:
        if result == p:
            return ['natural', result]
        elif result == 7:
            return ['crap', result]
        else:
            return ['ponto', result]
            


cont = 1
p = 0
while True:
    x = input(str('Jogar os dados? [s/n]: '))
    if x == 's':
        move = play_dice()
        print(f'Dados jogados: {move[0]} {move[1]}')
        state = check(move, cont, p)
        # print(p)
        print(state[0])
        if state[0] == 'crap':
            print('VOCÊ PERDEU!')
            break
        elif state[0] == 'natural':
            print('VOCÊ GANHOU!')
            break
        elif state[0] == 'ponto':
            print('jogue novamente...')
            if cont == 1:
                p = state[1]
        cont += 1
    elif x == 'n':
        break
    else:
        print('INVÁLIDO')