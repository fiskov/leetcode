# 2437(6208). Number of Valid Clock Times
# https://leetcode.com/contest/biweekly-contest-89/problems/number-of-valid-clock-times/

class Solution:
    def countTime(self, time: str) -> int:
        cnt = 1
        if time[0] == '?' and time[1] == '?':
            cnt *= 24
        else:
            if time[0] == '?' and time[1] != '?':
                if time[1] in "0123":
                    cnt *= 3
                else: 
                    cnt *= 2
            if time[0] != '?' and time[1] == '?':
                if time[0] == '2':
                    cnt *= 4
                else:
                    cnt *= 10
        if time[3] == '?':
            cnt *= 6
        if time[4] == '?':
            cnt *= 10

        return cnt


sol = Solution()

print(sol.countTime(time = "?5:00"))
print(sol.countTime(time = "2?:00"))
print(sol.countTime(time = "0?:0?"))
print(sol.countTime(time = "??:??"))
