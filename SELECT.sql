select track_name,track_length from Track
where track_length = (select max(track_length) from Track);

select track_name from Track
where track_length >= 3.5;

select Collection_name from Collection
where Collection_year>=2018 and Collection_year<=2020;

select singer_name from Singer
where singer_name not like '% %';

select track_name from Track
where track_name like '%мой%' or track_name like '%My%';
