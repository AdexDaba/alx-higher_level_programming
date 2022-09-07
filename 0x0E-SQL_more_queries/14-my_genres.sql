-- display all genres of the show Dexter
t_my_genres.sql  103-rating_genres.sql    12-no_genre.sql              15-comedy_only.sql
101-not_a_comedy.sql   10-genre_id_by_show.sql  13-count_shows_by_genre.sql  1-create_user.sql
root@a7b8a489c3fd:/alx-higher_level_programming/0x0E-SQL_more_queries#
SELECT tv_genres.name FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;
