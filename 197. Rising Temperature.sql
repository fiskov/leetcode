# 197. Rising Temperature
# https://leetcode.com/problems/rising-temperature/
# Write your MySQL query statement below
select w0.id from Weather as w0 inner join Weather as w1 on (w0.temperature > w1.temperature) and (w1.recordDate=subdate(w0.recordDate, 1))