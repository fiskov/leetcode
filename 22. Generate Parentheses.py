# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

import time
from typing import List
import itertools


class Solution:
    def test_brackets_by_bit_mask(self, x: int, len: int) -> bool:
        m = 0
        for i in range(len):
            if x & (1 << i):
                m += 1
            else:
                if m <= 0 or m > len//2:
                    return False
                else:
                    m -= 1
        return (m == 0)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        for x in range(2**(2*n-1)):
            if self.test_brackets_by_bit_mask(x, n*2):
                brackets_list = ["(" if x & (1 << i) else ")" for i in range(n*2)]
                brackets_str = "".join(brackets_list)
                res.append(brackets_str)
        return res


def test(arg1, arg2):
    res = sol.generateParenthesis(arg1)
    res_ok = True
    if len(res)==len(arg2):
        for x in res:
            if not x in arg2:
                res_ok = False
    if res_ok:
        print("OK", arg1)
    else:
        print("--", res, "==", arg2, " <= ", arg1)


start = time.time()

sol = Solution()
test(4, ["(((())))","((()()))","((())())","((()))()","(()(()))","(()()())","(()())()","(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"])
test(3, ["((()))", "(()())", "(())()", "()(())", "()()()"])
test(2, ["()()", "(())"])
test(1, ["()"])

print("time = ", time.time() - start)
