# 838. Push Dominoes
# https://leetcode.com/problems/push-dominoes/
# leet_838


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        hr = []
        dir = 0
        for c in dominoes:
            if c == 'R':
                dir = 1
            if c == '.' and dir:
                dir += 1
            if c == 'L':
                dir = 0
            hr.append(dir)

        hl = []
        dir = 0
        for c in dominoes[::-1]:
            if c == 'L':
                dir = 1
            if c == '.' and dir:
                dir += 1
            if c == 'R':
                dir = 0
            hl.append(dir)
        hl.reverse()

        res = ""
        for i in range(len(dominoes)):
            c = '.'
            if hr[i] and hl[i] == 0:
                c = 'R'
            if hr[i] == 0 and hl[i]:
                c = 'L'
            if hr[i] and hl[i]:
                if hr[i] < hl[i]:
                    c = 'R'
                if hr[i] > hl[i]:
                    c = 'L'
            # else c='.'
            res += c

        return res


#        print(dominoes)
#        print(hr)
#        print(hl)
sol = Solution()

print(sol.pushDominoes(dominoes = "RR.L"))
print("RR.L")
print(sol.pushDominoes(dominoes = ".L.R...LR..L..R.L"))
print("LL.RR.LLRRLL..R.L")
# print(sol.pushDominoes(dominoes = "."))
# print(sol.pushDominoes(dominoes = "L"))
