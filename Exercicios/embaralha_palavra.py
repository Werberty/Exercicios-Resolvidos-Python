import random


def scrambles_word(word):
    word = word.upper().strip()
    sequence = []
    r_word = ''
    n = len(word) - 1
    while True:
        x = random.randint(0, n)
        if x not in sequence:
            sequence.append(x)
            if len(word) == len(sequence):
                break
    for k in sequence:
        r_word += word[k]
    return r_word


def embaralha():
    return random.random()


new_word = ['p', 'y', 't', 'h', 'o', 'n']
random.shuffle(new_word, embaralha)
print(new_word)
