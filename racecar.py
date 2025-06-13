def racecar(target):
    npt=nearest_power_2(target*11)
    dp=[0]*(npt+1)
    power=0
    while 2**power-1 <= npt:
        dp[2**power-1]=power
        power+=1

    for x in range(1, len(dp)):
        np=nearest_power_2(x)
        print(x, np)
        dp[x]=dp[np]+1+dp[np-x] if dp[x]==0 else dp[x]
        print("===")
        print(dp[x], x)
        for r in range(1, x):
            dp[x]=min(dp[x], dp[r]+2+dp[x-r])

    print(dp)
    for z in range(0, 4):
        for m in range(len(dp)-1, 0, -1):
            for k in range(1, m):
                dp[m-k]=min(dp[m-k], dp[m]+dp[k]+1)

    for z in range(0, 4):
        for m in range(1, len(dp)):
            for k in range(1, m):
                if m+k < len(dp):
                    dp[m+k]=min(dp[m+k], dp[m]+dp[k]+2)

    for z in range(0, 4):
        for m in range(len(dp)-1, 0, -1):
            for k in range(1, m):
                dp[m-k]=min(dp[m-k], dp[m]+dp[k]+1)

    for z in range(0, 4):
        for m in range(1, len(dp)):
            for k in range(1, m):
                if m+k < len(dp):
                    dp[m+k]=min(dp[m+k], dp[m]+dp[k]+2)
    print(dp)
    return dp[target]

def nearest_power_2(i):
    p=1
    while p < i:
        p=(p+1)*2-1

    return p

#print(racecar(6))
print(racecar(5))
print(racecar(9))

