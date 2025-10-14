--  list number of records with the same score
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;