l, r = list( map( int, input().split() ) )

if abs(l-r) > 2:
    print( ( l+r )*2 )
elif abs(l-r) == 2 or abs(l-r) == 0:
    print( (l+r)*3//2 )
else:
    print( l+r)
