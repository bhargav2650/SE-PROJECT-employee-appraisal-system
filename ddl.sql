--database used empl
create table emp_details(user_id varchar(10),e_password varchar(20),emp_role int,primary key(user_id));

create table employee(e_name varchar(20),eid varchar(10),join_date date,ph_no bigint,
mail_id varchar(20),salary int,manager_id varchar(10),m_approve int,h_approve int,h_status int default 0,m_status int 0,
prev_rating float,prev_hike_date date,curr_rating float,primary key(eid));

create table emp_resp(e_name varchar(20),eid varchar(10),no_of_task_assigned int,
no_of_task_completed int,no_of_hrs_saved int,no_of_defects_found int,no_of_defects_fixed int,
additional_accomplishments varchar(200),primary key(e_name,eid),foreign key(eid) references employee(eid) on delete cascade);

create table manager(m_name varchar(20),m_id varchar(10),mail_id varchar(20),mgr_start_date date,
ph_no bigint,primary key(m_id));

create table m_resp(mid varchar(10),m_name varchar(20),no_of_task_assigned int,no_of_task_completed int,
no_of_hrs_saved int,no_of_defects_found int,no_of_defects_fixed,effectiveness int,integrity int,
conduct varchar(20),foreign key(mid) references manager(m_id),primary key(mid,m_name) on delete cascade);