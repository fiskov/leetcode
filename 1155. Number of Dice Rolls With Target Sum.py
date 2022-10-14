# 1155. Number of Dice Rolls With Target Sum
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
# leet_1155

from timeit import default_timer as timer


class Solution:
    MODULO = 1000000007  # 10**9 + 7

    def helper(self, n: int, k: int, target: int) -> int:
        if target < n or target > n*k:
            return 0
        if n == 1:
            return 1

        key = n*10000 + target
        if key in self.mem:
            return self.mem[key]

        s = 0
        for i in range(k):
            if i+1 < target:
                s += self.helper(n-1, k, target-(i+1))

        if s > self.MODULO:
            s = int(s % self.MODULO)

        self.mem[key] = s
        return s

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        self.mem = {}
        return self.helper(n, k, target)


sol = Solution()
start = timer()

print(sol.numRollsToTarget(n=3, k=6, target=9))  # 25
print(sol.numRollsToTarget(n=5, k=16, target=30))  # 20176
print(sol.numRollsToTarget(n=1, k=6, target=3))  # 1
print(sol.numRollsToTarget(n=2, k=6, target=7))  # 6
print(sol.numRollsToTarget(n=2, k=5, target=10))  # 1
print(sol.numRollsToTarget(n=30, k=30, target=500))  # 222616187

print(timer() - start)
