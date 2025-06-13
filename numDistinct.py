def numDistinct(s, t):
    dp=[[0]*len(s) for _ in t]
    for l in range(0, len(t)):
        for l2 in range(0, len(s)):
            dp[l][l2]=dp[l][l2-1]
            if t[l]==s[l2]:
                if l > 0 and l2>0:
                    dp[l][l2]+=dp[l-1][l2-1]
                elif l == 0:
                    dp[l][l2]+=1

    return dp[len(t)-1][len(s)-1]


print(numDistinct("babgbag", "bag"))
print(numDistinct("rabbbit", "rabbit"))
print(numDistinct("ccc", "c"))
print(numDistinct("ddd", "dd"))
