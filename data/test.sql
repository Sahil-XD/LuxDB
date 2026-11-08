CREATE TABLE users(
    id int primary key,
    name varchar(50)
);

CREATE TABLE orders(
    order_id int PRIMARY KEY,
    user_id int,
    amount decimal(10,2),
    FOREIGN KEY (user_id) REFERENCES users(id)
);