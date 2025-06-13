#leetcode 940
def distinctSubseqII(self, s: str) -> int:
    df = [0]*(len(s)+1)
    df[0]=1
    i=1
    for l in range(1, len(s)+1):
        df[i]=2*df[i-1]
        for j in range(l-1, 0, -1):
            if s[j-1] == s[l-1]:
                df[i]-=df[j-1]
                break
        i+=1

    return (df[len(s)]-1)%(10**9+7)


print(distinctSubseqII(0, "aaa"))
print(distinctSubseqII(0, "aba"))
print(distinctSubseqII(0, "abc"))
print(distinctSubseqII(0, "zchmliaqdgvwncfatcfivphddpzjkgyygueikthqzyeeiebczqbqhdytkoawkehkbizdmcnilcjjlpoeoqqoqpswtqdpvszfaksn"))
