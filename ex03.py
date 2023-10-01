import itertools

def cross(A,B):
  return {a+b for a in A for b in B}


urn = cross('M','1234') | cross('P','123') | cross('C','12') | cross('L','1')

def arrangements():
  U10 = list(itertools.permutations(urn,10))
  print(len(U10))
  count = 0
  for u in U10:
    s = ""
    for i in u:
      s += i[0]
    if ('MMMM' in s) and ('PPP' in s) and ('CC' in s):
      count += 1
  print(count)

arrangements()