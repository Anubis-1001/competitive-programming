from heapq import heappush, heappop

heap=[]

for x in [ (2,10), (1, 11), (2, 3), (1, -1), (2, 2), (1, 10), (1, 20), ( 2, 20)]:
    heappush(heap, x)

while heap:
    print(heappop(heap))
