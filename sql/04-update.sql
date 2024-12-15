use company;

update client
set city = 'asheville'
where id in (1, 4, 6);

update client
set city = 'mars hill'
where id = 2;

update client
set city = 'weaverville'
where id = 3;

update client
set city = 'hendersonsville'
where id = 5;

select * from client;

update client
set age = 40
where id = 6;