use company;

select avg(age)
from (
    select * from client
    order by age desc
    limit 3
) as subquery;

