def search(nums, target):
    s=0
    e=len(nums)-1

    while s<e:
        m=(s+e)//2
        if nums[m] == target:
            return m
        if nums[s] <= nums[m]:
            if target >= nums[s]  and target <= nums[m]:
                e=m-1
            else:
                s=m+1
        else:
            if target >= nums[s]  or target <= nums[m]:
                e=m-1
            else:
                s=m+1
    if nums[s] != target:
        return -1
    return s

print(search([4,5,6,7,0,1,2], 4))
print(search([1], 1))
