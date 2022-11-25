--database used empl
create table emp_details(user_id varchar(10),e_password varchar(20),emp_role int,primary key(user_id));

insert into emp_details values("EMP_1","satish@123",3);
insert into emp_details values("EMP_2","nakul@123",3);
insert into emp_details values("EMP_3","rahul@123",3);
insert into emp_details values("EMP_4","sairam@123",3);
insert into emp_details values("EMP_5","tarun@123",3);
insert into emp_details values("EMP_6","varsha@123",3);
insert into emp_details values("EMP_7","vanshika@123",3);
insert into emp_details values("EMP_8","monika@123",3);
insert into emp_details values("MGR_1","suhas@123",1);
insert into emp_details values("MGR_2","bhagya@123",1);
insert into emp_details values("MGR_3","bindu@123",1);

create table employee(e_name varchar(20),eid varchar(10),join_date date,ph_no bigint,
mail_id varchar(20),salary int,manager_id varchar(10),m_approve int,h_approve int,h_status int,m_status int,
prev_rating float,prev_hike_date date,curr_rating float);

insert into employee values("Satish","EMP_1","2020-08-23",9123561298,"ssatish58879@gmail.com",1000000,"MGR_1",1,1,0,0,4.5,"2021-11-15",4.5);
insert into employee values("Nakul","EMP_2","2019-07-14",9134532426,"Nakul43255@gmail.com",1200000,"MGR_1",1,1,0,0,4.8,"2021-11-15",4.6);
insert into employee values("Rahul","EMP_3","2018-05-01",91984532427,"r25260260@gmail.com",1300000,"MGR_2",1,1,0,0,4.4,"2021-11-15",4.6);
insert into employee values("Sairam","EMP_4","2020-09-15",9143535236,"Sairam58879@gmail.com",950000,"MGR_2",1,1,0,0,4.3,"2021-11-15",4.4);
insert into employee values("Tarun","EMP_5","2019-08-16",9145868894,"Tarun58879@gmail.com",1500000,"MGR_3",1,1,0,0,4.5,"2021-11-15",4.6);
insert into employee values("Varsha","EMP_6","2020-09-08",9145934752,"vv0074992@gmail.com",1100000,"MGR_1",1,1,0,0,4.6,"2021-11-15",4.6);
insert into employee values("Vanshika","EMP_7","2019-10-31",9134334534,"vv7665541@gmail.com",1300000,"MGR_2",1,1,0,0,4.7,"2021-11-15",4.5);
insert into employee values("Monika","EMP_8","2018-11-29",9145846346,"mm5570246@gmail.com",950000,"MGR_3",1,1,0,0,4.3,"2021-11-15",4.4);





create table emp_resp(e_name varchar(20),eid varchar(10),no_of_task_assigned int,
no_of_task_completed int,no_of_hrs_saved int,no_of_defects_found int,no_of_defects_fixed int,
additional_accomplishments varchar(200),primary key(e_name,eid),foreign key(eid) references employee(eid) on delete cascade);

-- insert into emp_resp()

create table manager(m_name varchar(20),m_id varchar(10),mail_id varchar(20),mgr_start_date date,
ph_no bigint,primary key(m_id));

insert into manager values("Suhas","MGR_1","suhas58879@gmail.com","2017-11-23",9123434484);
insert into manager values("Bhagya","MGR_2","bb7617254@gmail.com","2016-01-16",9185793564);
insert into manager values("Bindu","MGR_3","bindu58879@gmail.com","2018-01-01",9184534234);




create table m_resp(mid varchar(10),m_name varchar(20),no_of_task_assigned int,no_of_task_completed int,
no_of_hrs_saved int,no_of_defects_found int,no_of_defects_fixed,effectiveness int,integrity int,
conduct varchar(20),foreign key(mid) references manager(m_id),primary key(mid,m_name) on delete cascade);
