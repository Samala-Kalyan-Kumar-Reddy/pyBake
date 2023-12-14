select orders.order_id,
order_date,
delivery_method,
order_fulfilment_date,
user.firstname,
user.lastname,
order_status,
sum(orderline.quantity) as total_quantity,
sum(orderline.quantity * products.product_price) as amount,
orders.notes
from orders 
join user on user.user_id = orders.salesperson
join orderline on orders.order_id = orderline.order_id 
join products on products.product_id = orderline.product_id
group by order_id;