# 175. Combine Two Tables
# https://leetcode.com/problems/combine-two-tables/
# Write your MySQL query statement below
select p.firstName, p.lastName, a.city, a.state from Person as p left join Address as a on p.personId=a.personId
