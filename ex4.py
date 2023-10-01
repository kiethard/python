import random

count = 0
def simulator_dice4(n):
    global count
    for i in range(n):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if (die1 == 1 and die2 ==6) or (die1 ==6 and die2 ==1):
            count +=1

simulator_dice4(1000000)
probability = count/1000000
print(probability)    