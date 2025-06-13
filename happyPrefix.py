def longestPrefix(s):
    n = len(s)
    hashes=0
    base=26
    MOD=10**9+7
    result=""
    prefix_hash=0
    base_power=1
    for i in range(n-1, 0, -1):
        hashes=(hashes+base_power*ord(s[i]))%MOD
        prefix_hash=(prefix_hash*base+ord(s[n-1-i]))%MOD
        if prefix_hash == hashes:
            if s[:n-i] == s[i:]:
                result=s[:n-i]
        base_power=(base_power*base)%MOD

    return result

print(longestPrefix("level"))
print(longestPrefix("ababab"))
