import itertools

def cross(A,B):
    return {a+b for a in A for b in B}

urn = cross('W','12345678') | cross ('B','123456') | cross ('R','123456789')
count = 0
for selection in itertools.combinations(urn,6):
    white  = selection.count('W')
    blue = selection.count('B')
    red = selection.count('R')

    if white == 2 and blue ==2 and red ==2:
            count += 1

total = len(list(itertools.combinations(urn,6)))
probability = count/ total
print(probability)
