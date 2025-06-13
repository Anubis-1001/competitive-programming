


def canIWinRecursive(maxChoosableInteger, desiredTotal):
    dp=[[False]*(desiredTotal+1) for _ in range(0, 2**maxChoosableInteger)]
    for desired in range(0, desiredTotal+1):
        for s in range(0, 2**maxChoosableInteger):
            for x in range(0, maxChoosableInteger):
                if s & 1<<x == 0:
                    if desired-x >= 0:
                        dp[s][desired]|=( not dp[s | 1<<x ][desired-x-1] )
                    else:
                        dp[s][desired]=True
                    if dp[s][desired]: break

    return dp[0][desiredTotal-1]

print(canIWinRecursive(15, 16))
