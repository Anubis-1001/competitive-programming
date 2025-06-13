def smallestNumber(num, t):
    t2=t
    for x in [2,3,5,7]:
        while t2%x==0:
            t2//=x
    if t2 > 1:
        return "-1"

    s=""
    t2=t
    for x in range(9, 1, -1):
        while t2%x==0:
            t2//=x
            s=str(x)+s
    print(s)
    if len(s) > len(num):
        return s
    nums=[int(c) for c in num]
    nums.insert(0, 0)

    return str(int(smallestNumberAux(nums, t, 0, 1)[:-1]))



def smallestNumberAux(nums, t, i, p):
    if i >= len(nums):
        if p%t==0 and p>0:
            return "*"
        return ""
    s=max(0, nums[i])
    for x in range(s, 10):
        if i==0 and x==0:
            r=smallestNumberAux(nums, t, i+1, p)
        else:
            r=smallestNumberAux(nums, t, i+1, p*x)
        if len(r)>0:
            return str(x)+r

    nums[i]=-1
    return ""

print(smallestNumber("1234", 256))
print(smallestNumber("26", 9))
print(smallestNumber("26", 97977600000000))
