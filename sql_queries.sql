
create table emp_details(user_id varchar(10),e_password varchar(20),emp_role int,primary key(user_id));

create table employee(e_name varchar(20),eid varchar(10),join_date date,ph_no bigint,
mail_id varchar(30),salary int,manager_id varchar(10),m_status varchar(10),h_status varchar(10),
prev_rating float,prev_hike_date int,curr_rating float default 0,primary key(eid));

create table emp_resp(e_name varchar(20),eid varchar(10),no_of_task_assigned int,
no_of_task_completed int,no_of_hrs_saved int,no_of_defects_found int,no_of_defects_fixed int,
additional_accomplishments varchar(200),primary key(e_name,eid),foreign key(eid) references employee(eid) on delete cascade);

create table manager(m_name varchar(20),m_id varchar(10),mail_id varchar(30),mgr_start_date date,
ph_no bigint,primary key(m_id));

create table m_resp(mid varchar(10),m_name varchar(20),no_of_task_assigned int,no_of_task_completed int,
no_of_hrs_saved int,no_of_defects_found int,no_of_defects_fixed int,effectiveness int,integrity int,
emp_id varchar(20),accountability int ,quality_of_work int,time_management int,additional_note varchar(200),foreign key(mid) references manager(m_id) on delete cascade,primary key(mid,m_name));

-- ALTER TABLE [dbo].[States]  WITH CHECK ADD  CONSTRAINT [FK_States_Countries] FOREIGN KEY([CountryID])
-- REFERENCES [dbo].[Countries] ([CountryID])
-- ON DELETE CASCADE

insert into manager values("Suhas","MGR_1","suhas58879@gmail.com","2017-11-23",9123434484);
insert into manager values("Bhagya","MGR_2","bb7617254@gmail.com","2016-01-16",9185793564);
insert into manager values("Bindu","MGR_3","bindu58879@gmail.com","2018-01-01",9184534234);

insert into employee values("Satish","EMP_1","2020-08-23",9123561298,"ssatish58879@gmail.com",1000000,"MGR_1",'Pending','Pending',8.5,12,0);
insert into employee values("Nakul","EMP_2","2019-07-14",9134532426,"Nakul43255@gmail.com",1200000,"MGR_1",'Pending','Pending',7.8,4,0);
insert into employee values("Rahul","EMP_3","2018-05-01",9198453242,"r25260260@gmail.com",1300000,"MGR_2",'Pending','Pending',9.4,4,0);
insert into employee values("Sairam","EMP_4","2022-03-15",9143535236,"Sairam58879@gmail.com",950000,"MGR_2",'Pending','Pending',8.3,8,0);
insert into employee values("Tarun","EMP_5","2019-08-16",9145868894,"Tarun58879@gmail.com",1500000,"MGR_3",'Pending','Pending',8.5,12,0);
insert into employee values("Varsha","EMP_6","2022-02-08",9145934752,"vv0074992@gmail.com",1100000,"MGR_1",'Pending','Pending',9.6,0,0);
insert into employee values("Vanshika","EMP_7","2019-10-31",9134334534,"vv7665541@gmail.com",1300000,"MGR_2",'Pending','Pending',8.7,12,0);
insert into employee values("Monika","EMP_8","2018-11-29",9145846346,"mm5570246@gmail.com",950000,"MGR_3",'Pending','Pending',7.3,8,0);


insert into emp_details values('MGR_1','m1',1),
                              ('MGR_2','m2',1),
                              ('MGR_3','m3',1),
                              ('EMP_1','e1',),
                              ('EMP_2','e2',),
                              ('EMP_3','e3',),
                              ('EMP_4','e4',),
                              ('EMP_5','e5',),
                              ('EMP_6','e6',),
                              ('EMP_7','e7',),
                              ('EMP_8','e8',),
                              ('HR_1','h1',),