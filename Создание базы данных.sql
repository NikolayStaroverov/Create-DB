create table if not exists Singer (
	ID serial primary key,
	singer_name text not null
);

create table if not exists Album (
	ID serial primary key,
	album_name text not null,
	album_year integer check (album_year>1900)
);

create table if not exists Track (
	ID serial primary key,
	album_id integer references Album (ID),
	track_name text not null,
	track_length decimal (5,2) not null
);

create table if not exists Categories (
	ID serial primary key,
	category_name text not null
);

create table if not exists Collection (
	ID serial primary key,
	Collection_name text not null,
	Collection_year integer check (Collection_year>1900)
);

create table if not exists Singer_Categories (
	singer_id integer references singer(ID),
	categories_id integer references categories(ID),
	constraint PK_Singer_Categories primary key(singer_id,categories_id)
);

create table if not exists Album_singer (
	album_id integer references Album (ID),
	singer_id integer references Singer(ID),
	constraint PK_Album_singer primary key(album_id,singer_id)
);

create table if not exists Collection_track (
	Collection_id integer references Collection (ID),
	Track_id integer references Track(ID),
	constraint PK_Collection_track primary key(Collection_id,track_id)
);