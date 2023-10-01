import itertools

suits = {'Spades', 'Clubs', 'Diamonds', 'Hearts'}
ranks = {1,2,3,4,5,6,7,8,9,10,'J','Q','K'}
cards = list(itertools.product(suits,ranks))
print(len(cards))

#a
poker_5 = list(itertools.combinations(cards,5))
print(len(poker_5))

#b
three_of_a_kind = []
for poker in poker_5:
  s = set(rank[1] for rank in poker)
  s1 = list(rank[1] for rank in poker)
  if len(s) == 3:
    for r in ranks:
      if s1.count(r) == 3:
        three_of_a_kind.append(poker)
        break
print(len(three_of_a_kind))
for i in range(10):
  print(three_of_a_kind[i])