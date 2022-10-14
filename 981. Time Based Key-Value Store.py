# 981. Time Based Key-Value Store
# https://leetcode.com/problems/time-based-key-value-store/
import bisect


class TimeMap:

    def __init__(self):
        self.dict_tm = {}   # timestamp
        self.dict_vl = {}   # values
        pass

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict_tm.setdefault(key, [timestamp]).append(timestamp)
        self.dict_vl.setdefault(key, [value]).append(value)
        return 0

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict_tm:
            return ""

        pos = bisect.bisect(self.dict_tm[key], timestamp)-1
        if pos < 0:
            return ""

        return self.dict_vl[key][pos]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

timeMap = TimeMap()
print(timeMap.set("foo", "bar", 1) )
print(timeMap.set("x", "b", 3) )
print(timeMap.get("b", 3) ) 
print(timeMap.set("foo", "bar2", 4) )
print(timeMap.set("foo", "bar3", 6) )
print(timeMap.set("foo2", "bar7", 4))
print(timeMap.set("foo2", "bar8", 10))
print(timeMap.get("foo", 1)        )  # return "bar"
print(timeMap.get("foo", 5)        )  # return "bar2", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
print(timeMap.get("foo2", 3)        )  # return ""
print(timeMap.get("foo2", 4)        )  # return "bar7"
print(timeMap.get("foo2", 5)        )  # return "bar7"

'''
["TimeMap","set","set","get","set","get","get"]
[[],["a","bar",1],["x","b",3],["b",3],["foo","bar2",4],["foo",4],["foo",5]]
'''

'''
["TimeMap","set","set","get","get","get","get","get"]
[[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]
'''