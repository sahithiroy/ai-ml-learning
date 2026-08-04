# Advanced SQL

## 1. Joins
Joins are used to combine rows from two or more tables.

### INNER JOIN
Returns matching rows.

```sql
SELECT e.first_name, d.department_name
FROM employees e
INNER JOIN departments d ON e.department_id = d.id;
```

### LEFT JOIN
Returns all rows from the left table and matching rows from the right.

```sql
SELECT e.first_name, d.department_name
FROM employees e
LEFT JOIN departments d ON e.department_id = d.id;
```

### RIGHT JOIN
Returns all rows from the right table and matching rows from the left.

```sql
SELECT e.first_name, d.department_name
FROM employees e
RIGHT JOIN departments d ON e.department_id = d.id;
```

### FULL OUTER JOIN
Returns all rows from both tables.

```sql
SELECT e.first_name, d.department_name
FROM employees e
FULL OUTER JOIN departments d ON e.department_id = d.id;
```

### CROSS JOIN
Returns the Cartesian product of both tables.

```sql
SELECT *
FROM employees
CROSS JOIN departments;
```

### SELF JOIN
Joins a table to itself.

```sql
SELECT e1.first_name, e2.first_name AS manager_name
FROM employees e1
LEFT JOIN employees e2 ON e1.manager_id = e2.id;
```

---

## 2. UNION
Combines results from two SELECT statements.

```sql
SELECT first_name FROM employees
UNION
SELECT first_name FROM managers;
```

---

## 3. UNION ALL
Like UNION, but keeps duplicates.

```sql
SELECT first_name FROM employees
UNION ALL
SELECT first_name FROM managers;
```

---

## 4. INTERSECT
Returns common rows between two queries.

```sql
SELECT first_name FROM employees
INTERSECT
SELECT first_name FROM managers;
```

---

## 5. EXCEPT
Returns rows from the first query that are not in the second.

```sql
SELECT first_name FROM employees
EXCEPT
SELECT first_name FROM managers;
```

---

## 6. Subqueries
A subquery is a query inside another query.

### Scalar subquery
```sql
SELECT first_name
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```

### Correlated subquery
```sql
SELECT e.first_name
FROM employees e
WHERE salary > (
    SELECT AVG(salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id
);
```

### Nested subquery
```sql
SELECT *
FROM employees
WHERE department_id IN (
    SELECT id FROM departments WHERE department_name = 'IT'
);
```

---

## 7. Common Table Expressions (CTE)
CTEs make complex queries easier to read.

```sql
WITH high_salary AS (
    SELECT * FROM employees WHERE salary > 70000
)
SELECT * FROM high_salary;
```

---

## 8. Recursive CTE
Useful for hierarchical data.

```sql
WITH RECURSIVE cte AS (
    SELECT id, manager_id, first_name
    FROM employees
    WHERE manager_id IS NULL

    UNION ALL

    SELECT e.id, e.manager_id, e.first_name
    FROM employees e
    JOIN cte ON e.manager_id = cte.id
)
SELECT * FROM cte;
```

---

## 9. Window Functions
Window functions perform calculations across a set of rows.

### ROW_NUMBER()
```sql
SELECT first_name, salary,
ROW_NUMBER() OVER (ORDER BY salary DESC) AS rn
FROM employees;
```

### RANK()
```sql
SELECT first_name, salary,
RANK() OVER (ORDER BY salary DESC) AS rnk
FROM employees;
```

### DENSE_RANK()
```sql
SELECT first_name, salary,
DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rank
FROM employees;
```

### NTILE()
```sql
SELECT first_name, salary,
NTILE(4) OVER (ORDER BY salary DESC) AS quartile
FROM employees;
```

### LEAD() and LAG()
```sql
SELECT first_name, salary,
LEAD(salary) OVER (ORDER BY salary) AS next_salary,
LAG(salary) OVER (ORDER BY salary) AS previous_salary
FROM employees;
```

### FIRST_VALUE() and LAST_VALUE()
```sql
SELECT first_name, salary,
FIRST_VALUE(salary) OVER (ORDER BY salary DESC) AS highest_salary,
LAST_VALUE(salary) OVER (ORDER BY salary DESC) AS lowest_salary
FROM employees;
```

---

## 10. CASE Statement
Used for conditional logic in queries.

```sql
SELECT first_name,
CASE
    WHEN salary > 70000 THEN 'High'
    WHEN salary > 50000 THEN 'Medium'
    ELSE 'Low'
END AS salary_band
FROM employees;
```

---

## 11. Views
A view is a virtual table based on a query.

```sql
CREATE VIEW high_salary_employees AS
SELECT * FROM employees WHERE salary > 70000;
```

---

## 12. Indexes
Indexes improve query performance.

```sql
CREATE INDEX idx_employees_salary ON employees(salary);
```

---

## 13. Stored Procedures
Stored procedures are reusable SQL code blocks.

```sql
CREATE PROCEDURE get_high_salary_employees AS
SELECT * FROM employees WHERE salary > 70000;
```

---

## 14. Functions
SQL functions can return values based on input.

```sql
CREATE FUNCTION get_bonus(salary INT)
RETURNS INT
AS
BEGIN
    RETURN salary * 10 / 100;
END;
```

---

## 15. Triggers
Triggers automatically run when certain events occur.

```sql
CREATE TRIGGER log_employee_insert
AFTER INSERT ON employees
FOR EACH ROW
BEGIN
    INSERT INTO audit_log (message) VALUES ('New employee added');
END;
```

---

## 16. Transactions
Transactions group SQL statements into one unit of work.

### COMMIT
```sql
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
UPDATE accounts SET balance = balance + 100 WHERE id = 2;
COMMIT;
```

### ROLLBACK
```sql
START TRANSACTION;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
ROLLBACK;
```

### SAVEPOINT
```sql
START TRANSACTION;
SAVEPOINT sp1;
UPDATE accounts SET balance = balance - 100 WHERE id = 1;
ROLLBACK TO sp1;
COMMIT;
```

---

## 17. Normalization
Normalization organizes tables to reduce redundancy.

### 1NF
Each column contains atomic values.

### 2NF
No partial dependency on a composite key.

### 3NF
No transitive dependency.

### BCNF
A stronger form of 3NF.

---

## 18. Denormalization
Denormalization adds redundant data to improve read performance.

---

## 19. Query Optimization
Optimization makes queries faster and more efficient.

### Tips
- Use indexes
- Avoid `SELECT *`
- Filter early with `WHERE`
- Use joins carefully

---

## 20. Execution Plan
An execution plan shows how the database will run a query.

```sql
EXPLAIN SELECT * FROM employees WHERE salary > 50000;
```

---

## 21. Temporary Tables
Temporary tables are used for intermediate results.

```sql
CREATE TEMP TABLE temp_employees AS
SELECT * FROM employees WHERE salary > 60000;
```

---

## 22. SQL Performance Tips
- Use indexes on frequently searched columns
- Limit returned rows
- Avoid unnecessary joins
- Use `WHERE` before `GROUP BY`
- Analyze query plans

---

## 23. SQL for Data Analysis
### Date Functions
```sql
SELECT CURRENT_DATE;
```

### String Functions
```sql
SELECT UPPER(first_name) FROM employees;
```

### NULL Handling
```sql
SELECT COALESCE(department, 'Unknown') FROM employees;
```

### Conditional Aggregation
```sql
SELECT
    SUM(CASE WHEN salary > 50000 THEN 1 ELSE 0 END) AS high_salary_count
FROM employees;
```

### Pivot & Unpivot
```sql
SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department;
```

---

## 24. SQL Interview Questions
- What is the difference between `WHERE` and `HAVING`?
- What is the difference between `INNER JOIN` and `LEFT JOIN`?
- What is a primary key?
- What is a subquery?
- What is normalization?

---

## 25. Real-world SQL Problems
- Find the top 3 highest-paid employees.
- Calculate average salary per department.
- Find customers who placed orders in the last 30 days.
- Identify duplicate rows in a table.
