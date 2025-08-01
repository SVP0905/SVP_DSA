# Write your MySQL query statement below
select s.user_id,
    round(
        case when count(c.action)=0 then 0.00
        else sum(case when c.action='confirmed' then 1 else 0 end) *1.00/count(c.action)
        end,2
    ) as confirmation_rate
from Signups s
left join Confirmations c
on c.user_id=s.user_id
group by s.user_id;