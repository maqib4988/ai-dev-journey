DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS customers;

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    city VARCHAR(50),
    signup_date DATE NOT NULL
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(customer_id),
    amount NUMERIC(10, 2) NOT NULL,
    order_date DATE NOT NULL
);

INSERT INTO customers (name, email, city, signup_date) VALUES
('Aaqib Khan', 'aaqib@example.com', 'Islamabad', '2024-01-15'),
('Sara Ahmed', 'sara@example.com', 'Lahore', '2024-02-10'),
('Bilal Raza', 'bilal@example.com', 'Karachi', '2024-03-05'),
('Hina Tariq', 'hina@example.com', 'Islamabad', '2024-04-20');

INSERT INTO orders (customer_id, amount, order_date) VALUES
(1, 250.00, '2024-05-01'),
(1, 120.50, '2024-06-15'),
(2, 75.00, '2024-05-20'),
(3, 300.00, '2024-06-01'),
(3, 45.25, '2024-06-10'),
(4, 500.00, '2024-06-25');