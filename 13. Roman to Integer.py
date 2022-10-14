# 13. Roman to Integer
# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        numbers = {"I": 1, "V": 5, "X": 10,
                   "L": 50, "C": 100, "D": 500, "M": 1000}
        numbers_pre = {"VI": 4, "XI": 9,
                       "LX": 40, "CX": 90,
                       "DC": 400, "MC": 900}
        result = 0
        s = s[::-1]
        pos = 0
        while pos < len(s):
            if pos < len(s) - 1:
                s1 = s[pos: pos+2]
                if s1 in numbers_pre:
                    result += numbers_pre[s1]
                    pos += 2
                    continue
            result += numbers[s[pos]]
            pos += 1

        return result


sol = Solution()

print(sol.romanToInt(s = "III"))
print(sol.romanToInt(s = "LVIII"))
print(sol.romanToInt(s = "MCMXCIV"))
