use company;

select count(name), city
from client
group by city;

select count(name), shirt_size
from client
group by shirt_size;

