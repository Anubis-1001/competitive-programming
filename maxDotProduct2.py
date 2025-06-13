def maxDotProduct(nums1, nums2):
    if ( max(nums1) < 0 and min(nums2) > 0 ) or ( max(nums2) < 0 and min(nums1) > 0 ):
        return max(max(nums1)*min(nums2),  max(nums2)*min(nums1))
    dp = [ [0]*(len(nums2)+1) for _ in range(0, len(nums1)+1) ]
    #dp[1][1]=nums[0]*nums[0]
    for i in range(1, len(dp)):
        for j in range(1, len(dp[0])):
            dp[i][j]=max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]+nums1[i-1]*nums2[j-1])

    return dp[len(nums1)][len(nums2)]

#print(maxDotProduct([2,1,-2,5], [3,0,-5]))
print(maxDotProduct([2,1,-2,5],  [3,0,-6]))
