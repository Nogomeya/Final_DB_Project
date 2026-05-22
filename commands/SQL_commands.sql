phone nvarchar(11) primary key,
    cus_ssn_FK int ,
    constraint cus_FK foreign key (cus_ssn_FK) references customer (customer_ssn)
 



);

insert into phone (cus_ssn_FK,phone) values (90,'01154587297');
insert into phone (cus_ssn_FK,phone) values (80,'01010699237');
insert into phone (cus_ssn_FK,phone) values (70,'01115499245');
insert into phone (cus_ssn_FK,phone) values (60,'01000755398');

select * from phone;



-- DDL commands
alter table department add temp varchar(10);
alter table department modify temp int;
alter table department drop column temp;


create table temp_table(

 temp_pk int primary key ,
    name varchar(10)




);
insert into temp_table (temp_pk,name) values (2,'dr hayam');
select * from temp_table;


truncate table temp_table;
select * from temp_table;

drop table temp_table;
select * from temp_table;




-- DML commands
select employee_id ,first_name , last_name from employee;
select * from employee order by first_name;
select distinct last_name from employee;
select * from employee where employee_ssn between 100 and 172;
select * from employee where first_name like 's%';
select * from employee where last_name like '%h%';


-- .........ya rab full mark ......

select employee_id , first_name,last_name , name from employee inner join department on department_code_FK= department_code;

select employee_id,first_name , last_name , name from employee left outer join department on department_code_FK= department_code; 

select c.first_name as  cus_name , p.phone as cus_phone from customer c right join phone p on p.cus_ssn_FK=c.customer_ssn; 
-- full join by ai cause i use mysql 
SELECT e.first_name, d.name AS department_name
FROM employee e
LEFT JOIN department d ON e.department_code_FK = d.department_code
UNION
SELECT e.first_name, d.name AS department_name
FROM employee e
RIGHT JOIN department d ON e.department_code_FK = d.department_code;
-- ya rab fuul mark

select system__access_id,name, branch_name from manager where salary > (select avg(salary)from manager);

-- viewwwwwww

create view eemp_dept as select first_name , last_name , name from employee join department on department_code_FK= department_code;

select * from eemp_dept ;
