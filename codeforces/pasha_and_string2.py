strng = input()
m = int( input() )
ops = list( map(int, input().split() ) )
N = len(strng)
ops = list( map( lambda x:  m-x if x > ( N+1 )//2 else x, ops) )

ops.sort()

str_arr = list(strng)

def swap(str_arr, i, j):
    for p in range(i, j):
        str_arr[p-1], str_arr[N-p] = \
        str_arr[N-p], str_arr[p-1]

n = len(ops)


for i in range(0, n, 2):
    if i == n-1:
        swap(str_arr, ops[i], (N+2)//2)
    elif ops[i] != ops[i+1]:
        swap(str_arr, ops[i], ops[i+1])

print( ''.join( str_arr ) ) 
