# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
import time
from typing import List


class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            key = hash(''.join(sorted(s)))
            d[key].append(s)
        return [v[1] for v in d.items()]


start = time.time()

sol = Solution()

print(sol.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))  #  [["bat"],["nat","tan"],["ate","eat","tea"]]
print(sol.groupAnagrams(strs = [""]))
print(sol.groupAnagrams(strs = ["a"]))  # a

print("time = ", time.time() - start)
