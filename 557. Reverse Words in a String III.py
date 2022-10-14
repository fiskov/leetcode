# 557. Reverse Words in a String III
# https://leetcode.com/problems/reverse-words-in-a-string-iii/
# leet-557

class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([x[::-1] for x in s.split()])


sol = Solution()

print(sol.reverseWords(s = "Let's take LeetCode contest"))
print(sol.reverseWords(s = "God Ding"))
print(sol.reverseWords(s = "A"))
