#leetcode 2386
from heapq import heappush, heappop

def kSum(nums, k):
    pos_sum=0
    heap=[]
    for i, n in enumerate(nums):
        if n >= 0:
            pos_sum+=n
        else:
            nums[i]=-n

    nums.sort()
    heappush(heap, 0)
    prev=[0]
    for x in nums:
        if len(heap)==k and x > -heap[0]:
            return pos_sum+heappop(heap)
        nxt=[]
        for p in prev:
            nxt.append(p+x)

        for n_e in nxt:
            if -heap[0] > n_e or len(heap) <= k:
                heappush(heap, -n_e)
            if len(heap) > k:
                heappop(heap)
        prev+=nxt
        prev=sorted(prev)[:k]

    print(prev)
    return pos_sum+heappop(heap)

print(kSum([2,4,-2], 5))
print(kSum([1,-2,3,4,-10,12], 16))
print(kSum([-1, 1], 1))
