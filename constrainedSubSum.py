from heapq import heappush, heappop

def constrainedSubsetSum(nums, k):
    heap = [(0, -10)]
    max_sum = float("-inf")

    for i in range(len(nums)):
        while heap and i - heap[0][1] > k:
            heappop(heap)
        if heap:
            value = max(-heap[0][0], 0) + nums[i]
        else:
            value = nums[i]
        if value > max_sum: max_sum = value
        heappush(heap, (-value, i))

    return max_sum



print(constrainedSubsetSum([10,2,-10,5,20], 2))
print(constrainedSubsetSum([10,-2,-10,-5,20], 2))
