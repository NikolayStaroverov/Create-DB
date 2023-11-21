select count(distinct singer_id), category_name from Singer_Categories
left join categories on Singer_Categories.categories_id=categories.id
group by category_name;

select count(distinct ID) from Track
where album_id = (select ID from Album where album_year>=2019 and album_year<=2020);

select album_name,AVG(track_length) from Track
left join album on track.album_id=album.id
group by album_name
order by album_name;

select distinct	singer_name from Singer
where singer_name not in (select distinct singer_name from Singer
left join album_singer on singer.id=album_singer.singer_id
left join album on album_singer.album_id=album.id
where album_year=2020)
order by singer_name;

select distinct collection_name from collection
left join collection_track on collection.id=collection_track.collection_id
left join track on collection_track.track_id=track.id
left join album on track.album_id=album.id 
left join album_singer on album.id=album_singer.album_id
left join singer on album_singer.singer_id=singer.id 
where singer_name='Singer_4'
order by collection_name; 