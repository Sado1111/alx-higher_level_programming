-- lists count of records that has the same score where result displays score , number of records with that score in a descending order this list should be sorted
SELECT score, COUNT(*) AS number FROM second_table  GROUP BY score ORDER BY number DESC;
