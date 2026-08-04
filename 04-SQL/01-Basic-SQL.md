# SQL Basics

## 1. Introduction to SQL
SQL stands for Structured Query Language. It is used to interact with relational databases.

### Why we use it
- To store and retrieve data
- To update records
- To analyze business data

### Example
```sql
SELECT * FROM employees;
```

---

## 2. What is a Database?
A database is an organized collection of data.

### Example
A company database may store employee, customer, and order information.

---

## 3. RDBMS
RDBMS stands for Relational Database Management System. It stores data in tables with relationships between them.

### Examples
- MySQL
- PostgreSQL
- SQL Server
- Oracle

---

## 4. SQL Syntax
SQL statements are written using keywords like SELECT, INSERT, UPDATE, and DELETE.

### Example
```sql
SELECT first_name FROM employees;
```

---

## 5. Data Types
Common SQL data types include:
- `INT` for integers
- `VARCHAR` for text
- `DATE` for dates
- `BOOLEAN` for true/false

### Example
```sql
CREATE TABLE students (
    id INT,
    name VARCHAR(100),
    birth_date DATE
);
```

---

## 6. Creating Database
### CREATE DATABASE
Used to create a new database.

### Example
```sql
CREATE DATABASE school_db;
```

---

## 7. Creating Tables
### CREATE TABLE
Used to create a table in a database.

### Example
```sql
CREATE TABLE employees (
    id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    salary INT
);
```

---

## 8. Constraints
Constraints are rules applied to table columns.

### PRIMARY KEY
Uniquely identifies each row.

```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);
```

### FOREIGN KEY
Links one table to another.

```sql
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

### UNIQUE
Ensures values are unique.

```sql
CREATE TABLE users (
    email VARCHAR(100) UNIQUE
);
```

### NOT NULL
Prevents empty values.

```sql
CREATE TABLE employees (
    name VARCHAR(100) NOT NULL
);
```

### DEFAULT
Assigns a default value.

```sql
CREATE TABLE products (
    stock INT DEFAULT 0
);
```

### CHECK
Ensures values meet a condition.

```sql
CREATE TABLE employees (
    age INT CHECK (age >= 18)
);
```

---

## 9. CRUD Operations
CRUD stands for Create, Read, Update, Delete.

### INSERT
Adds new rows.

```sql
INSERT INTO employees (id, first_name, last_name, salary)
VALUES (1, 'John', 'Doe', 50000);
```

### SELECT
Reads data from a table.

```sql
SELECT * FROM employees;
```

### UPDATE
Changes existing data.

```sql
UPDATE employees
SET salary = 55000
WHERE id = 1;
```

### DELETE
Removes rows.

```sql
DELETE FROM employees
WHERE id = 1;
```

---

## 10. Filtering Data
Filtering helps retrieve only relevant rows.

### WHERE
```sql
SELECT * FROM employees
WHERE salary > 50000;
```

### AND
```sql
SELECT * FROM employees
WHERE department = 'IT' AND salary > 50000;
```

### OR
```sql
SELECT * FROM employees
WHERE department = 'IT' OR department = 'HR';
```

### NOT
```sql
SELECT * FROM employees
WHERE NOT department = 'HR';
```

### IN
```sql
SELECT * FROM employees
WHERE department IN ('IT', 'HR');
```

### BETWEEN
```sql
SELECT * FROM employees
WHERE salary BETWEEN 40000 AND 70000;
```

### LIKE
```sql
SELECT * FROM employees
WHERE first_name LIKE 'J%';
```

### IS NULL
```sql
SELECT * FROM employees
WHERE department IS NULL;
```

---

## 11. Sorting
### ORDER BY
Sorts the result.

```sql
SELECT * FROM employees
ORDER BY salary DESC;
```

---

## 12. Limiting Records
### LIMIT
Used to limit the number of rows returned.

```sql
SELECT * FROM employees
LIMIT 5;
```

### TOP
Used in some databases like SQL Server to get the first rows.

```sql
SELECT TOP 5 * FROM employees;
```

---

## 13. Aggregate Functions
Aggregate functions perform calculations over a group of rows.

### COUNT()
```sql
SELECT COUNT(*) FROM employees;
```

### SUM()
```sql
SELECT SUM(salary) FROM employees;
```

### AVG()
```sql
SELECT AVG(salary) FROM employees;
```

### MIN()
```sql
SELECT MIN(salary) FROM employees;
```

### MAX()
```sql
SELECT MAX(salary) FROM employees;
```

---

## 14. GROUP BY
Groups rows that have the same values.

```sql
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
```

---

## 15. HAVING
Filters groups after aggregation.

```sql
SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department
HAVING AVG(salary) > 50000;
```

---

## 16. DISTINCT
Removes duplicate values.

```sql
SELECT DISTINCT department FROM employees;
```

---

## 17. Aliases (AS)
Aliases give a temporary name to a column or table.

```sql
SELECT first_name AS fname, last_name AS lname
FROM employees;
```

---

## 18. Comments
Comments help explain SQL code.

```sql
-- This is a single-line comment
SELECT * FROM employees;
```

```sql
/* This is a
multi-line comment */
SELECT * FROM employees;
```

---

## 19. SQL Operators
Common operators include:
- `=` equal to
- `!=` or `<>` not equal
- `>` greater than
- `<` less than
- `>=` greater than or equal
- `<=` less than or equal

### Example
```sql
SELECT * FROM employees
WHERE salary >= 50000;
```

---

## 20. Practice Questions
- Find all employees with salary greater than 50000.
- Count how many employees work in each department.
- Find the highest salary in the company.
- List all unique departments.
