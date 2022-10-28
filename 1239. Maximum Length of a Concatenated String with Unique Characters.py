# 1239. Maximum Length of a Concatenated String with Unique Characters
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
import itertools
import time
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr_new = []
        for s in arr:
            if len(set(s)) == len(s):
                arr_new.append(s)

        n = len(arr_new)
        if n == 0:
            return 0

        if n == 1:
            return len(arr_new[0])

        maxlen = 0

        for i in range(n):
            for bfr in itertools.combinations(arr_new, i+1):
                s = "".join(bfr)
                if len(set(s)) == len(s):
                    maxlen = max(maxlen, len(s))

        return maxlen


start = time.time()

sol = Solution()

print(sol.maxLength(arr = ["un","iq","ue"]))  # 4
print(sol.maxLength(arr = ["cha","r","act","ers"]))  # 6
print(sol.maxLength(arr = ["abcdefghijklmnopqrstuvwxyz"]))  # 26
print(sol.maxLength(["aa","bb"]))   # 0
print(sol.maxLength(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]))   # 16


print("time = ", time.time() - start)
