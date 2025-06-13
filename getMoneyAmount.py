def getMoneyAmount(n):
    money=0
    current=0
    for x in range(n, 0, -4):
        if x < 4 and x > 1:
            money=max(money, current+x-1)
        else:
            current+=2*x-4
            money=max(money, current)
            current-=x-1
            if x == n:
                current=n-3

        print("money", money, x)
        print("current", current, x)

    return money

#print(getMoneyAmount(13))
#print(getMoneyAmount(3))
#print(getMoneyAmount(16))
#print(getMoneyAmount(6))
print(getMoneyAmount(25))
