\c postgres

DROP DATABASE IF EXISTS warehouse1;
CREATE DATABASE warehouse1

\c warehouse1

DROP TABLE IF EXISTS employee;
CREATE TABLE employee(
    user_name VARCHAR(10) PRIMARY KEY,
    password VARCHAR(20),
    lead_by VARCHAR(10) REFERENCEs employee
);

DROP TABLE IF EXISTS warehouse;
CREATE TABLE warehouse(
    id SERIAL PRIMARY KEY,
    name VARCHAR(20)
);

DROP TABLE IF EXISTS item;
CREATE TABLE item(
    id SERIAL PRIMARY KEY,
    state VARCHAR(15),
    category VARCHAR(25),
    warehouse_id INT REFERENCEs warehouse,
    date_of_stock TIMESTAMP
);

--INSERT INTO employee(user_name,password,lead_by) VALUES ()