-- all genres from hbtn_0d_tvshows and displays the number of shows linked to each
CREATE TABLE IF NOT EXISTS genre_table AS
SELECT show_id, COUNT(genre_id) AS number_of_shows
FROM tv_show_genres
GROUP BY show_id;

SELECT tv_genres.name, number_of_shows
FROM tv_genres
INNER JOIN genre_table on tv_genres.id=genre_table.show_id
ORDER BY number_of_shows DESC;