def canJump(nums):
    maxRange=[i+nums[i] for i in range(0, len(nums))]
    k=len(nums)-1
    for j in range(len(maxRange)-1, -1, -1):
        if  maxRange[j] >= k:
            k=j

    return k==0

print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))

