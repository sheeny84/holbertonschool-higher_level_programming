--  compute the average score of all the records
SELECT SUM(score)/COUNT(*) AS average
FROM second_table;