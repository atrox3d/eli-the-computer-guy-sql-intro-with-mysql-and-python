create database if not exists company;

use company;

create table if not exists client(
    id int auto_increment primary key,
    name text,
    age int,
    shirt_size text
);

show tables;
desc client;
select * from client;

