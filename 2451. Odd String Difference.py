# 2451. Odd String Difference
# https://leetcode.com/problems/odd-string-difference/
from bisect import bisect
from collections import Counter, defaultdict
import time
from typing import List


class Solution:
    def getDiff(self, word: str):
        res = []
        for i in range(1, len(word)):
            res.append(ord(word[i]) - ord(word[i-1]))
        return tuple(res)

    def oddString(self, words: List[str]) -> str:
        c = Counter()
        d = dict()
        for w in words:
            t = self.getDiff(w)
            c[t] += 1
            if w not in d:
                d[t] = w
        return d[c.most_common(2)[1][0]]


def test(arg1, arg2):
    res = sol.oddString(arg1)
    if res == arg2:
        print("OK", res, "==", arg2)
    else:
        print("--", res, "==", arg2, " <= ", arg1)


start = time.time()

sol = Solution()

test(["adc","wzy","abc"], "abc")
test(["aaa","bob","ccc","ddd"], "bob")

print("time = ", time.time() - start)

