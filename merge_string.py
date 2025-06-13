def getMergeWord(word1, word2):
    d = len(word1)
    r = ""
    p = max(len(word1), len(word2))
    total_word= word1+word2
    for i in range(p):
        print(r)
        r+= total_word[i] if i < d else ""
        r+= ( total_word[i+d] if i+d < len(word1+word2) else "" )
    return r


print(getMergeWord("abcd", "pq"))
print(getMergeWord("ab", "pqrs"))
