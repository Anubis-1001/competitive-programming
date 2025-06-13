from heapq import heappush, heappop

def maxSizeSlices(slices):
    n = len(slices)
    n_s = [0]*n
    heap = []
    for i in range(n):
        n_s[i]=[(i-1)%n, (i+1)%n]
        heappush(heap, ( slices[i], i) )

    for i  in [1, 7, 11]:
        if n_s[i] != -1:
            n_s[n_s[n_s[i][0]][0]][1] = n_s[n_s[i][1]][1]
            n_s[n_s[n_s[i][1]][1]][0] = n_s[n_s[i][0]][0]
            n_s[n_s[i][0]]=-1
            n_s[n_s[i][1]]=-1
            n_s[i]=-1
    print(n_s)

maxSizeSlices([1,2,3,4,5,6,7,8,9,10,11,12])
