-- Lists genres and the number of shows linked to each in the hbtn_0d_tvshows database
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY COUNT(tv_show_genres.show_id) DESC;
