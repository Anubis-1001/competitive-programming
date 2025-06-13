def getMaxRepetitions(s1, n1, s2, n2):
    i2 = 0
    s1_count = 0
    n = len(s2)
    equities = [0]
    while (i2 % n != 0 or i2 == 0) and s1_count < 40000:
        for l in s1:
            if l == s2[i2%n]: i2+=1
        s1_count+=1
        equities.append(i2//n)

    result = (n1//s1_count)*(i2//n)
    result+= equities[n1%s1_count]
    result = result//n2
    return result

#print(getMaxRepetitions("acb", 12, "abc", 2))
print(getMaxRepetitions("bacaba", 3, "abacab", 1))
