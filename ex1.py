import itertools

A = {1,2,3,4,5}
k = 3

#a
num_3_digit =  list(itertools.permutations(A,k))
num_length = len(num_3_digit)
print("Number of the num_3_digit: ",num_length)
print("List of the numbers: ", num_3_digit)