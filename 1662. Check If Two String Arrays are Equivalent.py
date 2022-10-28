# 1662. Check If Two String Arrays are Equivalent
# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/
from itertools import chain, zip_longest
import time
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # return "".join(word1) == "".join(word2)
        s1 = chain.from_iterable(word1)
        s2 = chain.from_iterable(word2)
        for z in zip_longest(s1, s2, '0'):
            if z[0] != z[1]:
                return False
        return True


start = time.time()

sol = Solution()

print(sol.arrayStringsAreEqual(word1=["ab", "c"], word2=["a", "bc"]))  # t
print(sol.arrayStringsAreEqual(word1=["a", "cb"], word2=["ab", "c"]))  # f
print(sol.arrayStringsAreEqual(
    word1=["abc", "d", "defg"], word2=["abcddefg"]))  # t


print("time = ", time.time() - start)
