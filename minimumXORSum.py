def minimumXORSum(nums1, nums2):
    n = len(nums2)
    dp= [ [-1]*(1<<(n+1)) for _ in range(n) ]

    def dfs(i, bm, x_sum):
        if i == n: return x_sum
        if dp[i][bm] != -1: return dp[i][bm]+x_sum

        min_x_sum=float("inf")
        for x in range(n):
            if not 1<<x & bm:
                m = dfs(i+1, bm | 1<<x, x_sum + ( nums1[i] ^ nums2[x] ) )
                min_x_sum = min(min_x_sum, m)

        dp[i][bm]=min_x_sum-x_sum
        return min_x_sum

    return dfs(0, 0, 0)

print(minimumXORSum([1,0,3], [5,3,4]))
print(minimumXORSum([1,2], [2,3]))
print(minimumXORSum([72,97,8,32,15], [63,97,57,60,83]))
