def longestDupSubstring(s):
    def test(L):
        h_s = set()
        MOD = int(pow(2, 63))-1
        base=26
        base_power=( int(pow(base, L-1)) ) %MOD
        h=0
        for i in range(len(s)):
            if i >= L:
                h=( h - ( ord(s[i-L]) - 96 )*base_power + MOD )%MOD
            h=( h*base + ord(s[i]) - 96 )%MOD

            if h not in h_s: h_s.add(h)
            else: return True, i

        return False, 0

    l, r = 0, len(s)-1
    largest=[0, 0]
    while l <= r:
        mid = (l+r+1)//2
        res = test(mid)
        if res[0]:
            largest=[mid, res[1]]
            l=mid+1
        else:
            r=mid-1
    length, ind = largest
    return s[ind+1-length:ind+1]

#print(longestDupSubstring("banana")) #ana
#print(longestDupSubstring("abcd")) #
#print(longestDupSubstring("aghh")) #h
#print(longestDupSubstring("zxcvdqkfawuytt")) #t
print(longestDupSubstring("nnpxouomcofdjuujloanjimymadkuepightrfodmauhrsy")) #ma
print(longestDupSubstring("aa")) #a
