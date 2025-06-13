#Leetcode 805

def splitArraySameAverage(nums):
    n = len(nums)
    if n == 1: return False
    t = sum(nums)/n
    half_1, half_2 = nums[:n//2], nums[n//2:]

    sums = [ [0]*(n//2 + 2)  for _ in range(sum(half_2)+30) ]
    sums[0][0]=1
    subavg = [(0, 0)]

    for n2 in half_2:
        buffer=[]
        for s, l  in subavg:
            buffer.append((s+n2, l+1))
            sums[s+n2][l+1]=1

        subavg+=buffer

    subavg = [(0, 0)]

    for n1 in half_1:
        buffer=[]
        for s, l  in subavg:
            buffer.append((s+n1, l+1))
            #print(buffer[0])
            for i in range(0, n//2+1):
                h=t*(i+l+1)-s-n1
                print(h)

                if  abs(h-int(h)) < 1/10**7 and 0 <= h < len(sums) and  sums[int(h)][i] == 1 and i+l+1 < n: return True

        subavg+=buffer

    return False


#print(splitArraySameAverage([60,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]))
#print(splitArraySameAverage([1,2,3,4,5,6,7,8]))
#print(splitArraySameAverage([1,3]))
#print(splitArraySameAverage([1,1]))
#print(splitArraySameAverage([5,6,7,11, 16]))
#print(splitArraySameAverage([0,13,13,7,5,0,10,19,5]))
#print(splitArraySameAverage([3,1]))
#print(splitArraySameAverage([1, 6, 1]))
#print(splitArraySameAverage([18,10,5,3]))
#print(splitArraySameAverage([3,1,2]))
print(splitArraySameAverage([4, 4, 4, 4, 4, 4, 5, 4, 4, 4, 4, 4, 4, 5]))
#print(splitArraySameAverage([9990,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]))
#print(splitArraySameAverage([8,6,7,7,2]))
#print(splitArraySameAverage([1865,2885,6227,3222,2726,1710,1775,716,8901,8283,9082,5676,5513,9462,4512,268,4636,129,8196,1722,2583,6497,5181,2333,2067,2653,5246,3676,1566,9768]))
