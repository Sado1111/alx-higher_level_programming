-- displays top 3 cities temperature during JULY and AUGUST, ordered by descending order 
SELECT city, AVG(value) AS avg_temp FROM temperature WHERE 'month' = 7 OR 'month' = 8 GROUP BY city ORDER BY avg_temp DESC;
LIMIT 3;