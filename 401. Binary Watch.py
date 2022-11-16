# 401. Binary Watch
# https://leetcode.com/problems/binary-watch/

import time
from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        res = []
        if turnedOn < 9:
            for h in range(12):
                for m in range(60):
                    if h.bit_count() + m.bit_count() == turnedOn:
                        res.append(f"{h}:{m:02d}")
        return res


def test(arg1, arg2):
    res = sol.readBinaryWatch(arg1)
    if res == arg2:
        print("OK", res, "==", arg2)
    else:
        print("--", res, "==", arg2, " <= ", arg1)


start = time.time()

sol = Solution()

test(1, ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"])
test(2, ["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"])
test(9, [])

print("time = ", time.time() - start)
