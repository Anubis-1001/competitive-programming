from heapq import heappush, heappop
def mincostToHireWorkers(quality, wage, k):
    n = len(quality)
    ratio=[1]*n
    heap=[]
    for i in range(n):
        ratio[i]=(wage[i]/quality[i], quality[i], wage[i])

    ratio = sorted(ratio)
    min_cost=float("inf")
    min_sum = 0
    for r in ratio[:k-1]:
        heappush(heap, (-r[1], r[0]))
        min_sum+=r[1]

    for k in ratio[k-1:]:
        min_cost=min(min_cost, k[2]*( min_sum/k[1] + 1 ) )
        if heap and -heap[0][0] > k[1]:
            min_sum+=heap[0][0]+k[1]
            heappop(heap)
            heappush(heap, (-k[1], k[0]))

    return min_cost

#print(mincostToHireWorkers([3,1,10,10,1], [4,8,2,2,7], 3))
print(mincostToHireWorkers([10,20,5], [70,50,30], 2))
