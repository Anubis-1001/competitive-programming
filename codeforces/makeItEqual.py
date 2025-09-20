t=int(input().strip())


def setEqual(nums):
    target=sum(nums)//len(nums)
    minimun=-1
    for t in [target, target-1, target-2]:
        if minimun == -1:
            minimun=setEqualAux(nums, t)
        else:
            new_ops=setEqualAux(nums, t)
            if new_ops != -1:
                minimun=min(minimun, new_ops)

    return minimun

def setEqualAux(nums, target):
    eqCount=0
    i=0
    opCount=0
    prevOpCount=0
    n=len(nums)
    while eqCount < n:
        if nums[i] >= target+2:
            nums[i]-=2
            nums[(i+1)%n]+=1
            eqCount=0
            opCount+=1
        elif nums[i] == target:
            eqCount+=1
        else:
            eqCount=0
        i=(i+1)%n
        if i == 0:
            if prevOpCount == opCount:
                return -1
            prevOpCount=opCount

    return opCount


for _ in range(t):
    n=input().strip()
    arr=[int(x) for x in input().strip().split()]
    print(setEqual(arr))

