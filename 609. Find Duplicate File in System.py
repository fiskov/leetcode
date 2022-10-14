# 609. Find Duplicate File in System
# https://leetcode.com/problems/find-duplicate-file-in-system/
# leet-609
from typing import List
from collections import defaultdict

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for path in paths:
            files = path.split(' ')
            for file in files[1::]:
                items = file.split('(')     # file_name
                data = items[1][:-1]     # data in (brackets)
                res[data].append(files[0] + '/' + items[0]) # dir + filename
                
        # return lists with more 1 elements
        return [dt for x, dt in res.items() if len(res[x]) > 1]


sol = Solution()

print(sol.findDuplicate(paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))
print(sol.findDuplicate(paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]))

