import random
# from random import shuffle


def embaralha(word):
    w = random.sample(word, len(word))
    w = ''.join(w)
    return w


def game(word, r_word):
    print(f'Tente advinhar a palavra: \n{r_word}')
    cont = 6
    for v in range(1, 7):
        print(f'Você tem {cont} tentativas!')
        tentativa = input(str('===>> '))
        cont -= 1
        if tentativa == word:
            print('Você ganhou!')
            break


with open("Exercicios/word random.txt", "r") as arquivo:
    words = arquivo.read()
    word_list = words.split('\n')
print(word_list)
word_random = random.choice(word_list)
print(word_random)
word_embaralhada = embaralha(word_random)
print(word_embaralhada)
game(word_random, word_embaralhada)

