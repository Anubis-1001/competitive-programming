from re import search

sequence  = input()

if search(r'[^EO]', sequence) or search(r'OO', sequence) or search('E$', sequence):
    print('INVALID')
    exit(0)


N = 2**47
O = 5

while O <= N:
    i = O
    for n, l in enumerate(sequence[::-1][1:]):
        if l == 'E':
            i*=2
        else:
            if ( i - 1 ) % 3 != 0:
                break
            i=( i-1 ) // 3
        
        if n == len(sequence) - 2:
            print(i)
            exit(0)
    
    O =  O*4+1