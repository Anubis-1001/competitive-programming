def maxSubArray(nums, i, c, m):
    if i >= len(nums):
        return m
    c += nums[i]
    if c < 0:
        c = 0
    if c > m:
        m = c
    return maxSubArray(nums, i+1, c, m)


print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4],0,0,0))
print(maxSubArray([1],0,0,0))
print(maxSubArray([5,4,-1,7,8],0,0,0))
print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4],0,0,0))
