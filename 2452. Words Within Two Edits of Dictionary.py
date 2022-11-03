# 2452. Words Within Two Edits of Dictionary
# https://leetcode.com/problems/words-within-two-edits-of-dictionary/
from bisect import bisect
from collections import Counter
import time
from typing import List


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        n = len(queries[0])
        res = []

        for q in queries:
            for d in dictionary:
                cnt = 0
                i = 0
                while i < n and cnt < 3:
                    if q[i] != d[i]:
                        cnt += 1
                    i += 1
                if cnt < 3:
                    res.append(q)
                    break

        return res


def test(arg1, arg2, arg3):
    res = sol.twoEditWords(arg1, arg2)
    if res == arg3:
        print("OK", res, "==", arg3)
    else:
        print("--", res, "==", arg3, " <= ", arg1)


start = time.time()

sol = Solution()

test(["word","note","ants","wood"], ["wood","joke","moat"], ["word","note","wood"])
test(["yes"], ["not"], [])
test(["tsl","sri","yyy","rbc","dda","qus","hyb","ilu","ahd"], ["uyj","bug","dba","xbe","blu","wuo","tsf","tga"], ["tsl","yyy","rbc","dda","qus","hyb","ilu"])

print("time = ", time.time() - start)

