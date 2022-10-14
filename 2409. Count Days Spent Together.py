# 2409. Count Days Spent Together
# https://leetcode.com/problems/count-days-spent-together/
# leet-2409 (6184)


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        m_sum = [0, 0]  # because start from 1 month
        s = 0
        for days in m:
            s += days
            m_sum.append(s)

        a_start  = m_sum[ int(arriveAlice[0:2])] + int(arriveAlice[3:5])
        a_finish = m_sum[ int(leaveAlice[0:2])] + int(leaveAlice[3:5]) + 1 # inclusive
        b_start  = m_sum[ int(arriveBob[0:2])] + int(arriveBob[3:5])
        b_finish = m_sum[ int(leaveBob[0:2])] + int(leaveBob[3:5]) + 1

        if (b_start <= a_finish) and (b_finish >= a_start):
            start = max(a_start, b_start)
            finish = min(a_finish, b_finish)
            return finish-start

        return 0


sol = Solution()

print(sol.countDaysTogether(arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"))
print(sol.countDaysTogether(arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"))
print(sol.countDaysTogether(arriveAlice = "02-01", leaveAlice = "02-28", arriveBob = "03-01", leaveBob = "03-31"))
