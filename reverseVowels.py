def revVowels(s):
    ptr1 = 0
    ptr2 = len(s)-1
    result = list(s)
    while ptr1 < ptr2:

        while s[ptr1] not in list("AEIOUaeoiu"):
            ptr1+=1
            if ptr1 >= ptr2: return "".join(result)


        while s[ptr2] not in list("AEIOUaeoiu"):
            ptr2-=1
            if ptr1 >= ptr2: return "".join(result)

        result[ptr1] = s[ptr2]
        result[ptr2] = s[ptr1]
        ptr1+=1
        ptr2-=1

    return "".join(result)

print(revVowels("IceCreAm"))
print(revVowels("leetcode"))
