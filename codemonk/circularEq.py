from math import comb

T = int(input())

for _ in range(T):
    n = int(input())
    divisor = 1
    power = 1
    count = 0
    while ( divisor <= n ):
        if n % divisor == 0 and ( n / divisor ) <= 9*power:
            digit_sum =  n // divisor
            count += comb( digit_sum+power-1, power-1 )

        divisor = divisor*10+1
        power+=1

    print( count )
