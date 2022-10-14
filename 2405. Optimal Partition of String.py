# 2405. Optimal Partition of String
# https://leetcode.com/problems/optimal-partition-of-string/
# leet-2405
class Solution:
    def partitionString(self, s: str) -> int:
        m = set()
        cnt = 1
        for c in s:
            if c in m:
                cnt += 1
                m = set()
                m.add(c)
            else:
                m.add(c)

        return cnt


sol = Solution()

print(sol.partitionString(s="abacaba"))
print(sol.partitionString(s="ssssss"))
print(sol.partitionString(s="a"))
print(sol.partitionString(s="abcdefg"))
