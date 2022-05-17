## 資料庫的核心概念 （10題）
C D B A C B A D B A

## 建立資料庫物件（30題）
1. B
2. D
3. A
4. A D
5. C
6. B
7. A
8. D
9. B
10. D
11. D
12. A
13. C
14. A
15. C D
16. C
17. C
18. A
19. C
20. B
21. D
22. C D
23. B
24. A B C
25. B
26. C
27. C
28. C
29. C
30. B
<br>

## 處理資料（16題）
1. C
<p>

2. D
<p>

3. A
<p>

4. C
<p>

5. B C
<p>

6. C
<p>

7. B
<p>

8. D
<p>

9. A
<p>

10. A
<p>

11. B
<p>

12. B
<p>

13. A B D
<p>

14. C
<p>

15. A
<p>

16. B
<br>

## 資料處存方式（20題）
D D A D A C C A A D B C B C A A D D A D

## 管理資料庫（10題）
B D C C C D D D B B

## 概念與指令介紹實作簡例（10題）
A C B C A A D C B B

## SQL 綜合考題
1. 
    ```sql
    SELECT Subject.subject_id, Subject.subject_name, Subject.note, Teacher teacher__name, Groups.group__name FROM Subject 
    LEFT JOIN Teacher ON Teacher teacher_id = Subject.teacher_id 
    LEFT JOIN Groups ON Groups.group_id = Teacher.teacher_id
    ```
2.  
    <ol type="A">
    <li>列出所有主管姓名</li>

    ```sql
    SELECT s1.id, s1.name, s1.title, s1.sex, s1.slry, t1.name AS bossName 
    FROM EET001 s1
    INNER JOIN EET001 t1 ON t1.id = s1.b_id
    ```

    <li>列出各部門薪資總和，並依總和高低排名</li>
    
    ```sql
    SELECT dpt, SUM(slry), RANK() OVER(
    ORDER BY SUM(slry) DESC
    ) FROM EET001
    GROUP BY dpt
    ORDER BY SUM(slry) DESC
    ```

    <li>列出薪資不足50000的員工</li>
    
    ```sql
    SELECT name, title, slry FROM EET001
    WHERE slry < 50000
    ```


    </ol>