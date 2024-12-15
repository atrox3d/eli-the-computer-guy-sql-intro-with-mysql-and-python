use company;

select * from client;

select name, age from client 
limit 3;

select name, age from client 
where age > 40;

select name, age from client 
where age >= 50;

select * from client 
where name = 'fred';

select * from client 
where name like '%e%';

select * from client 
where name like 's__';

select * from client 
order by name desc;


