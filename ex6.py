import itertools
import random

def simulator_poker1(n):
    suits = {'Hearts', 'Diamonds', 'Clubs', 'Spades'}
    ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}

    cards = list(itertools.product(suits, ranks))
    count = 0

    for i in range(n):
        five_cards = random.sample(cards, 5)
        if all(card[0] == 'Hearts' for card in five_cards):
            count += 1

    experimental_probability = count / n
    return experimental_probability

n = 1000000
probability = simulator_poker1(n)
print(probability)
