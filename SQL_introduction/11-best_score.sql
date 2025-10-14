-- list scores and names of 'second table'
-- where score is greater than or equal to 10
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;