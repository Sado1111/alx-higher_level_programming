-- lists all records of score, name with a score >= 10 in second_table, record should be ordered by score in descending order 
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
