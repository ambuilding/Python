DROP DATABASE IF EXISTS schooldb;
CREATE DATABASE IF NOT EXISTS schooldb;
USE schooldb;
CREATE TABLE IF NOT EXISTS Student (
	ssn VARCHAR(11) NOT NULL PRIMARY KEY,
	f_name VARCHAR(20) NOT NULL,
	l_name VARCHAR(20) NOT NULL,
	phone VARCHAR(10),
	city VARCHAR(20) NOT NULL,
	zip VARCHAR(5) NOT NULL
);

CREATE TABLE IF NOT EXISTS Course (
	number VARCHAR(3) NOT NULL PRIMARY KEY,
	name VARCHAR(30) NOT NULL,
	room INT NOT NULL
);

--
-- ssn, social security number
--

CREATE TABLE IF NOT EXISTS Enrolls_in (
	ssn VARCHAR(11) NOT NULL,
	class VARCHAR(3) NOT NULL,
	score FLOAT,
	CONSTRAINT pk_enroll PRIMARY KEY (ssn,class)
);

select * from Student where city="New York"
SELECT f_name, l_name FROM Student WHERE city="New York";
select ssn from Student order by f_name asc;
select ssn from Student order by f_name desc;
select DISTINCT city from Student;

select avg(score) from Enrolls_in;
select avg(score) from Enrolls_in where class="c1";
select class, avg(score) from Enrolls_in group by `class`;
select class, avg(score) from Enrolls_in group by `class` having count(score) > 1;

select class, avg(score) as average from Enrolls_in group by `class`;

-- Temporary table
create temporary TABLE averages SELECT class, avg(score) as average from Enrolls_in group by `class`;
SELECT * from averages where average < 90;
create temporary TABLE summary SELECT class, avg(score) as average, count(score) as count from Enrolls_in group by `class` ORDER BY count DESC;
SELECT * from summary;

-- Working across multiple tables
SELECT f_name, l_name FROM Student a, Enrolls_in b WHERE a.ssn = b.ssn;
SELECT f_name, l_name FROM Student a, Enrolls_in b WHERE a.ssn = b.ssn;
SELECT s.ssn, f_name, l_name, `class` FROM Student s, Enrolls_in e WHERE s.ssn = e.ssn;
SELECT s.ssn, f_name, l_name, `class`, score FROM Student s, Enrolls_in e WHERE s.ssn = e.ssn and f_name="John" and l_name="childs" and score>=95;
SELECT name, s.ssn, f_name, l_name, `class`, score FROM Student s, Enrolls_in e, Course c WHERE s.ssn=e.ssn and e.class=c.number and f_name="John" and l_name="childs";

-- Join
-- explicit
SELECT number, name, room, ssn, score from Course inner join Enrolls_in on Course.number = Enrolls_in.class;
-- implicit
SELECT number, name, room, ssn, score from Course, Enrolls_in where Course.number = Enrolls_in.class;

SELECT Course.name FROM Student
INNER JOIN Enrolls_in ON Student.ssn=Enrolls_in.ssn
INNER JOIN Course ON Course.number=Enrolls_in.class
WHERE f_name="JOHN";
