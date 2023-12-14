INSERT INTO role VALUES(1,'admin'),(2,'manager'),(3,'standard');

INSERT INTO orderstatus (order_status_name,order_status_description) VALUES
('created','The initial status when an order is first placed by the customer'),
('pending payment','This status indicates that the order has been created but the payment has not been processed yet'),
('paid','This status indicates that payment has been successfully received'),
('in progress','This status signifies that the bakery is actively working on fulfilling the order'),
('ready for pickup/delivery', 'This status indicates that the order has been completed and ready for pickup/delivery'),
('completed','The order is fully processed, delivered or picked up, and the customer has received it'),
('cancelled','This status indicates that a customer has decided to cancel an order'),
('on hold', 'In case there are issues or delays with an order, you can use this status to put it on hold temporarily');


