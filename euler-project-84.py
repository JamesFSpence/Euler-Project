import random
import numpy as np
import time
spaces = ['GO','A1','CC1','A2','T1','R1','B1','CH1','B2','B3','JAIL','C1','U1','C2','C3','R2','D1','CC2','D2','D3','FP','E1','CH2','E2','E3','R3','F1','F2','U2','F3','G2J','G1','G2','CC3','G3','R4','CH3','H1','T2','H2']
s = 4 # sides on dice
def rollDice():
    a = random.randint(1,s)
    b = random.randint(1,s)
    if a == b:
        doublerolled = True
    else:
        doublerolled = False
    diceroll = a + b
    return [a+b,doublerolled]

l = len(spaces)
visited = [] # array which counts number of visits to each place
for i in range(l):
    visited.append([0,i])

rails = [5,15,25,35]
utilities = [12,28]
chests = [2,17,33]
chances = [7,22,36]

ccorder = np.random.permutation(16)
cccard = 0
chorder = np.random.permutation(16)
chcard = 0

x=0
for i in range(100000):
    diceroll = rollDice()
    x += diceroll[0]
    x = x%40
    if diceroll[1]:
        dubinrow += 1
        if dubinrow == 3: #3 triples in a row -> to jail
            x = 10
            dubinrow = 0
    else:
        dubinrow = 0
    if x in chances:#land on chance
        card = chorder[chcard]
        chcard = (chcard+1)%16
        if card < 6: # move to respective spot
            chmoves = [0,10,11,24,39,5]
            x = chmoves[card]
            chmoves = None
        if card in [6,7]: # move to next station
            if x == 7:
                x = 15
            elif x == 22:
                x = 25
            else:
                x = 5
        if card == 8: #move to next utility
            if x == 22:
                x = 28
            else:
                x = 12
        if card == 9:
            x -= 3
    if x in chests: #land on ccommunity chest
        card = ccorder[cccard]
        cccard =(cccard+1)%16
        if card < 2: #move to respective spot
            ccmoves = [0,10]
            x = ccmoves[card]
            ccmoves = None
    if x == 30: #land on go to jail
        x = 10
    visited[x][0] += 1

print(sorted(visited,reverse = True))