# 28. Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

import time


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


def test(arg1, arg2, arg3):
    sol = Solution()
    res = sol.strStr(arg1, arg2)
    if res == arg3:
        print("OK", res, "==", arg3)
    else:
        print("--", res, "==", arg3, " <= ", arg1, arg2)


start = time.time()

sol = Solution()

test("sadbutsad", "sad", 0)
test("leetcode", "leeto", -1)

print("time = ", time.time() - start)
