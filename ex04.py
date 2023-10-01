import itertools

def cross(A,B):
    return {a+b for a in A for b in B}

urn = cross('M','123456') | cross('W','123456789')
U5 = list(itertools.combinations(urn,5))
print(U5)


count = 0
for u in U5:
    s = ""
    for i in u:
        s += i[0]
    if s.count('M') ==3 and s.count('W') ==2:
        count +=1
print(count)

