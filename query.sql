SELECT crew_names.name, title_data.titleName, title_data.averageRating, title_data.numVotes, title_data.genre
FROM crew_names
INNER JOIN title_directors ON crew_names.nconst = title_directors.nconst
INNER JOIN title_data ON title_data.tconst = title_directors.tconst
-- WHERE title_data.numVotes > 1000
WHERE title_data.titleName IS NOT NULL
-- ORDER BY crew_names.name;