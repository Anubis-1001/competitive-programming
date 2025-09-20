n = int( input() )

t = []
for _ in range(n):
    t.append( tuple( map(int, input().split() ) ) )

c = min(2, n)
i = 1
right = False

while i < n-1:
    if t[i][0] - t[i-1][0] - right*t[i-1][1] > t[i][1]:
        c+=1
        right=False
    elif t[i+1][0] - t[i][0] > t[i][1]:
        c+=1
        right=True
    else:
        right=False
    i+=1

print(c) 
