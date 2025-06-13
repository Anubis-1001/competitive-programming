def countRangeSum(nums, lower, upper):
    n = len(nums)
    ranges = [0]*n
    for i in range(n):
        ranges[i]=ranges[i-1]+nums[i]

    result = countRanges(ranges, lower, upper)
    return result


def countRanges(nums, lower, upper):
    if len(nums) == 1:
        return 1 if lower <= nums[0] <= upper else 0

    mid = len(nums)//2
    count_r = countRanges(nums[mid:], lower, upper)
    count_l = countRanges(nums[:mid], lower, upper)
    result = count_l+count_r

    nums_r = sorted(nums[mid:])
    nums_l = sorted(nums[:mid])
    l, u = 0, 0
    for num in nums_r:
        while l < mid and num-nums_l[l] > upper: l+=1
        while u < mid and num-nums_l[u] >= lower: u+=1
        result += max(0, u-l)

    return result


print("Result:", countRangeSum([-2, 5, -1], -2, 2))
print("Result:", countRangeSum([0], 0, 0))
print("Result:", countRangeSum([0,-3,-3,1,1,2], 3, 5))


