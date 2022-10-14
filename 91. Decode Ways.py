# 91. Decode Ways
# https://leetcode.com/problems/decode-ways/
# leet_91

class Solution:
    def numDecodings(self, s: str) -> int:
        # similar problem about stairs
        if not s or s[0] == '0':
            return 0

        # looks like Fibonaccy-row -> a[n-2] + a[n-1] = a[n]
        a1, a2, a3 = 1, 1, 0

        for i in range(2, len(s)+1):
            # 1-step [1..9]
            if s[i-1] != '0':
                a3 = a2
            # 2-step [10..26]
            if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] <= '6'):
                a3 += a1
            a1, a2, a3 = a2, a3, 0

        return a2  # return last sum


sol = Solution()

print(sol.numDecodings("12"))   # 2
print(sol.numDecodings("226"))  # 3
print(sol.numDecodings("06"))   # 0
print(sol.numDecodings("1111"))   # 5
