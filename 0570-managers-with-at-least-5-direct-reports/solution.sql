# Write your MySQL query statement below
-- SELECT e1.name 
-- FROM Employee e1
-- JOIN Employee e2
-- ON e1.id = e2.managerid
-- GROUP BY e2.managerId 
-- HAVING COUNT(e2.managerId) >= 5

SELECT e1.name
FROM Employee e1
JOIN 
(
    SELECT managerId, count(*) as directReports
    FROM Employee
    GROUP BY managerId
    HAVING count(managerId)>=5
) e2
ON e1.id = e2.managerId;
