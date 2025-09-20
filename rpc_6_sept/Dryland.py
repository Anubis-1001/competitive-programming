h, w = list( map( int, input().split(" ") ) )

pr = [0]*w
max_square=0

def get_max_square(rt):
    span = [-1]*len(rt)
    q=[]

    for i,x in enumerate(rt+[-1]):
        while len(q) > 0 and q[-1][0] > x:
            span[q[-1][1]]+=i-q[-1][1]
            q.pop()

        q.append((x,i))

    q=[]
    
    for i,x in enumerate(rt[::-1]+[-1]):
        while len(q) > 0 and q[-1][0] > x:
            span[len(rt)-q[-1][1]-1]+=i-q[-1][1]
            q.pop()

        q.append((x,i))
        
    max_area=0

    for i in range(len(span)):
        area=span[i]*rt[i]
        max_area=max(area, max_area)

    return max_area

for _ in range(h):
    cr = list( map( int, list(input()) ) )
    rt = [ (x+y)*x for x, y in zip(cr,pr) ]
    pr = rt
    local_max=get_max_square(rt)
    max_square=max(max_square, local_max)

print(max_square)
