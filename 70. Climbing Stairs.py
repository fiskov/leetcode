# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# leet_70

class Solution:
    def climbStairs(self, n: int) -> int:
        # it looks like Fibonacci numbers
        a = 1
        b = 0
        for _ in range(n):
            a, b = a+b, a
        return a


sol = Solution()

print(sol.climbStairs(2))   # 2
print(sol.climbStairs(3))   # 3
print(sol.climbStairs(4))   # 5
print(sol.climbStairs(5))   # 8
print(sol.climbStairs(45))
