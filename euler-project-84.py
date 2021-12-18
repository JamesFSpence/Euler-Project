import random
import numpy as np
import time
spaces = ['GO','A1','CC1','A2','T1','R1','B1','CH1','B2','B3','JAIL','C1','U1','C2','C3','R2','D1','CC2','D2','D3','FP','E1','CH2','E2','E3','R3','F1','F2','U2','F3','G2J','G1','G2','CC3','G3','R4','CH3','H1','T2','H2']

def rolldice(pos):
    a = random.randint(1,6)
    b = random.randint(1,6)
    if a == b:
        doublerolled = True
    else:
        doublerolled = False
    diceroll = a + b
    newpos = (pos + diceroll)%40
    return [newpos,doublerolled]

for l in range(10):
    cc_order = np.random.permutation(16)
    ch_order = np.random.permutation(16)
    current_cc_card = 0
    current_ch_card = 0

    r_indexes = []
    cc_indexes = []
    ch_indexes = []
    u_indexes = []
    visited = []

    m = 0
    for space in spaces:
        visited.append([0,m])
        m+=1
        if space[0] == 'R':
            r_indexes.append(spaces.index(space))
        if space[0:2] == 'CC':
            cc_indexes.append(spaces.index(space))
        if space[0:2] == 'CH':
            ch_indexes.append(spaces.index(space))
        if space[0] == 'U':
            u_indexes.append(spaces.index(space))

    nodiar = 0 # "number of doubles in a row"
    pos = 0
    for i in range(100000):
        x = rolldice(pos)
        pos = x[0]
        found = False
        if x[1]:
            nodiar += 1
            if nodiar == 3:
                nodiar = 0
                pos = spaces.index('JAIL')
                found = True
        else:
            nodiar = 0
        while not found:
            found = True
            if pos == spaces.index('G2J'):
                pos = spaces.index('JAIL')
            elif pos in cc_indexes:
                card = cc_order[current_cc_card]
                if card > 1:
                    continue
                elif card == 0:
                    pos = spaces.index('GO')
                elif card == 1:
                    pos = spaces.index('JAIL')
                current_cc_card = (current_cc_card + 1)%16
            elif pos in ch_indexes:
                card = ch_order[current_ch_card]
                if card > 9:
                    continue
                elif card == 0:
                    pos = spaces.index('GO')
                elif card == 1:
                    pos = spaces.index('JAIL')
                elif card == 2:
                    pos = spaces.index('C1')
                elif card == 3:
                    pos = spaces.index('E3')
                elif card == 4:
                    pos = spaces.index('H2')
                elif card == 5:
                    pos = spaces.index('R1')
                elif card in [6,7]:
                    moved = False
                    for rail in r_indexes:
                        if pos < rail and not moved:
                            pos = rail
                            moved = True
                    if not moved:
                        pos = r_indexes[0]
                elif ch_order[current_ch_card] == 8:
                    moved = False
                    for util in u_indexes:
                        if pos < util and not moved:
                            pos = util
                            moved = True
                    if not moved:
                        pos = u_indexes[0]
                elif ch_order[current_ch_card] == 9:
                    pos -= 3
                    found = False
                current_ch_card = (current_ch_card + 1)%16
        visited[pos][0] += 1
        # if i%10000 == 0:
        #     print(i)

    answer = ''
    for i in range(3):
        answer += "{:02d}".format(sorted(visited,reverse = True)[i][1])
    print(answer)

#print(sorted(visited,reverse = True))