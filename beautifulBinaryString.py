def minChanges(s):
    total=0
    for i in range(0, len(s), 2):
        total+=( s[i] != s[i+1] )
    return total
