def merge(a1, a2 ):
    j=0
    for n in a1:
        while j<len(a2) and n >= a2[j]:
            j+=1
        a2.insert(j, n)

    return a2 


print(merge([1,3,5,11], [4,4.5,23, 24, 30]))
print(merge([1,3,5,11], [1, 2, 2.2]))
