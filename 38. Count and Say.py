# 38. Count and Say
# https://leetcode.com/problems/count-and-say/


class Solution:
    # 3322251 -> "23321511"
    def convert(self, s: str) -> str:
        # print("conv=", s)
        xs = [0, s[0]]
        for c in s:
            if c == xs[-1]:
                xs[-2] += 1
            else:
                xs.append(1)
                xs.append(c)
        return ''.join(map(str, xs))

    def countAndSay(self, n: int) -> str:
        res = "1"
        if n > 1:
            for _ in range(n-1):
                res = self.convert(res)
        return res


sol = Solution()

print(sol.countAndSay(1))
print(sol.countAndSay(4))
