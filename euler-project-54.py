import time 
time.sleep(2)
facecards = ['T','J','Q','K','A']
player1wins = 0
n = 0
with open('euler-project-54-text-file.txt') as f:
    n+=1
    line = f.readline()
    while line:
        hands = [line.split(' ')[0:5],line.split(' ')[5:10]]
        hands[1][4] = hands[1][4][0:2]
        handvalues = [0,0]
        for i in range(2):
            nums = []
            suits = set()
            HC = ['','']
            for card in hands[i]:
                suits.add(card[1])
                if card[0] in facecards:
                    nums.append(facecards.index(card[0])+10)
                else:
                    nums.append(int(card[0]))
            nums = sorted(nums)
            maxcount = 1
            for num in nums:
                if nums.count(num)>maxcount:
                    maxcount = nums.count(num)
                    HC[i] = num
            numsset = set(nums)
            if maxcount == 2:
                if len(numsset) == 4:
                    handvalues[i] = 1
                elif len(numsset) == 3:
                    handvalues[i] = 2
                continue
            elif maxcount == 3:
                if len(numsset) == 3:
                    handvalues[i] = 3
                elif len(numsset) == 2:
                    handvalues[i] = 6
                continue
            elif maxcount == 4:
                handvalues[i] = 7
                continue
            flush = False
            straight = True
            if len(suits) == 1:
                flush = True
            for j in range(4):
                if not nums[j+1] == nums[j] + 1:
                    straight = False
                    break
            if nums == [2,3,4,5,14]:
                straight = True
                nums = [1,2,3,4,5]
            if not straight and not flush:
                continue
            elif not flush and straight:
                HC[i] = hands[i][4]
                handvalues[i] = 4
                continue
            elif flush and not straight:
                HC[i] = hands[i][4]
                handvalues[i] = 5
                continue
            else:
                handvalues[i] = 8
                HC[i] = hands[i][4]
                continue
        if handvalues[0] > handvalues[1]:
            player1wins += 1
            print('win')
        elif handvalues[0] == handvalues[1]:
            if handvalues[0] in [3,4,5,6,7,8,9]:
                if HC[0]>HC[1]:
                    player1wins +=1
                    print('win')
                else:
                    print('no win')
            else:
                advnums = [[],[]]
                maxnums = [[],[]]
                for i in range(2):
                    for card in hands[i]:
                        if card[0] in facecards:
                            advnums[i].append(facecards.index(card[0])+10)
                        else:
                            advnums[i].append(int(card[0]))
                    advnums[i] = sorted(advnums[i], reverse = True)
                    for num in advnums[i]:
                        if advnums[i].count(num) == maxcount:
                            maxnums[i].append(num)
                    maxnums[i] = sorted(maxnums[i], reverse = True)
                for a in range(len(maxnums[0])):
                    if maxnums[0][a] > maxnums[1][a]:
                        player1wins += 1
                        print('win')
                        break
                    elif maxnums[0][a] == maxnums[1][a]:
                        if a == len(maxnums[0])-1:
                            for p in range(5):
                                if advnums[0][p] > advnums[1][p]:
                                    player1wins += 1
                                    print('win')
                                    break
                                elif advnums[0][p] < advnums[1][p]:
                                    print('no win')
                                    break
                                else:
                                    continue
                        continue
                    else:
                        print('no win')
                        break
        else:
            print('no win')

        print('---')
        line = f.readline()
print(player1wins)
# 9 = royal flush
# 8 = straight flush
# 7 = 4 of a kind
# 6 = full house
# 5 = flush
# 4 = straight
# 3 = 3 of a kind
# 2 = 2 pairs
# 1 = 1 pair
# 0 = high card

