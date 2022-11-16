# 345. Reverse Vowels of a String
# https://leetcode.com/problems/reverse-vowels-of-a-string/

import time
from typing import List


class Solution:
    def reverseVowels(self, s: str) -> str:
        sl = list(s)
        vowels = "aeiouAEIOU"
        i, j = 0, len(sl)-1
        while i < j:
            while sl[i] not in vowels and i < j:
                i += 1
            while sl[j] not in vowels and i < j:
                j -= 1
            if i < j:
                sl[i], sl[j] = sl[j], sl[i]
            i += 1
            j -= 1

        return ''.join(sl)


def test(arg1, arg2):
    res = sol.reverseVowels(arg1)
    if len(arg1) < 10:
        if res == arg2:
            print("OK", res, "==", arg2)
        else:
            print("--", res, "==", arg2, " <= ", arg1)
    else:
        print("-- complete len(arg)=", len(arg1), ", len(res)=", len(res))


start = time.time()

sol = Solution()

test("bcdfaghjk", "bcdfaghjk")
test("bcdfaoghjk", "bcdfoaghjk")
test("auoghjk", "ouaghjk")

test("hello", "holle")
test("leetcode", "leotcede")
# test(test_big_array.p1, [])

print("time = ", time.time() - start)
