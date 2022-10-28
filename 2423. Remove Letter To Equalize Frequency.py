# 2423. Remove Letter To Equalize Frequency
# https://leetcode.com/problems/remove-letter-to-equalize-frequency/
from collections import Counter
import time


class Solution:

    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        letters = [x for x in c]
        for letter in letters:
            c[letter] -= 1
            # remove zero-element
            if c[letter] == 0:
                del c[letter]
            # all count-of-letters is similar
            if len(set(c.values())) == 1:
                return True
            c[letter] += 1
        return False


def test(arg1, arg2):
    res = sol.equalFrequency(arg1)
    if res == arg2:
        print("OK", res, "==", arg2)
    else:
        print("--", res, "==", arg2, " <= ", arg1)


start = time.time()

sol = Solution()

test("abcc", True)
test("aazz", False)
test("bac", True)
test("abbcc", True)
test("aazz", False)
test("cccaa", True)
test("zz", True)
test("aaaaabb", False)
test("ddaccb", False)

print("time = ", time.time() - start)
