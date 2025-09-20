strng = input()
m = int( input() )
ops = list( map(int, input().split() ) )

ops = list( map( lambda x:  m-x if x > ( len(strng)+1 )//2 else x, ops) )

ops.sort()

str_arr = list(strng)

def swap(strng, p):
    if p == 1:
        return strng[::-1]
    s , e = min(p-1, len(strng)-p), max(p-1, len(strng)-p)
    res_s = strng[:s]
    res_e = strng[e+1:]
    res_m = strng[e:s-1:-1]
    return res_s + res_m + res_e

while ops:
    if len(ops) >= 2 and ops[0] == ops[1]:
        ops.pop(0)
        ops.pop(0)
    else:
        strng = swap(strng, ops[0])
        ops.pop(0)

print(strng)
