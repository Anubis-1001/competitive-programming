import bisect

def containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff):
    heap=[-10**9-10, 2*10**9]

    i=0
    for x in nums:
        print(heap)
        if len(heap) > indexDiff+2:
            heap.pop(heap.index(nums[i]))
            i+=1

        idx=bisect.bisect_left(heap, x)
        heap.insert(idx, x)
        print(heap)
        print(idx)
        if abs(heap[idx]-heap[idx-1]) <= valueDiff or abs(heap[idx]-heap[idx+1]) <= valueDiff:
            return True

    return False


print(containsNearbyAlmostDuplicate([1,5,9,1,5,9],2, 3))

