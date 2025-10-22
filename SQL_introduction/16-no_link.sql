--  list all records except those where name is empty
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;