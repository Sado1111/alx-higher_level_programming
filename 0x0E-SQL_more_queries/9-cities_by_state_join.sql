-- lists all cities in usa database showing cities' id and name and state name
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY id ASC;
