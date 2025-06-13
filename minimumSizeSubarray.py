def minSubArrayLen(target, nums):
    tail, head = -1, -1
    f_sum=0
    min_length=float("inf")
    while head < len(nums):
        #print(f_sum)
        if f_sum < target:
            head+=1
            if head < len(nums):
                f_sum+=nums[head]
        elif f_sum >= target:
            tail+=1
            f_sum-=nums[tail]
            min_length=min(min_length, head-tail+1)

    return min_length if min_length != float("inf") else 0

print(minSubArrayLen(7, [2,3,1,2,4,3]))
print(minSubArrayLen(11, [1,1,1,1,1,1,1,1]))
print(minSubArrayLen(213, [12,28,83,4,25,26,25,2,25,25,25,12]))
print(minSubArrayLen(15, [1,2,3,4,5]))

