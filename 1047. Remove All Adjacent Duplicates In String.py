# 1047. Remove All Adjacent Duplicates In String
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

from collections import defaultdict
import time


class Solution:
    def removeDuplicates(self, s: str) -> str:
        res = []
        for c in s:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)


def test(arg1, arg2):
    res = sol.removeDuplicates(arg1)
    if len(arg1) < 10:
        if res == arg2:
            print("OK", res, "==", arg2)
        else:
            print("--", res, "==", arg2, " <= ", arg1)
    else:
        print("-- complete len(arg)=", len(arg1), ", len(res)=", len(res))


start = time.time()

sol = Solution()

test("abbaca", "ca")
test("azxxzy", "ay")

print("time = ", time.time() - start)
