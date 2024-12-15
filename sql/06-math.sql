use company;

select 
        count(name), 
        min(age), 
        max(age), 
        avg(age)
from client;
