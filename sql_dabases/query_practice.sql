


-- Window query
select *,
rank() over (partition by product_id order by quantity_sold) as rank,
row_number() over (partition by product_id order by quantity_sold) as row_ranking,
dense_rank() over (partition by product_id order by quantity_sold) as dense_ranking,
percent_rank() over (partition by product_id order by quantity_sold) as percent_ranking
from daily_sales;



-- Top 3 Days for Each Product (by quantity)
select sale_date,quantity_sold,product_id 
from
(select *,
row_number() over (partition by product_id order by quantity_sold desc) as ranking   
from daily_sales)
where ranking<=3


-- Highest Revenue Day
select sale_date,sum(total_amount) as day_revenue from daily_sales
group by sale_date
order by day_revenue desc
limit 1



-- Average Daily Sales
select to_char(sale_date,'YYYY-MM-DD') as daily_sale, round(avg(total_amount),2)
from daily_sales
group by daily_sale
order by daily_sale asc


--  Total Quantity Sold by Category
select sum(s.quantity_sold) as quantity,p.category 
from daily_sales s
join daily_products as p
on s.product_id=p.product_id
group by p.category


-- Monthly Sale Summary
select extract(month from sale_date) as sale_month, sum(total_amount) as monthly_revenue
from daily_sales
group by sale_month
order by monthly_revenue asc

--Top 5 Best Selling Products (by Revenue)
 
select p.product_id,p.product_name, sum(s.total_amount)
from daily_products p
inner join daily_sales s
on p.product_id=s.product_id
group by p.product_id,p.product_name
order by sum(s.total_amount) desc
limit 5;

-- daily_sales 
select * from daily_sales;

-- daily_products
select * from daily_products;





