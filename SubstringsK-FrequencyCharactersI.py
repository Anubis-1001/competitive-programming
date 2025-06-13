def numberOfSubstrings(s, k):
    h=dict()
    f=-1
    result=0
    for l in s:
        if l not in h:
            h[l]=0
        h[l]+=1
        while h[l] >= k:
            f+=1
            h[s[f]]-=1
        result+=f+1
    return result


print(numberOfSubstrings())
