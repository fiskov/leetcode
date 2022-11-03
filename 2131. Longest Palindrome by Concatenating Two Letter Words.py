# 2131. Longest Palindrome by Concatenating Two Letter Words
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

from collections import Counter
import time
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        words_cnt = Counter(words)
        words_cnt_aa = Counter()
        words_cnt_abba = Counter()

        for c in words_cnt.items():
            a, b = c[0][0], c[0][1]
            ab, ba = a+b, b+a
            if c[1]:
                if a == b:
                    words_cnt_aa[a+b] += c[1]
                elif ba in words_cnt:
                    words_cnt_abba[ab] += min(c[1], words_cnt[ba])
                    words_cnt[ba] = 0
                    words_cnt[ab] = 0

        cnt_aa, cnt_abba = 0, 0
        if len(words_cnt_aa):
            cnt_aa = sum([x//2 for x in words_cnt_aa.values()])*2
            if len([x for x in words_cnt_aa.values() if x % 2]):
                cnt_aa += 1
        if len(words_cnt_abba):
            cnt_abba = sum(words_cnt_abba.values())

        return cnt_abba*4 + cnt_aa*2


def test(arg1, arg2):
    res = sol.longestPalindrome(arg1)
    if len(arg1) < 10:
        if res == arg2:
            print("OK", res, "==", arg2)
        else:
            print("--", res, "==", arg2, " <= ", arg1)
    else:
        print("-- complete len(arg)=", len(arg1), ", len(res)=", len(res))


start = time.time()

sol = Solution()

test(["lc","cl","gg"], 6)
test(["lc","cl","gg","aa","gg","aa","bb"], 14)
test(["ab","ty","yt","lc","cl","ab"], 8)
test(["cc","ll","xx"], 2)
test(["cc","ll","ll","ll","xx"], 6)

print("time = ", time.time() - start)
