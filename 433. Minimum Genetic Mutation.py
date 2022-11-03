# 433. Minimum Genetic Mutation
# https://leetcode.com/problems/minimum-genetic-mutation/

from collections import defaultdict
import time
from typing import List


class Solution:
    def isDiffSingleLetter(self, s1, s2) -> bool:
        # get count of diff letters in strings
        cnt = sum([1 for a, b in zip(s1, s2) if a != b])
        return cnt == 1

    def getNum(self, n: int, startWord: str, prevNum: set) -> int:
        nums = set()
        for index in self.nums.difference(prevNum):
            if self.isDiffSingleLetter(startWord, self.bank[index]):
                if self.bank[index] == self.endword:
                    return n+1
                else:
                    nums.add(index)

        res_min = 9999
        for index in nums:
            prevNum.add(index)
            res = self.getNum(n+1, self.bank[index], prevNum)
            if res > -1:
                res_min = min(res_min, res)
            prevNum.remove(index)

        if res_min == 9999:
            return -1
        else:
            return res_min

    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        self.bank = bank
        self.endword = end
        self.nums = set([x for x in range(len(bank))])

        return self.getNum(0, start, set())


def test(arg1, arg2, arg3, argR):
    sol = Solution()
    res = sol.minMutation(arg1, arg2, arg3)
    if len(arg1) < 10:
        if res == argR:
            print("OK", res, "==", argR)
        else:
            print("--", res, "==", argR, " <= ", arg1)
    else:
        print("-- complete len(arg)=", len(arg1), ", len(res)=", len(res))


start = time.time()

test("AACCGGTT", "AACCGGTA", ["AACCGGTA"], 1)
test("AACCGGTT", "AAACGGTA", ["AACCGGTA","AACCGCTA","AAACGGTA"], 2)
test("AAAAACCC", "AACCCCCC", ["AAAACCCC","AAACCCCC","AACCCCCC"], 3)
test("AAAACCCC", "CCCCCCCC", ["AAAACCCA","AAACCCCA","AACCCCCA","AACCCCCC","ACCCCCCC","CCCCCCCC","AAACCCCC","AACCCCCC"], 4)
print("time = ", time.time() - start)
