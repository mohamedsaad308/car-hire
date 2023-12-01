# Car Hire Management System.
 
This is a simple Flask microservice for managing customer information, It 's a part of car hire management system. It includes (Read, Update, Delete) operations for customer records stored in a MySQL database.

## Project Structure

```
.
├── api
│   ├── app.py
│   ├── config.py
│   ├── customers
│   │   ├── __init__.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── db.py
│   ├── Dockerfile
│   ├── __init__.py
│   └── requirements.txt
├── create-db-car-hire.sql
├── docker-compose.yml
├── ERD_diagram.png
└── populate_customers_table.sql

```


- **api:** Contains the Flask application code.
  - **app.py:** Main application file.
  - **config.py:** Configuration file for the application.
  - **customers:** Package for customer-related functionality.
    - **__init__.py:** Package initialization.
    - **urls.py:** URL routing for customer views.
    - **views.py:** Customer views and business logic.
  - **db.py:** Database connection and initialization.
  - **Dockerfile:** Docker configuration for building the app image.
  - **requirements.txt:** List of Python dependencies.

- **create-db-car-hire.sql:** SQL script for creating the database schema.

- **docker-compose.yml:** Docker Compose configuration for running the app and MySQL.

- **ERD_diagram.png:** Entity-Relationship Diagram for the database schema.

- **populate_customers_table.sql:** SQL script for populating the customers table.

## Getting Started

Follow the steps below to set up and run the Flask app:

1. Clone this repository:
   ```bash
   git clonehttps://github.com/mohamedsaad308/car-hire.git
   cd car-hire
2. Create .env file with these env variables:
    ```
    MYSQL_HOST=db
    MYSQL_USER=username
    MYSQL_PASSWORD=password
    MYSQL_DATABASE=sql_car_hire # If you change it here you will have to change it in create database script
3. Build and run the Docker containers:
docker-compose up --build

4. Access the app at http://localhost:5000.

## Usage
- The app provides CRUD operations for managing customer records. except for Create,
- Access the customer management interface through the provided API endpoints.

## Endpoints

1. Get Customer by ID

Endpoint: GET /<customer_id>

Description: Retrieve customer information by their ID.

Parameters:

customer_id (integer): ID of the customer to retrieve.

Example Request:

    
    curl -X GET http://localhost:5000/api/customers/1

Example Response:

    {
    "customer_id": 1,
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "phone": "123-456-7890"
    }

2. Update Customer
Endpoint: PUT /<customer_id>

Description: Update customer information.

Parameters:

customer_id (integer): ID of the customer to update.

Request Body:

    {
    "first_name": "NewFirstName",
    "last_name": "NewLastName",
    "email": "new.email@example.com",
    "phone": "987-654-3210"
    }

Example Request:

    curl -X PUT -H "Content-Type: application/json" -d '{"first_name": "NewFirstName", "last_name": "NewLastName", "email": "new.email@example.com", "phone": "987-654-3210"}' http://localhost:5000/api/customers/1

Example Response:

    {
    "message": "Customer updated successfully"
    }

3. Delete Customer
Endpoint: DELETE /<customer_id>

Description: Delete a customer.

Parameters:

customer_id (integer): ID of the customer to delete.

Example Request:

    curl -X DELETE http://localhost:5000/api/customers/1

Example Response:

    {}  # Empty response with status code 204
