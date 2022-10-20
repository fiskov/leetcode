# 12. Integer to Roman
# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num: int) -> str:
        r_str = [(1000, "M"), (900,  "CM"), (500,  "D"), (400,  "CD"), (100,  "C"), (90,  "XC"),
                 (50,  "L"), (40,  "XL"), (10,  "X"), (9,  "IX"), (5,  "V"), (4,  "IV"), (1,  "I")]
        res = ""
        for pos in r_str:
            dd = divmod(num, pos[0])
            res += dd[0] * pos[1]
            num = dd[1]
        return res


sol = Solution()

print(sol.intToRoman(3))        # III
print(sol.intToRoman(58))       # LVIII
print(sol.intToRoman(1994))     # MCMXCIV
