# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

import time
from typing import List
import itertools


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        letters = {
            "2": ("a","b","c"),
            "3": ("d","e","f"),
            "4": ("g","h","i"),
            "5": ("j","k","l"),
            "6": ("m","n","o"),
            "7": ("p","q","r","s"),
            "8": ("t","u","v"),
            "9": ("w","x","y","z")}
        if len(digits):
            res = [c for c in letters[digits[0]]]
            pos = 1
            while pos < len(digits):
                res_new = []
                for r in res:
                    for c in letters[digits[pos]]:
                        res_new.append(r+c)
                res = res_new
                pos += 1
        return res


def test(arg1, arg2):
    res = sol.letterCombinations(arg1)
    res_ok = False
    if len(res)==len(arg2):
        res_ok = True
        for x in res:
            if not x in arg2:
                res_ok = False
    if res_ok:
        print("OK", arg1)
    else:
        print("--", arg1, ": ", res, "!=", arg2)


start = time.time()

sol = Solution()
test("234", ["ad","ae","af","bd","be","bf","cd","ce","cf"])
test("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"])
test("2", ["a","b","c"])
test("", [])

print("time = ", time.time() - start)
