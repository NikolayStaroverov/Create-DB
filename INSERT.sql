insert into Singer (singer_name)
values
	('Singer_1'),
	('Singer_2'),
	('Singer_3'),
	('Singer_4'),
	('Singer5 Singer5');

insert into Categories (category_name)
values
	('Category_1'),
	('Category_2'),
	('Category_3'),
	('Category_4');

insert into Album (album_name,album_year)
values
	('Album_1',2005),
	('Album_2',2010),
	('Album_3',2015),
	('Album_4',2020);

insert into Track (album_id,track_name,track_length)
values
	(1,'Track_1',2.00),
	(2,'Track_2',2.50),
	(3,'Track_3',3.00),
	(4,'Track_4',3.50),
	(1,'Track_5',3.00),
	(2,'Track_6',2.50),
	(3,'My way',4.00);

insert into Collection(Collection_name,Collection_year)
values
	('Collection_1',2015),
	('Collection_2',2016),
	('Collection_3',2017),
	('Collection_4',2018),
	('Collection_5',2019);


insert into Album_singer (album_id,singer_id)
values
	(1,1),
	(1,2),
	(2,3),
	(2,4),
	(3,5),
	(3,1),
	(4,2),
	(1,3),
	(4,5);

insert into Singer_Categories (singer_id,categories_id)
values
	(1,1),
	(2,2),
	(3,3),
	(4,4),
	(5,1),
	(1,2),
	(2,3),
	(3,4),
	(4,1);

insert into Collection_track (Collection_id,Track_id)
values
	(1,1),
	(2,2),
	(3,3),
	(4,4),
	(5,5),
	(1,6),
	(2,7),
	(3,1),
	(4,2);
