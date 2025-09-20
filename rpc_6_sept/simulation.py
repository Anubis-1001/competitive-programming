#l, r = list( map( int, input().split() ) )


l = list( "ABC" )
r = list( "DE" )



print(l,"==",r)

for _ in range(len(l)*2+len(r)*2):
    r.append( l.pop() )
    print(l,"==",r)
    l.insert( 0, r.pop(0) )
    print(l,"==",r)


