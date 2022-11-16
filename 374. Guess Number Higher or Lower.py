# 374. Guess Number Higher or Lower
# https://leetcode.com/problems/guess-number-higher-or-lower/

import time


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

pick = 0


def guess(num: int) -> int:
    if num > pick:
        return -1
    if num < pick:
        return 1
    return 0


class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        a, b = 1, n
        middle = (a + b + 1) // 2
        res = guess(middle)
        while res and b != middle:
            if res > 0:
                a = middle
            else:
                b = middle

            middle = (a + b + 1) // 2
            res = guess(middle)
        if b == middle:
            if res == -1:
                return middle-1

        return middle


def test(arg1, arg2, arg0):
    global pick
    pick = arg2
    res = sol.guessNumber(arg1)
    print(["OK", "--"][res != arg0], res, "==", arg0)


start = time.time()

sol = Solution()

test(2, 1, 1)
test(2, 2, 2)
test(3, 3, 3)
test(4, 4, 4)
test(10, 6, 6)
test(10, 7, 7)
test(10, 8, 8)
test(10, 9, 9)
test(1, 1, 1)

print("time = ", time.time() - start)
