import pprint

def splitArraySameAverage(nums):
    n = len(nums)
    t = sum(nums)/n
    dp=[ [-1]*( int(t*n) + 1 ) for _ in range(n+1) ]
    def dfs(bm, l, s):
        print(bm)
        if dp[l][s] == -1: dp[l][s] = bm
        if l > n//2: return False

        for i in range(l):
            h=int(t*(i+l))-s
            if  ( h==t*(i+l)-s and dp[i][h] != -1 ) and (dp[i][h] & bm == 0): return True

        for x in range(n):
            if not bm & 1<<x:
                if dfs(bm | 1<<x, l+1, s+nums[x]):
                    return True

        return False

    return dfs(0, 0, 0)
#print(splitArraySameAverage([1,2,3,4,5,6,7,8]))
#print(splitArraySameAverage([3, 1]))
#print(splitArraySameAverage([1,1]))
#print(splitArraySameAverage([5,6,7,11, 16]))
#print(splitArraySameAverage([0,13,13,7,5,0,10,19,5]))
#print(splitArraySameAverage([3,3,2]))
print(splitArraySameAverage([60,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]))
