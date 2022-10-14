# 2406. Divide Intervals Into Minimum Number of Groups
# https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/
# leet-2406
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        points = []
        # fill [ start_point, +1 interval ], [end_point+1, -1 interval] 
        # end_point+1, because next interval strictly more
        for interval in intervals:
            points.append([interval[0], 1])
            points.append([interval[1]+1, -1])

        # sort for increase start_points - intervals will be intersect
        # and maximum of intersections is answer
        points = sorted(points)
        intersections = 0
        max_intersections = 0
        for point in points:
            intersections += point[1]
            max_intersections = max(max_intersections, intersections)
        return max_intersections


sol = Solution()

print(sol.minGroups(intervals=[[5, 10], [6, 8], [1, 5], [2, 3], [1, 10]]))
print(sol.minGroups(intervals=[[1, 3], [5, 6], [8, 10], [11, 13]]))
print(sol.minGroups(intervals=[[4, 4]]))
