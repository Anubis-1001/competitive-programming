T = int(input())

def parseISBN13(ISBN):
    if valid_checksum(ISBN) == 'invalid':
        return 'invalid'
    checksum=38
    i = 3
    for l in ISBN[:-1]:
        if l != '-':
            if l == 'X':
                l='10'
            checksum+=i*int(l)
            i = ( i + 2 ) % 4

    lastdigit =( 10-checksum%10 ) % 10
    ISBN13 = '978-'+ISBN[:-1]+str(lastdigit)

    return ISBN13

def valid_checksum(ISBN):
    if ISBN[0] == '-' or  ISBN[-1] == '-':
        return 'invalid'

    count=10
    h_count=0
    checksum=0
    flag=False
    for l in ISBN:
        if l != '-':
            flag=False
            if l == 'X':
                l=10
            checksum+=count*int(l)
            count-=1
        else:
            if flag == True:
                return 'invalid'
            h_count+=1
            flag=True

    if count != 0 or ( h_count >= 3 and ISBN[-2] != '-' ):
        return 'invalid'

    return 'valid' if  checksum%11 == 0 else 'invalid'

for x in range(T):
    ISBN10 = input()
    print(parseISBN13(ISBN10))

#                  '0987654321'
#print(parseISBN13('3-540-4258-02'))
#print(parseISBN13('3-540-42580-2'))
#print(parseISBN13('039428013X'))
#print(parseISBN13('0-14-028333-3'))
