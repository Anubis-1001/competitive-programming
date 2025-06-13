def validSubstringCount(word1, word2):
    h2={}
    dlCount=0
    for l in word2:
        if l not in h2:
            dlCount+=1
        h2[l]=h2.get(l, 0)+1

    f=0
    h1={}
    result=0
    for l in word1:
        h1[l]=h1.get(l, 0)+1
        if l in h2 and h1[l] == h2[l]:
            dlCount-=1
        while dlCount==0:
            wf=word1[f]
            h1[wf]-=1
            f+=1
            if wf in h2 and h1[wf] <h2[wf]:
                dlCount+=1

        result+=f

    return result
