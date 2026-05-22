create database Bank;
use bank;
-- manager table
create table manager(
 manager_ssn int primary key,
    name nvarchar(20),
    branch_name nvarchar(15), 
    salary numeric(10,2),
    system__access_id int not null,
    constraint sys_access_id unique (system__access_id)

);

insert into manager (manager_ssn,name,branch_name,salary,system__access_id) values(123,'hayam','BNS',20000000.23,1122);
insert into manager (manager_ssn,name,branch_name,salary,system__access_id) values(30510,'abdo','cairo',30000000.13,2233);
insert into manager (manager_ssn,name,branch_name,salary,system__access_id) values(738,'nagm','dashtut',20000000.23,3344);
insert into manager (manager_ssn,name,branch_name,salary,system__access_id) values(3334,'khaled','meet_auqba',20846000.23,4455);
insert into manager (manager_ssn,name,branch_name,salary,system__access_id) values(321,'hossam','tezmont',20000000.23,5566);


-- department table 

create table department(

 department_code int not null,
    constraint dept_code primary key(department_code),
    name nvarchar(10)





);



insert into department (department_code,name) values (1,'sales');
insert into department (department_code,name) values (2,'CallCenter');
insert into department (department_code,name) values (3,'markting');
insert into department (department_code,name) values (4,'services');

-- employee table

create table employee(
 employee_id int not null primary key,
    first_name nvarchar(15),
    last_name nvarchar(15),
    employee_ssn int not null ,
    constraint emp_ssn unique (employee_ssn),
    department_code_FK int ,
    constraint department_FK foreign key (department_code_FK) references department (department_code),
    manager_ssn_FK int,
    constraint manager_FK foreign key (manager_ssn_FK) references manager (manager_ssn)
    

);

insert into employee (employee_id,first_name,last_name,employee_ssn,department_code_FK,manager_ssn_FK) values (1,'sayed','hany',120,1,123);
insert into employee (employee_id,first_name,last_name,employee_ssn,department_code_FK,manager_ssn_FK) values (2,'othman','hany',122,2,30510);
insert into employee (employee_id,first_name,last_name,employee_ssn,department_code_FK,manager_ssn_FK) values (3,'anas','dahshan',190,3,738);
insert into employee (employee_id,first_name,last_name,employee_ssn,department_code_FK,manager_ssn_FK) values (4,'belal','hammad',180,4,3334);
insert into employee (employee_id,first_name,last_name,employee_ssn,manager_ssn_FK) values (5,'mohamed','hany',170,321);

-- customer table 

create table customer (
 
 customer_ssn int not null ,
    constraint c_ssn primary key(customer_ssn),
    first_name nvarchar(20),
    last_name nvarchar(15),
    funds numeric(10,2)



);

insert into customer (customer_ssn,first_name,last_name,funds) values(90,'abdo','sayed',93684638.87);
insert into customer (customer_ssn,first_name,last_name,funds) values(80,'abdo','ayman',93684638.87);
insert into customer (customer_ssn,first_name,last_name,funds) values(70,'abdo','mostafa',64684638.87);
insert into customer (customer_ssn,first_name,last_name,funds) values(60,'ahmed','sayed',99999999.87);
insert into customer (customer_ssn,first_name,last_name,funds) values(50,'delete','1',99999999.87);
insert into customer (customer_ssn,first_name,last_name,funds) values(40,'updatee','1',99999999.87);
select* from customer;


-- .........ya rab full mark ......


delete from customer where first_name='delete';
update customer set first_name ='updated successfully' where first_name='updatee';
select* from customer;



-- deal_with
create table deal_with(

 employee_id_FK int ,
    constraint emmployee_FK foreign key (employee_id_FK) references employee (employee_id),
    customer_ssn_FK int,
    constraint customer_FK foreign key (customer_ssn_FK) references customer (customer_ssn)
    
 



);

insert into deal_with(employee_id_FK,customer_ssn_FK) values(1,90);
insert into deal_with(employee_id_FK,customer_ssn_FK) values(1,80);
insert into deal_with(employee_id_FK,customer_ssn_FK) values(3,60);


-- phone 

create table phone(phone nvarchar(11) primary key,
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
