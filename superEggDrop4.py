def superEggDrop(k, n):
    if k == 1:
        return n
    dp=[[10002]*(n+1) for _ in range(0, k+1)]
    dp[1]=list(range(0, n+1))
    for m in range(0, k+1):
        dp[m][0]=0
    #print(dp)
    for x in range(1, k+1):
        for j in range(1, n+1):
            for s in range(1, j+1):
                dp[x][j]=min(dp[x][j], 1+max(dp[x-1][s-1], dp[x][j-s]))
    return dp
    #return dp[k][n]



#print(superEggDrop(1, 2))
#print(superEggDrop(2, 6))
#print(superEggDrop(3, 14))
#print(superEggDrop(3, 4))
#print("k=2")
#print(superEggDrop(2, 2))
#print(superEggDrop(2, 3))
#print(superEggDrop(2, 4))
#print(superEggDrop(2, 5))
#print(superEggDrop(2, 6))
#print(superEggDrop(2, 7))
#print(superEggDrop(3, 14))
#print(superEggDrop(4, 5000))
print(superEggDrop(3, 25))

