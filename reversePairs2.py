def countSmaller(nums):

    n = len(nums)
    result = countWithMerge(nums)

    return result[1]

def countWithMerge(nums):
    if len(nums) == 1: return nums, 0

    mid = len(nums)//2
    halve_l, cnt_l = countWithMerge(nums[:mid])
    halve_r, cnt_r = countWithMerge(nums[mid:])
    result = []

    rev_pairs = 0
    cnt_rev_pairs = cnt_l+cnt_r
    j = 0
    for n in halve_l:
        while rev_pairs < len(halve_r) and n > 2*halve_r[rev_pairs]: 
            rev_pairs+=1
        while j < len(halve_r) and n > halve_r[j]: 
            result.append(halve_r[j])
            j+=1
        cnt_rev_pairs+=rev_pairs
        result.append(n)

    if j < len(halve_r):
        result+=halve_r[j:]

    return result, cnt_rev_pairs

print( countSmaller([1,3,2,3,1]) )
print( countSmaller([2,4,3,5,1]) )
#print( countSmaller([-1, -1]) )

