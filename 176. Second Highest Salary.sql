# 176. Second Highest Salary
# https://leetcode.com/problems/second-highest-salary/
# Write your MySQL query statement below

-- create
CREATE TABLE EMPLOYEE (
  id INTEGER PRIMARY KEY,
  salary INTEGER NOT NULL
);

-- insert
INSERT INTO EMPLOYEE VALUES (0001, 200);
INSERT INTO EMPLOYEE VALUES (0002, 200);
INSERT INTO EMPLOYEE VALUES (0003, 200);

-- fetch 
# select max(salary) `SecondHighestSalary` from EMPLOYEE where salary < (select max(salary) from EMPLOYEE);
select (select distinct(salary) from EMPLOYEE order by salary desc limit 1 offset 1) `SecondHighestSalary`;