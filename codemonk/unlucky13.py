

T = int(input())

max_i = 10**9 + 9
for _ in range(0, T):
    N = int(input())
    count = 0
    count_x_1 = 0
    count_x = 0
    if N < 2:
        print( 10**N )
        continue
    for x in range(2, N + 1 ):
        count =  ( 10*count + 10**( x-2 ) - count_x_1 ) % ( max_i )
        count_x_1 = count_x
        count_x = count

    print( ( 10**( N % max_i ) - count ) % max_i )
