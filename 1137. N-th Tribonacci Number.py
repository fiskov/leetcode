# 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/
# leet_1137

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        # Tribonacci numbers
        a = 1
        b = 0
        c = 0
        for _ in range(n-1):
            a, b, c = a+b+c, a, b
        return a


sol = Solution()

print(sol.tribonacci(0))   # 0
print(sol.tribonacci(1))   # 1
print(sol.tribonacci(3))   # 2
print(sol.tribonacci(4))   # 4
print(sol.tribonacci(25))   # 1389537
