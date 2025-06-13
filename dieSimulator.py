from functools import cache

def dieSimulator(n, rollMax):
    @cache
    def dfs(n, last, last_count):
        if n == 0:
            return 1
        t_sum = 0 
        for i in range(len(rollMax)):
            if i == last and last_count > 0:
                t_sum += dfs(n - 1, i, last_count - 1)
            elif i != last:
                t_sum += dfs(n - 1, i, rollMax[i] - 1)

        return t_sum
    r_sum = 0
    for j in range(len(rollMax)):
        r_sum += dfs(n - 1, j, rollMax[j] - 1)
    return r_sum

print(dieSimulator(3, [1,1,1,2,2,3]))

