from pprint import pprint
def getMaxRepetitions(s1, n1, s2, n2):
    dp = [ [-1]*len(s1) for _ in range(len(s2)) ] 
    i2 = 0
    n = len(s2)
    s1_count = 0
    flag=True
    equities = [0]
    while flag:
        prev=i2
        for i1 in range(len(s1)):
            if s1[i1] == s2[i2%n]:
                #print(s2, ":", s1)
                #print(i2, i1)
                if dp[i2%n][i1] > -1:
                    flag=False
                dp[i2%n][i1] = s1_count
                i2+=1
        if prev == i2:
            return 0
        s1_count+=1
        equities.append(i2//n)

    print(equities)
    s1_count-=1
    print( n1, s1_count, i2, n)
    r = ( n1//( s1_count) )*(i2//n)
    print("--", r)
    r+= equities[n1%( s1_count )]
    return r//n2


pprint(getMaxRepetitions("bacaba", 3, "abacab", 1))
pprint(getMaxRepetitions("acb", 4, "ab", 2))
pprint(getMaxRepetitions("acb", 1, "acb", 1))
#pprint(getMaxRepetitions("musicforever", 10, "lovelive", 100000))
