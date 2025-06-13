def nearestPalindromic(n):
    l = len(n)
    if l==1:
        return str(int(n)-1)

    k=reflection(n)

    #if l%2==1:
    m=reflection(int(k)+10**(l//2))
    j=reflection(int(k)-10**(l//2))
    #else:
     #   m=reflection(int(k)+10**(l//2)+10**(l//2-1))
      #  j=reflection(int(k)-10**(l//2)-10**(l//2-1))

    s="9"*(l-1)
    e=str(10**l+1)
    z=reflection(int(n)+10)
    w=reflection(int(n)-10)

    minDiff=int(n)
    candidates=[]
    for num in [k, m, s, j, e, z, w]:
        num=int(num)
        diff=abs(int(num)-int(n))
        if diff == minDiff:
            candidates.append(num)
        elif diff < minDiff and diff!=0:
            minDiff=diff
            candidates=[num]

    print(candidates)
    return str(min(candidates))

def reflection(num):
    num=str(num)
    l=len(num)
    k=num[:l//2]
    if l%2==1:
        k+=num[l//2]
    k+=num[:l//2][::-1]

    return k
#print(nearestPalindromic("12334"))
#print(nearestPalindromic("2321"))
#print(nearestPalindromic("21"))
#print(nearestPalindromic("23"))
#print(nearestPalindromic("2322"))
#print(nearestPalindromic("1"))
#print(nearestPalindromic("123"))
#print(nearestPalindromic("10"))
#print(nearestPalindromic("11"))
#print(nearestPalindromic("88"))
#print(nearestPalindromic("99"))
#print(nearestPalindromic("11011"))
#print(nearestPalindromic("399999999999"))
#print(nearestPalindromic("11"))
#print(nearestPalindromic("807045053224792883"))
print(nearestPalindromic("190091"))
