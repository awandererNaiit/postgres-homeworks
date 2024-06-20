CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    position VARCHAR(50),
    hire_date DATE
);

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20)
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE,
    customer_id INT REFERENCES customers(customer_id),
    total_amount DECIMAL(10, 2),
    employee_id INT REFERENCES employees(employee_id)
);
