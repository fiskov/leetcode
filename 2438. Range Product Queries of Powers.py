# 2438(6209). Range Product Queries of Powers
# https://leetcode.com/contest/biweekly-contest-89/problems/range-product-queries-of-powers/

import bisect
from math import log
from typing import List

class Solution:
    modulo = 1E9 + 7
    powers0 = []

    def preparePowers0Array(self):
        # how many powers of 2 before 1E9
        cnt = int(log(1E9) / log(2))
        num = 1
        for p in range(cnt+1):
            self.powers0.append(num)
            num *= 2

    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        res = []
        powers = []

        if len(self.powers0) == 0:
            self.preparePowers0Array()

        while n:
            n_max = self.powers0[bisect.bisect(self.powers0, n)-1]
            powers.append(n_max)
            n -= n_max
        powers = sorted(powers)

        for q_range in queries:
            value = 1
            for i in range(q_range[0], q_range[1]+1):
                value *= powers[i]
                if value > self.modulo:
                    value %= int(self.modulo)
            res.append(value)

        return res


sol = Solution()

print(sol.productQueries(n=15, queries=[[0, 1], [2, 2], [0, 3]]))  # [2,4,64]
print(sol.productQueries(n=2, queries=[[0, 0]]))  # [2]
print(sol.productQueries(806335498, [[11, 11]]))
# 268435456
# 536870912
