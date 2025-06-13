def makesquare(matchsticks):
    mask=0
    t=sum(matchsticks)
    if t%4!=0: return False
    t=t//4

    for x in range(0, 4):
        dp=[0]*(t+1)
        for m in range(0, len(matchsticks)):
            if mask & 1<<m == 0:
                dp[matchsticks[m]]=1<<m
                for x in range(0, len(dp)):
                    if dp[x] > 0 and x+matchsticks[m]<=t:
                        dp[x+matchsticks[m]]|=1<<m
                    if x+matchsticks[m] == t:
                        mask|=dp[x+matchsticks[m]]
                        break

    return mask == 2**len(matchsticks)-1

print(makesquare([1,1,2,2,2]))
print(makesquare([3,3,3,3,4]))
print(makesquare([5,5,5,5,4,4,4,4,3,3,3,3]))
