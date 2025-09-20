d1 = list( map( int, input().split() ) )
d2 = list( map( int, input().split() ) )
d3 = list( map( int, input().split() ) )

d1.sort()
d2.sort()
d3.sort()

d = [d1, d2, d3]


def get_duplicates(d1, d2):
    res = 0
    for x in d1:
        for y in d2:
            if x == y:
                res+=1

    return res

for i in range(3):
    wr1 = 0
    wr2 = 0
    m1 = 0
    m2 = 0
    b1 = get_duplicates( d[i] , d[ (i+1) % 3 ] )
    b2 = get_duplicates( d[i] , d[ (i+2) % 3 ] )

    for n in d[i]:
        while m1 < 6 and n > d[ (i+1) % 3 ][m1]: m1+=1
        while m2 < 6 and n > d[ (i+2) % 3 ][m2]: m2+=1
        wr1+=m1
        wr2+=m2
    if b1 == 36 or b2 == 36:
        continue
    if wr1/( 36 - b1 ) >= 0.5 and wr2/( 36 - b2 ) >= 0.5:
        print(i+1)
        exit(0)

print('No dice')
