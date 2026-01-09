USE it_company;

select * from employee;

-- 1.return employee id and name from employees thoes salary is morethan  49000
select id, name, salary from employee
where salary > 49000;
-- 2.find IT employee details
select * from employee
where dept = 'it';
-- 3.Increase 10% salary for sales employees
set sql_safe_updates = 0;
update employee set salary = salary + (salary * 0.1)
where dept = 'sales';

select * from employee;
-- 4.find the employee details whoes have more than 40000 salary in IT dept.
select * from employee
where salary > 40000 and dept = 'it';
 
 -- Aggreagated functions - MIN(), MAX(), AVG(), SUM(), COUNT()
-- 5.Find the max salary in a table
SELECT MAX(SALARY) AS HIGHEST_SALARY FROM EMPLOYEE;
-- 6.Find the minimum salary in table
SELECT MIN(SALARY) AS MINIMUM_SALARY FROM EMPLOYEE;

-- 7.Find the total salary company spend on employee every month
SELECT SUM(SALARY) TOTAL_SALARY FROM EMPLOYEE;
-- 8.Find total employee count in the company
SELECT COUNT(*) TOTAL_EMPLOYEES FROM EMPLOYEE;
-- 9. Find IT and HR dept employee details
SELECT * FROM EMPLOYEE
WHERE DEPT = 'HR' AND DEPT = 'IT';

-- FIND THE IT EMPLOYEE COUNT
SELECT DEPT, COUNT(*) TOTAL_EMPLOYEE  FROM EMPLOYEE 
WHERE DEPT = 'IT';
-- FIND NON IT DEPT EMPLOYEE TOTAL SALARY
SELECT SUM(SALARY) FROM EMPLOYEE
WHERE DEPT != 'IT';




