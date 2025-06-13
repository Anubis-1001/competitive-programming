def topKFrequent(nums, k):
    h = dict()
    for n in nums:
        if n not in h: h[n]=0
        h[n]+=1

    result = sorted( list( h.keys() ), key=lambda x: -h[x])
    return result[:k]


#print(topKFrequent([1,1,1,2,2,3], 2))
#print(topKFrequent([1], 1))
print(topKFrequent([4,1,-1,2,-1,2,3], 2))
