-- list all the cities of CAlifornia found in database
SELECT * FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name='California')