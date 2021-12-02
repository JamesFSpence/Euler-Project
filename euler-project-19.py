year = 1900
day = 2

nonleap = [31,28,31,30,31,30,31,31,30,31,30,31]
leap = [31,29,31,30,31,30,31,31,30,31,30,31]

count = 0

while year < 2000:
    year +=1
    if year%4==0:
        if year%100 != 0:
            months = leap
            print(year)
            print('leap')
        else:
            months = nonleap
    elif year%400 == 0:
        months = leap
        print(year)
        print('leap')
    else:
        months = nonleap
    if year == 2000:
        k = 11
    else:
        k = 12
    for j in range(k):
        day = (day+months[j])%7
        if day%7 == 0:
            count +=1
print(count)
print(day)



