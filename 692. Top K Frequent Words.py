# 692. Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [x[0] for x in Counter(sorted(words)).most_common(k)]


sol = Solution()

print(sol.topKFrequent(words=["love", "i", "leetcode", "i", "love", "coding"], k=2))
print(sol.topKFrequent(words=["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k=4))
