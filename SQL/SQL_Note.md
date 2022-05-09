# SQL quick note

## [SELECT](select.py) : 取出欄位

```sql
SELECT column1, column2, ... FROM table_name;
```
 取某個欄位的『不重複資料』時，可以使用 **Distinct**
```sql
SELECT DISTINCT column1, column2, ... FROM table_name;
```

當想計算『滿足條件的資料有幾筆』時，可以使用 **Count**

```sql
SELECT COUNT(DISTINCT column1, column2, ...) FROM table_name;
```
<br>

## [INSERT INTO](insertRow.py): 新增

- Specify both the column names and the values to be inserted
  ```sql
  INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
   ```

- If you are adding values for all the columns of the table
 
   ```sql
   INSERT INTO table_name VALUES (value1, value2, value3, ...);
   ```
<br>

## ORDER BY: 排序
```sql
SELECT column1, column2, ... FROM table_name ORDER BY column1, column2, ... ASC|DESC;
```

<br>

## WHERE : 條件判斷

```sql
SELECT * FROM table_name WHERE condition(s);
```

### Operators
 Refer: https://www.w3schools.com/sql/sql_like.asp

- AND
  ```sql
  SELECT column1, column2, ... FROM table_name WHERE condition1 AND condition2 AND condition3 ...;
  ```

- OR
  ```sql
  SELECT column1, column2, ... FROM table_name WHERE condition1 OR condition2 OR condition3 ...;
  ```

- NOT
  ```sql
  SELECT column1, column2, ... FROM table_name WHERE NOT condition;
  ```

- (NOT) LIKE : (不)匹配
   ```sql
   SELECT column1, column2, ... FROM table_name WHERE columnN (NOT) LIKE pattern;
   ```
    
- (NOT) IN : shorthand for multiple **OR**

  ```sql
  SELECT column_name(s) FROM table_name WHERE column_name IN (value1, value2, ...);
  ```

- (NOT) BETWEEN ... AND ... : selects values within a given range

  ```sql
  SELECT column_name(s) FROM table_name WHERE column_name BETWEEN value1 AND value2;
  ```

<br>

## NULL: 顯示缺失值

- IS NULL
  ```sql
  SELECT column_names FROM table_name WHERE column_name IS NULL;
  ```

- IS NOT NULL
  ```sql
  SELECT column_names FROM table_name WHERE column_name IS NOT NULL;
  ```

<br>

## [UPDATE ... SET](delete_update.py): 修改
```sql
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
```

<br>

## DELETE FROM ... (WHERE): 刪除

```sql
DELETE FROM table_name WHERE condition(s);
```

若要刪除整個表格，則執行:

```sql
DELETE FROM table_name;
```

<br>

## Function
- MIN
  ```sql
  SELECT MIN(column_name) FROM table_name WHERE condition(s);
  ```
- MAX
  ```sql
  SELECT MAX(column_name) FROM table_name WHERE condition(s);
  ```
- COUNT
  ```sql
  SELECT COUNT(column_name) FROM table_name WHERE condition(s);
  ```
 - AVG
   ```sql
   SELECT AVG(column_name) FROM table_name WHERE condition(s);
   ```
 - SUM
   ```sql
   SELECT SUM(column_name) FROM table_name WHERE condition(s);
   ```
  <br>

## AS: 別名
- Column 
  ```sql
  SELECT column_name AS alias_name FROM table_name;
  ```

- Table
  ```sql
  SELECT column_name(s) FROM table_name AS alias_name;
  ```
<br>

## JOIN: 關聯語句 
Refer: https://ithelp.ithome.com.tw/articles/10207129

- INNER JOIN
  ```sql
  SELECT column_name(s) FROM table1 INNER JOIN table2 ON table1.column_name = table2.column_name;
  ```

- LEFT JOIN
  ```sql
  SELECT column_name(s) FROM table1 LEFT JOIN table2 ON table1.column_name = table2.column_name;
  ```

- RIGHT JOIN
  ```sql
  SELECT column_name(s) FROM table1 RIGHT JOIN table2 ON table1.column_name = table2.column_name;
  ```

- FULL JOIN
  ```sql
  SELECT column_name(s) FROM table1 FULL OUTER JOIN table2 ON table1.column_name = table2.column_name WHERE condition;
  ```
<br>

## GROUP BY: groups rows that have the same values into summary rows

  ```sql
  SELECT column_name(s) FROM table_name WHERE condition GROUP BY column_name(s) ORDER BY column_name(s);
  ```
<br>

## HAVING: 條件判斷(搭配Function)

  ```sql
  SELECT column_name(s) FROM table_name WHERE condition GROUP BY column_name(s) HAVING condition ORDER BY column_name(s);
  ```
<br>

## [CREATE](create.py): 創建資料庫與表單
- DATABASE
  ```sql
  CREATE DATABASE data_base_name;
  ```

- table
  ```sql
  CREATE TABLE table_name(
    column1 datatype constraint,
    column2 datatype constraint,
    column3 datatype constraint,
    ...
  );
  ```
  refer: https://www.w3schools.com/sql/sql_constraints.asp
<br>

## [DROP](drop.py): 刪除資料庫與表單
- DATABASE
  ```sql
  DROP DATABASE data_base_name;
  ```

- table
  ```sql
  DROP TABLE table_name(
    column1 datatype constraint,
    column2 datatype constraint,
    column3 datatype constraint,
    ...
  );
  ```
<br>

## ALTER TABLE: 修改表格
- ADD Column
  ```sql
  ALTER TABLE table_name ADD column_name datatype;
  ```

- DROP COLUMN
  ```sql
  ALTER TABLE table_name DROP COLUMN column_name;
  ```

- MODIFY COLUMN
  ```sql
  ALTER TABLE table_name MODIFY COLUMN column_name datatype;
  ```

