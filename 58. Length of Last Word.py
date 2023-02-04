# 58. Length of Last Word
# https://leetcode.com/problems/length-of-last-word/
import itertools
import time
from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        r = s.rfind(' ')
        if r > -1:
            return len(s)-r-1
        return len(s)


def test(**kwargs):
    if not hasattr(test, "counter"):
        test.counter = 0
    test.counter += 1

    method_list = [func for func in dir(Solution) if callable(
        getattr(Solution, func)) and not func.startswith("__")]
    method = getattr(Solution, method_list[0])

    kwarg_dict = dict(itertools.islice(kwargs.items(), len(kwargs)-1))
    res = method(Solution, **kwarg_dict)

    res0 = list(kwargs.items())[-1][1]
    msg = "OK" if res == res0 else "--"
    print(f"{test.counter:3}: {msg} {res0} == {res}")


start = time.time()

sol = Solution()

test(s="Hello World", output=5)
test(s="   fly me   to   the moon  ", output=4)
test(s="luffy is still joyboy", output=6)

print("time = ", time.time() - start)
