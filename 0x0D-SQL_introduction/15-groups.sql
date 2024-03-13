-- Script that lists the nuber of records with the same score
SELECT COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
