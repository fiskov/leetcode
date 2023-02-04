# 6262. Maximum Star Sum of a Graph
# https://leetcode.com/contest/biweekly-contest-93/problems/maximum-star-sum-of-a-graph/
import itertools
import math
import bisect
import time
from typing import List, DefaultDict


class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        sum_max = max(vals)

        sum2nodes = DefaultDict(list)
        for edge in edges:
            sum2nodes[edge[0]].append(vals[edge[1]])
            sum2nodes[edge[1]].append(vals[edge[0]])
        #print(f"sum2nodes={sum2nodes}")
        for key, sums in sum2nodes.items():
            sums = sorted(sums, reverse=True)
            #print(f"sums={sums}")
            sum_local = vals[key]
            for i in range(min(k, len(sums))):
                sum_new = sum_local + sums[i]
                if sum_new > sum_local:
                    sum_local = sum_new
                else:
                    break

            sum_max = max(sum_local, sum_max)

        return sum_max


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

test(vals = [1,2,3,4,10,-10,-20], edges = [[0,1],[1,2],[1,3],[3,4],[3,5],[3,6]], k = 2, output=16)
test(vals = [-5], edges = [], k = 0, output=-5)

print("time = ", time.time() - start)
