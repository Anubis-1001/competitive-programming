from heapq import heappush, heappop

graph = dict()

count_l = dict()
def get_count(s):
    a = [0]*26
    for l in s:
        a[ord(l)-97]+=1

    return a

def doublet(s1, s2):
    if len(s1) != len(s2): return False
    a1 = count_l[s1]
    a2 = count_l[s2]

    count=0
    for v1, v2 in zip(a1, a2):
        if v1 != v2: count+=1
        if count > 2: return False

    return count == 2

while True:
    x = input()
    if x == "":
        break

    graph[x] = []
    count_l[x] = get_count(x)
    for k in graph.keys():
        if doublet(k, x):
            graph[x].append(k)
            graph[k].append(x)

def shortest(start, end, h):
    buffer=[ (0, start, '') ]
    while buffer:
        l, curr, prev = heappop(buffer)
        for child in graph[curr]:
            if l+1 < h[child][1] and child != prev:
                heappush(buffer, (l+1, child, curr))
                h[child] = (curr, l+1)
                if child == end:
                    return

try:
    while True:
        s, e = input().split(" ")
        v = dict()

        for k in graph.keys(): v[k] = ("", float("inf") )

        shortest(s, e, v)
        if v[e][1] == float("inf"):
            print("No solution.")
            continue

        path=[]
        p=e
        while p != s:
            path.insert(0, p)
            p=v[p][0]
        print(s)
        for x in path: print(x)
        print()

except EOFError:
    pass
