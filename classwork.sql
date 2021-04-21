select mov_title, mov_year
from movie;

select mov_year, mov_title
from movie
where mov_title = 'American beauty';

select mov_year, mov_title
from movie
where mov_year = '1999';

select mov_year, mov_title
from movie
where mov_year < '1998';

select concat(mov_title, "      ", rev_name) as mov_rev_names
from movie, reviewer;

select rev_stars, rev_name
from ratings, reviewer
where rev_stars > 7;

select mov_title, num_of_ratings
from movie, ratings
where num_of_ratings = '0';

select rev_name, num_of_ratings
from reviewer, ratings
where num_of_ratings is null;

select dir_fname, dir_lname, mov_title
from director , movie
where mov_title = 'Eyes Wide Shut';