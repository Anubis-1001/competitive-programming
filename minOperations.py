def minOperations(nums):
    op=0
    i=len(nums)-1
    while i > 0:
        if nums[i] < nums[i-1]:
            while i> 0 and nums[i] < nums[i-1]:
                nums[i-1]=getMinDiv(nums[i-1])
                if nums[i-1] == -1 or nums[i] < nums[i-1]:
                    return -1
                i-=1
                op+=1
        else:
            i-=1

    return op



def getMinDiv(num):
    i=2
    while i*i <= num:
        if num%i==0: return i
        i+=1

    return -1

print(minOperations([25,7]))
print(minOperations([1,1,1,1]))
print(minOperations([7,7,6]))
print(minOperations([9,2]))
