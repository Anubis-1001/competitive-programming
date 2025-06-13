def countSmaller(nums):

    n = len(nums)
    cnts=[0]*n
    idx=[ i for i in range(n) ]
    countWithMerge(idx, nums, cnts)

    return cnts

def countWithMerge(idx, nums, counts):
    if len(idx) == 1: return idx

    mid = len(idx)//2
    halve_l = countWithMerge(idx[:mid], nums, counts)
    halve_r = countWithMerge(idx[mid:], nums, counts)
    result = []

    j = 0
    for n in halve_l:
        while j < len(halve_r) and nums[n] > nums[halve_r[j]]: 
            result.append(halve_r[j])
            j+=1
        counts[n]+=j
        result.append(n)

    if j < len(halve_r):
        result+=halve_r[j:]

    return result

print( countSmaller([5,2,6,1]) )
print( countSmaller([-1]) )
print( countSmaller([-1, -1]) )

