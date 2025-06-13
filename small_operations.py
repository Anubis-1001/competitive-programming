#https://codeforces.com/problemset/problem/2114/F

def get_min_ops(x, y, k):
    #print(x, y, k)
    gcd = GCD(x, y)
    x //= gcd
    y //= gcd
    ops = 0
    div = k
    while div > 1:
        if x%div == 0:
            x//=div
            ops+=1
        elif y%div == 0:
            y//=div
            ops+=1
        else:
            div-=1
        print(ops, x, y, div)

    return ops if x == 1 and y == 1 else -1

def GCD(A, B):
    if A%B == 0:
        return B
    else:
        return GCD(B, A%B)


#print(get_min_ops(4, 6, 3))
#print(get_min_ops(4, 5, 3))
#print(get_min_ops(4, 6, 2))
#print(get_min_ops(10, 45, 3))
#print(get_min_ops(780, 23, 42))
#print(get_min_ops(11, 270, 23))
print(get_min_ops(1, 982800, 13))
#print(get_min_ops(1, 6, 2))
