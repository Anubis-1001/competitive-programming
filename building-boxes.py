import math

def minimunBoxes(n):
    k = math.floor((6*n)**(1/3))+1
    if k**3-k > 6*n:
        k-=1
    result = (k-1)*k/2
    remainder = n-(k**3-k)/6
    result+= math.ceil( ( -1 + (1+4*2*remainder)**(1/2) )/2 )
    return int(result)

print(minimunBoxes(288))
