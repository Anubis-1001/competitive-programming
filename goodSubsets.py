#Leetcode 1994

def numberOfGoodSubsets(nums):
    primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    subsets = [0]
    count=0
    for x in nums:
        print(x, "++")
        bitmask = getBM(x, primes)
        if bitmask == -1: continue
        curr = []

        for s in subsets:
            if s & bitmask == 0:
                curr.append( s | bitmask )
                if s | bitmask > 0 : count+=1

        subsets+=curr

    return count

def getBM(number, primes):
    bm=0
    for i in range(10):
        if number % primes[i] == 0: bm|=1<<i
        if number % primes[i]**2 == 0: return -1

    return bm


print(numberOfGoodSubsets([1,2,3,4])) #6
print(numberOfGoodSubsets([4,2,3,15])) #5
print(numberOfGoodSubsets([6,8,1,8,6,5,6,11,17])) #62
print(numberOfGoodSubsets([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])) #62
#print(getBM(1,[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]))
