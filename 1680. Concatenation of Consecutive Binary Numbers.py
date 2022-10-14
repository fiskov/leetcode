# 1680. Concatenation of Consecutive Binary Numbers
# https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
# leet-1680


class Solution:
    MODULO = 1e9 + 7

    # `write` number at right = equal shift RESULT by length of binary
    # add number and need only reminder of RESULT
    def concatenatedBinary(self, n: int) -> int:
        result = 0

        for t in range(1, n+1):
            result <<= t.bit_length()
            result += t
            result = int(result % self.MODULO)

        return result


sol = Solution()

print(sol.concatenatedBinary(n = 1))
print(sol.concatenatedBinary(n = 3))
print(sol.concatenatedBinary(n = 12))
print(sol.concatenatedBinary(n = 9999))
