import random

count = 0
def simulator_dice1(n):
    global count
    for i in range(n):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if die1 % 2 == 0 and die2 %2 ==0:
            count += 1

simulator_dice1(1000000)
probability = count / 1000000
print(probability)