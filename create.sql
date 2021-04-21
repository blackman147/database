CREATE TABLE movie(
	mov_id    Integer       NOT NULL,
    mov_title   Char(50)        NULL,
    mov_year    Integer         NULL,
    mov_time    Integer         NULL,
    mov_lang    Char(50)        NULL,
    mov_dt_rel  Date            NULL,
    mov_rel_country  Char(10)   NULL,
	CONSTRAINT     movie_pk     PRIMARY KEY(mov_id)
);

CREATE TABLE actor(
	act_id       Integer       NOT NULL,
    act_fname    Char(20)          NULL,
    act_lname    Char(20)          NULL,
    act_gender   Char(1)           NULL,
    CONSTRAINT     actor_pk     PRIMARY KEY(act_id)
);


CREATE TABLE movie_cast(
	mov_id       Integer       NOT NULL,
    act_id       Integer       NOT NULL,
	role         Char(30)          NULL,
	CONSTRAINT     movie_cast_pk     PRIMARY KEY(mov_id, act_id)
);



CREATE TABLE  director(
	dir_id       Integer       NOT NULL,
    dir_fname    Char(20)          NULL,
    dir_lname    Char(20)          NULL,
    CONSTRAINT    director_pk     PRIMARY KEY(dir_id)
);


CREATE TABLE movie_direction(
	dir_id       Integer       NOT NULL,
    mov_id       Integer       NOT NULL,
    CONSTRAINT     movie_direction_pk     PRIMARY KEY(dir_id, mov_id)
);


CREATE TABLE genre(
	gen_id       Integer       NOT NULL,
    gen_title    Char(20)          NULL,
	CONSTRAINT    genre_pk     PRIMARY KEY(gen_id)
);

CREATE TABLE movie_genre(
	mov_id       Integer       NOT NULL,
    gen_id       Integer       NOT NULL,
    CONSTRAINT     movie_genre_pk     PRIMARY KEY(mov_id, gen_id)
);

CREATE TABLE reviewer(
	rev_id       Integer       NOT NULL,
    rev_name    Char(30)          NULL,
    CONSTRAINT    reviewer_pk     PRIMARY KEY(rev_id)
);

CREATE TABLE ratings(
	mov_id       Integer       NOT NULL,
    rev_id       Integer       NOT NULL,
    rev_stars    Integer           NULL,
    num_of_ratings   Integer       NULL,
     CONSTRAINT    ratings_pk     PRIMARY KEY(mov_id, rev_id)
);