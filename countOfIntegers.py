from math import pow

class Solution:
    def getIntegers(self, max_digit_sum, min_digit_sum, num_limit):
        n = len(num_limit)
        dp = [[0] * (max_digit_sum + 1) for _ in range(n + 1)]

        for i in range( len(dp)):
            for j in range(len(dp[0])):
                if j >= 9 * i:
                    dp[i][j] = int(pow(10, i))
                else:
                    dp[i][j] = 0
                    for d in range(10):
                        if j - d >= 0:
                            dp[i][j] += dp[i - 1][j - d]

        result = 0

        for k in range(n):
            digit = int(num_limit[k])

            for d in range(digit):
                if max_digit_sum - d >= 0:
                    result += dp[n - 1 - k][max_digit_sum - d]
                if min_digit_sum - 1 - d >= 0:
                    result -= dp[n - 1 - k][min_digit_sum - 1 - d]

            max_digit_sum -= digit
            min_digit_sum -= digit
        if max_digit_sum >= 0 and min_digit_sum <= 0:
            result+=1
        return result

    def count(self, num1, num2, min_sum, max_sum):
        return (self.getIntegers(max_sum, min_sum, num2) - 
                self.getIntegers(max_sum, min_sum, str(int(num1) - 1)) ) % 1000000007


g = Solution()
print(g.getIntegers(5, 1, "5"))
