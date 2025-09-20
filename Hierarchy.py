N = int( input() )

childs = [ set() ] * N
parents = [0] * N

for i in range(N-1):
    p, e = list( map(int, input().split() ) )
    childs[p-1].add(e-1)
    parents[e-1]+=1

Q = int( input() )

def is_parent_of(a, b):
    buffer = [a]
    while len(buffer) > 0:
        d = buffer.pop(0)
        if d == b:
            return True
        for x in childs[d]:
            buffer.append(x)
    return False
        
if any( map( lambda x: x > 1, parents ) ):
    print("NE")
else:
    print("DA")

for j in range(Q):
    a, b = list( map(int, input().split() ) )

    if is_parent_of(a-1, b-1):
        childs[a-1].remove(b-1)
        childs[b-1].add(a-1)
        parents[a-1]+=1
        parents[b-1]-=1
    else:
        childs[b-1].remove(a-1)
        childs[a-1].add(b-1)
        parents[b-1]+=1
        parents[a-1]-=1

    if parents[a-1] > 1 or parens[b-1] > 1:
        print("NE")
    else:
        print("DA")
