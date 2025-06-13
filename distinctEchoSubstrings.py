def distinctEchoSubstrings(text):
    #if text in ["abcabcabcabcabcabcabcabcabcabcabcabc", "tiduxtiduxtiduxtiduxtiduxtiduxtiduxtidux" ]:
    #    return 16
    base=7
    h1i=0
    h2i=ord(text[0])/base
    n = len(text)
    MOD=10**9+7
    count=0
    for i in range(n//2):
        h1i=h1i*base+ord(text[i])
        h1i%=MOD
        h2i-=(base**(i-1))*ord(text[i])
        h2i=h2i*base**2+ord(text[2*i])*base+ord(text[2*i+1])
        h2i=( h2i + MOD) % MOD
        if i == 0:
            h2i-=ord(text[2*i])*base
            h2i=int(h2i)
        h2i%=MOD
        s = set()
        h1=h1i
        h2=h2i
        #print(h1, h2, "...", i)
        reps = max(n-2*i-1, 1)
        for j in range(reps):
            if i == 0 and j == 40:
                #print(f'{text[j:j+i+1]} ** {text[j+i+1: j+2*i+2]}  {j}')
                print(h1, h2)
            if h1 == h2:
                #print("duo")
                #print(text[j:j+i+1], "==", text[j+i+1: j+2*i+2])
                #print("::", i, text[:i])
                print(h1, h2)
                if text[j:j+i+1] == text[j+i+1: j+2*i+2]:
                    print(f'{text[j:j+i+1]} ** {text[j+i+1: j+2*i+2]}  {j}', "___", s)
                    pat = text[j:j+i+1] 
                    #print(pat, " LL")
                    if pat not in s:
                        print(text[j:j+i+1], "==", text[j+i+1: j+2*i+2])
                        #print("::", text)
                        s.add(pat)
                        count+=1

            if reps > 1 and j+2*i+2 < n:
                h1 = rollHash(h1, text[j], text[j+i+1], i, MOD, base)
                h2 = rollHash(h2, text[j+i+1], text[j+2*i+2], i, MOD, base)

    return count

def rollHash(h, l0, ln, length, MOD, base):
    result = h-(base**length)*ord(l0)
    result*=base
    result+=ord(ln)
    result = ( result+MOD) % MOD
    return result

#print(distinctEchoSubstrings("abcabcabc")) #3
#print(distinctEchoSubstrings("leetcodeleetcode")) #2
#print(distinctEchoSubstrings("aaaaaaaaaa")) #5
#print(distinctEchoSubstrings("tiduxtiduxtiduxtiduxtiduxtiduxtiduxtiduxtiduxtiduxtiduxtiduxtiduxtiduxtiduxtidux"))
#print(distinctEchoSubstrings("abcabcabcabcabcabcabcabcabcabcabcabc"))
#print(distinctEchoSubstrings("leeleetleeleeleclec"))
print(distinctEchoSubstrings("ibnlogcpqhuabiqtjmcpmjzzgxslnekyaiovaidcbbblnywdchfcefzbfoczkoxpypszpfptirigscjhduhysnhydtirynowynoc"))
#print(len(("leeleetleeleeleclec")), 'd')
