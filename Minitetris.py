a, b, c = list( map(int, input().split() ) )

n = 2*a

if c >= 2:
    n+=3+2*b

if c > 2:
    n+= 3*( (c-2)//2 )

print(n)
