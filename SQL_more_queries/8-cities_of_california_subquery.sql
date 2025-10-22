-- list all the cities of CAlifornia found in database
SELECT id, name FROM cities
WHERE state_id = (
	SELECT id FROM states
	WHERE name='California')