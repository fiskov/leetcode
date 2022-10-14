# 1328. Break a Palindrome
# https://leetcode.com/problems/break-a-palindrome/

class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) > 1:
            # search first not-a (only first half of word)
            for i in range(len(palindrome) // 2):
                if palindrome[i] != 'a':
                    return (palindrome[:i] + 'a' + palindrome[i+1:])
            # replace last symbol to 'b' (hint #4)
            return (palindrome[:-1] + 'b')
        return ""


sol = Solution()

print(sol.breakPalindrome("abccba"))    # return "aaccba"
print(sol.breakPalindrome("aaa"))    # return "aab"
print(sol.breakPalindrome("aba"))    # return "aab"
print(sol.breakPalindrome("a"))    # return ""
