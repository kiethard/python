import itertools

def cross(A,B):
    return{a+b for a in A for b in B}
urn = cross('W','12345678') | cross('B','123456') | cross('R','123456789')

#a
k =  3
U3 = list(itertools.combinations(urn,k))
print(len(U3))

#b
countB = 0
for u in U3:
    f = u[0][0] + u[1][0] + u[2][0]

    if len(set(f)) ==3:
        countB +=1
print(countB)
#c
countC =0
for u in U3:
    if u[0][0] == 'W' and u[1][0] =='R':
        countC +=1
print(countC)