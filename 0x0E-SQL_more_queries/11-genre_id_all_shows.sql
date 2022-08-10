-- lists all shows contained in the database hbtn_0d_tv_showshows
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id OR tv_show_genres.show_id = NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
