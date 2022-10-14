# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        if len(strs) == 1:
            return res

        for pos in range(1, len(strs)):
            while strs[pos][0:len(res)] != res:
                res = res[0: len(res)-1]
                if len(res) == 0:
                    return ""
        return res


sol = Solution()

print(sol.longestCommonPrefix(strs=["flower", "flow", "flight"]))
print(sol.longestCommonPrefix(strs=["dog", "racecar", "car"]))
print(sol.longestCommonPrefix(strs=["a"]))
print(sol.longestCommonPrefix(strs=[""]))
