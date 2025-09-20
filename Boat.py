n, m, k = list( map(int, input().split() ) )

ins = [-1]*m
prices = [0] * m

for i in range(k):
    p, c = list( map(int, input().split() ) )
    if ins[c-1] != -1:
        if ins[c-1] != p:
            prices[c-1] += abs( p - ins[c-1] )
        else: 
            prices[c-1] += 100
        ins[c-1] = -1
    else:
        ins[c-1] = p

for j in range(m):
    if ins[j] != -1:
        prices[j] += 100


print( " ".join(list( map(str, prices) ) ) )
