def nearestPalindromic(n):
    l = len(n)
    if l==1:
        return str(int(n)-1)

    k=n[:l//2]
    if l%2==1:
        k+=n[l//2]
    k+=n[:l//2][::-1]
    if l%2==1:
        m=int(k)+10**(l//2)
    else:
        m=int(k)+10**(l//2)+10**(l//2-1)


    s="9"*(l-1)
    diffk= abs(int(k)-int(n))
    diffm= abs(int(m)-int(n))
    diffs= abs(int(s)-int(n))

    if diffm > diffk:
        if l%2==1:
            m=int(k)-10**(l//2)
        else:
            m=int(k)-10**(l//2)-10**(l//2-1)
    
    diffm= abs(int(m)-int(n))

    if diffs > diffk:
        s=str(10**l+1)
    diffs= abs(int(s)-int(n))

    if diffk == 0: diffk=100000
    if diffm == 0: diffm=100000
    if diffs == 0: diffs=100000

    print(m, k, s)
    if diffk < diffm and diffk < diffs:
        return k 
    elif diffm < diffk and diffm < diffs:
        return str(m)
    elif diffs < diffk and diffs < diffm:
        return s
    else:
        if diffs==diffm:
            return str(min(int(s), int(m)))
        if diffs==diffk:
            return str(min(int(s), int(k)))
        if diffk==diffm:
            return str(min(int(k), int(m)))

#print(nearestPalindromic("12334"))
#print(nearestPalindromic("2321"))
#print(nearestPalindromic("21"))
#print(nearestPalindromic("23"))
#print(nearestPalindromic("2322"))
#print(nearestPalindromic("1"))
#print(nearestPalindromic("123"))
#print(nearestPalindromic("10"))
print(nearestPalindromic("11"))
#print(nearestPalindromic("88"))
#print(nearestPalindromic("99"))
