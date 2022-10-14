# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(', '}':'{', ']':'['}
        m = []
        for c in s:
            if c in "({[":
                m.append(c)
            else:
                if (len(m) == 0) or (m.pop() != brackets[c]):
                    return False
        return (len(m)==0)


sol = Solution()

print(sol.isValid(s = "()"))
print(sol.isValid(s = "()[]{}"))
print(sol.isValid(s = "({[]})"))
print(sol.isValid(s = "({)[]}"))
print(sol.isValid(s = "(]"))
print(sol.isValid(s = "]"))
print(sol.isValid(s = "["))
