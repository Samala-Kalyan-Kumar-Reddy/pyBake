-- CREATE THE USER TABLE
DROP TABLE IF EXISTS user;
CREATE TABLE IF NOT EXISTS user(
    user_id INT NOT NULL AUTO_INCREMENT,
    firstname VARCHAR(50) NOT NULL,
    middlename VARCHAR(50) NOT NULL,
    lastname VARCHAR (50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role INT NOT NULL DEFAULT 1,
    status VARCHAR(20) NOT NULL DEFAULT "inactive",
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(user_id),
    FOREIGN KEY (role) REFERENCES role(role_id)   
);


-- CREATE THE ROLES TABLE
DROP TABLE IF EXISTS role;
CREATE TABLE IF NOT EXISTS role(
    role_id INT NOT NULL,
    role_name VARCHAR (20) NOT NULL DEFAULT 'standard',
    PRIMARY KEY (role_id) 
);

-- CREATE THE LOGIN HISTORY TABLE
CREATE TABLE login_history (
    log_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    login_time DATETIME NOT NULL,
    logout_time DATETIME,
    FOREIGN KEY (user_id) REFERENCES user(user_id)
);



DROP TABLE IF EXISTS customer;
CREATE TABLE IF NOT EXISTS customer(
    customer_id INT NOT NULL AUTO_INCREMENT,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR (50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    address VARCHAR(100) NOT NULL,
    city VARCHAR (50) NOT NULL,
    state VARCHAR(2) NOT NULL,
    notes VARCHAR(255) NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'active',
    date_created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(customer_id)   
);

--create the order table
CREATE TABLE orders (
    order_id INT NOT NULL AUTO_INCREMENT,
    order_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    order_fulfilment_date DATE,
    delivery_method VARCHAR(50) NOT NULL,
    salesperson INT NOT NULL,
    customer INT NOT NULL,
    order_status VARCHAR(30) NOT NULL DEFAULT "created",
    payment_status VARCHAR(20) NOT NULL,
    notes VARCHAR(255),
    PRIMARY KEY (order_id),
    FOREIGN KEY (salesperson) REFERENCES user (user_id),
    FOREIGN KEY (customer) REFERENCES customer(customer_id)
);

-- #ORDER_LINE TABLE
DROP TABLE IF EXISTS orderline;
CREATE TABLE IF NOT EXISTS orderline (
	orderline_id INT NOT NULL AUTO_INCREMENT,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (orderline_id),
    FOREIGN KEY (order_id) REFERENCES `orders`(order_id),
    FOREIGN KEY (product_id) REFERENCES products (product_id)
);

-- ORDER HISTORY TABLE
DROP TABLE IF EXISTS orderhistory;
CREATE TABLE IF NOT EXISTS orderhistory (
	order_history_id INT NOT NULL AUTO_INCREMENT,
    order_id INT NOT NULL,
    user_id INT NOT NULL,
    order_status INT NOT NULL,
    notes VARCHAR(255),
    date_updated TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (order_history_id),
    FOREIGN KEY (order_status) REFERENCES `orderstatus`(orderstatus_id),
    FOREIGN KEY (order_id) REFERENCES `orders`(order_id),
    FOREIGN KEY (user_id) REFERENCES `user` (user_id)
);

-- ORDER STATUS TABLE
DROP TABLE IF EXISTS orderstatus;
CREATE TABLE IF NOT EXISTS orderstatus (
	orderstatus_id INT NOT NULL AUTO_INCREMENT,
    order_status_name VARCHAR(50) NOT NULL,
    order_status_description VARCHAR (255) NOT NULL,
    PRIMARY KEY (orderstatus_id)
);

--create the productTable
DROP TABLE IF EXISTS product;
CREATE TABLE IF NOT EXISTS product (
    product_id INT NOT NULL AUTO_INCREMENT,
    product_code VARCHAR(20) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    product_price DECIMAL(10, 2) NOT NULL,
    product_description VARCHAR(255) NOT NULL,
    PRIMARY KEY (product_id)
);

