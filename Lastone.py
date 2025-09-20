import math

h1, d1, r1 = list( map(int, input().split() ))
h2, d2, r2 = list( map(int, input().split() ))

t1 = ( math.ceil( h2/d1 ) - 1 ) * r1 + 0.5
t2 = ( math.ceil( h1/d2 ) - 1 ) * r2 + 0.5

if t1 < t2:
    print("player one")
if t2 < t1:
    print("player two")
if t2 == t1:
    print("draw")
