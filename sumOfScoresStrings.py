def calculate_z_function(s):
    n = len(s)
    l, r = 0, 0
    Z=[0]*n
    sum_t = 0
    for i in range(1, n):
        if i <= r:
            Z[i] = min(Z[i-l], r-i+1)
        while i+Z[i] < n and s[Z[i]] == s[i+Z[i]]:
            Z[i]+=1
        sum_t+=Z[i]
        if i+Z[i] < r:
            l, r = i, i+Z[i]-1


    return sum_t+n

print(calculate_z_function("babab"))
print(calculate_z_function("azbazbzaz"))
