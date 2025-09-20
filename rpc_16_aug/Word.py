h1, w1 = list(map(int, input().split()))

pat = []

for _ in range(h1):
    pat.append( list( list( input() ) )  )

h2, w2 = list(map(int, input().split()))

grid = []


for _ in range(h2):
    grid.append( list( list( input() ) )  )


result = [ [ '.' ] * w2 for x in range(h2)  ]

flag = False

for i in range( h2-h1+1 ):
    for j in range( w2-w1+1 ):

        flag = False
        for k in range(h1):
            if flag:
                break
            for l in range(w1):
                if pat[k][l] != grid[i+k][j+l]:
                    flag = True
                    break
                if k == h1-1 and l == w1-1:
                    result[i][j] = 1

for i in range(h2-1, -1, -1):
    for j in range(w2-1, -1, -1):
        if result[i][j] ==  1:
            for k in range(h1):
                for l in range(w1):
                    result[i+k][j+l] = pat[k][l]



print( '\n'.join(list( map( lambda x: ''.join(x), result ) ) ) )
