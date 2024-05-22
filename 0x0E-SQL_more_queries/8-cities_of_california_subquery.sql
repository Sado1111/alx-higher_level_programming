-- lists all cities of California, does not use JOIN, 
SELECT id, name
FROM  cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
