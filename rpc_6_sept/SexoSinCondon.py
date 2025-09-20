n = int(input())

if n <= 360:
    print(0)
    exit(0)

if 390 >= n > 360:
    print( n - 360 )
    exit(0)

if n - 45 > 600:
    print( n - 600 )
    exit(0)

if n - 45 > 540:
    print(45)
    exit(0)

if n - 30 > 360:
    x = 0
    if n - 30 > 540:
        x = n-570
    print(min(30+x, 45))
    exit(0)

