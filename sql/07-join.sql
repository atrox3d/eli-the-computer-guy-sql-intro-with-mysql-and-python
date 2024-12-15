use company;

create table if not exists city(
    id int auto_increment primary key,
    city text,
    state text,
    climate text,
    description text
);

desc city;

select distinct city
from client;

insert into city
    (city, state, climate, description)
values
    ('asheville', 'nc', 'temperate', 'something'),
    ('mars hill', 'nc', 'temperate', 'something'),
    ('weaverville', 'nc', 'cold', 'something'),
    ('hendersonsville', 'nc', 'hot', 'something');

    select * from city;

insert into city
    (city, state, climate, description)
values
    ('hickory', 'nc', 'hot', 'something');

insert into client
    (name, age, shirt_size, city)
values
    ('bobby', 22, 'large', 'seattle');

/***********************************************
 *      INNER JOIN
 ***********************************************/
select a.name, a.city, b.city 
from client as a
inner join city as b
on a.city = b.city;

/***********************************************
 *      LEFT JOIN
 ***********************************************/
select a.name, a.city, b.city 
from client as a
left join city as b
on a.city = b.city;

/***********************************************
 *      RIGHT JOIN
 ***********************************************/
select a.name, a.city, b.city 
from client as a
right join city as b
on a.city = b.city;


