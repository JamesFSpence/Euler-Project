import math

max = 0
maxd = 0
for d in range(2,1000):
    keepGoing = True
    nextrem = 10 #the number we divide d into
    rems = [] #keeps track of the remainders we divide into
    while keepGoing:
        while d > nextrem: #i.e r is too small so we tag a zero on the end
            nextrem*=10
            rems.append('') #keeps track of the position of the decimal we divide into by putting blanks
        nextrem = nextrem%d #find next remainder
        if nextrem == 0: #if zero we don't have recurrence
            keepGoing = False
        elif nextrem in rems: #if we've already seen this remainder we know the decimal repeats from here onward
            length = len(rems) - rems.index(nextrem) #length of repeating part
            if length > max: #seting the new maxlength and maxd values
                max = length
                maxd = d
            keepGoing = False
        else:
            rems.append(nextrem)
            nextrem*=10
print(maxd)
print(max)