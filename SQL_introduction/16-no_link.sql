-- Lists score and name from second_table, excluding records with no name,
-- ordered by score descending
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
