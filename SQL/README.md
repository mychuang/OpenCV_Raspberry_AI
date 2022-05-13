# DataBase & SQL

## SQL語法
- 透過一些簡單[範例](SQLexam.md)了解SQL
- Python搭配SQL與語法字典可以參考[SQL_Note.md](SQL_Note.md)

<br>

## 資料庫設計原理參考 [DataBase.md](DataBase.md)
<br>

## SQL 挑戰

### 建立表單:
1. 學生表
```sql
-- 建立學生表單
CREATE TABLE Student(
 s_id VARCHAR(20),
 s_name VARCHAR(20) NOT NULL DEFAULT '',
 s_birth VARCHAR(20) NOT NULL DEFAULT '',
 s_sex VARCHAR(10) NOT NULL DEFAULT '',
 PRIMARY KEY (s_id)
);

insert into Student values('01' , '趙雷' , '1990-01-01' , '男');
insert into Student values('02' , '錢電' , '1990-12-21' , '男');
insert into Student values('03' , '孫風' , '1990-05-20' , '男');
insert into Student values('04' , '李雲' , '1990-08-06' , '男');
insert into Student values('05' , '周梅' , '1991-12-01' , '女');
insert into Student values('06' , '吳蘭' , '1992-03-01' , '女');
insert into Student values('07' , '鄭竹' , '1989-07-01' , '女');
insert into Student values('08' , '王菊' , '1990-01-20' , '女');
```
<img src="./t01.png" width="300px" /> <p>

2. 課程表
```sql
CREATE TABLE Course(
 c_id  VARCHAR(20),
 c_name VARCHAR(20) NOT NULL DEFAULT '',
 t_id VARCHAR(20) NOT NULL,
 PRIMARY KEY(c_id)
);

insert into Course values('01' , '語文' , '02');
insert into Course values('02' , '數學' , '01');
insert into Course values('03' , '英語' , '03');
```
<img src="./t02.png" width="200px" /> <p>

3. 教師表
```sql
CREATE TABLE Teacher(
 t_id VARCHAR(20),
 t_name VARCHAR(20) NOT NULL DEFAULT '',
 PRIMARY KEY(t_id)
);

insert into Teacher values('01' , '張三');
insert into Teacher values('02' , '李四');
insert into Teacher values('03' , '王五');
```
<img src="./t03.png" width="150px" /> <p>

4. 成績表
```sql
CREATE TABLE Score(
 s_id VARCHAR(20),
 c_id  VARCHAR(20),
 s_score INT(3),
 PRIMARY KEY(s_id, c_id)
);

insert into Score values('01' , '01' , 80);
insert into Score values('01' , '02' , 90);
insert into Score values('01' , '03' , 99);
insert into Score values('02' , '01' , 70);
insert into Score values('02' , '02' , 60);
insert into Score values('02' , '03' , 80);
insert into Score values('03' , '01' , 80);
insert into Score values('03' , '02' , 80);
insert into Score values('03' , '03' , 80);
insert into Score values('04' , '01' , 50);
insert into Score values('04' , '02' , 30);
insert into Score values('04' , '03' , 20);
insert into Score values('05' , '01' , 76);
insert into Score values('05' , '02' , 87);
insert into Score values('06' , '01' , 31);
insert into Score values('06' , '03' , 34);
insert into Score values('07' , '02' , 89);
insert into Score values('07' , '03' , 98);
```
<img src="./t04.png" width="200px" /> <p>

<br>

### 挑戰題庫 (to do list)
<br>

### Refer:
- https://allaboutdataanalysis.medium.com/%E8%B6%85%E7%B6%93%E5%85%B8mysql%E7%B7%B4%E7%BF%9250%E9%A1%8C-%E5%81%9A%E5%AE%8C%E9%80%99%E4%BA%9B%E4%BD%A0%E7%9A%84sql%E5%B0%B1%E9%81%8E%E9%97%9C%E4%BA%86-600fca8979a8