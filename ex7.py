import itertools
import random

def simulator_poker2(n):
    suits= {'Hearts','Diamonds','Clubs','Spades'}
    ranks = {1,2,3,4,5,6,7,8,9,10,'J','Q','K'}
    cards = list(itertools.product(suits,ranks))
    count = 0

    for _ in range(n):
        five_cards= random.sample(cards,5)
        suits_in_cards = set(cards[1] for cards in five_cards)
        if len(suits_in_cards) ==4:
            count +=1
    experimental_probability = count/n
    return experimental_probability

n = 1000000
probability = simulator_poker2(n)
print(probability)
