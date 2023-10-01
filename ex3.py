import random

count  =0
def simulator_dice3(n):
    global count
    for i in range(n):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        if die1 == die2:
            count +=1
simulator_dice3(1000000)
probability = count/1000000
print(probability)
        
