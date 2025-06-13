def minimumOperationsToMakeEqual(x, y):
    dp=[-1]*(max(y,x)+12)
    dp[y]=1
    fillDP(dp, y, 0)
    return dp

def fillDP(dp, x, cnt):
    if x >= len(dp) or x<0: 
        return
    if dp[x] <= cnt and dp[x]!=-1:
        return

    dp[x]=cnt
    fillDP(dp, x+1, cnt+1)
    fillDP(dp, x-1, cnt+1)
    fillDP(dp, x*5, cnt+1)
    fillDP(dp, x*11, cnt+1)

print(minimumOperationsToMakeEqual(25, 30))
print(minimumOperationsToMakeEqual(1, 1))
