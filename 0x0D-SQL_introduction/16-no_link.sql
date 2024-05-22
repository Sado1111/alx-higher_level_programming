-- lists records of second_table where name is not null, selected by score,name in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
