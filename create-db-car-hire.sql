DROP DATABASE IF EXISTS `sql_car_hire`;
CREATE DATABASE `sql_car_hire`;
USE `sql_car_hire`;


CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(20) NOT NULL
);


INSERT INTO categories (category_name) VALUES 
    ('Small'), 
    ('Family'), 
    ('Van');


CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(15),
    UNIQUE (email)
);


CREATE TABLE vehicles (
    vehicle_id INT AUTO_INCREMENT PRIMARY KEY,
    category_id INT,
    is_available BOOLEAN DEFAULT TRUE,
    CONSTRAINT fk_category FOREIGN KEY (category_id) REFERENCES categories(category_id)
);


CREATE TABLE bookings (
    booking_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    vehicle_id INT,
    date_of_hire DATE NOT NULL,
    date_of_return DATE NOT NULL,
    booking_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    payment_status ENUM('Paid', 'Unpaid') DEFAULT 'Unpaid',
    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
    CONSTRAINT fk_vehicle FOREIGN KEY (vehicle_id) REFERENCES vehicles(vehicle_id),
    CHECK (date_of_return >= date_of_hire AND DATEDIFF(date_of_return, date_of_hire) <= 7) 
);

CREATE TABLE invoices (
    invoice_id INT AUTO_INCREMENT PRIMARY KEY,
    booking_id INT,
    total_amount DECIMAL(10, 2) NOT NULL,
    payment_date DATETIME,
    CONSTRAINT fk_booking FOREIGN KEY (booking_id) REFERENCES bookings(booking_id)
);
