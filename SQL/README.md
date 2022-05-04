# SQL quick note

## SELECT : 取出欄位
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

## WHERE : 條件判斷

```sql
SELECT * FROM table_name WHERE condition(s);
```
<br>

### SQL AND, OR and NOT Operators
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

## ORDER BY: 排序
```sql
SELECT column1, column2, ... FROM table_name ORDER BY column1, column2, ... ASC|DESC;
 ```

## INSERT INTO: 新增

- Specify both the column names and the values to be inserted
  ```sql
  INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
   ```

 - If you are adding values for all the columns of the table
 
   ```sql
   INSERT INTO table_name VALUES (value1, value2, value3, ...);
   ```

## NULL: 顯示缺失值

- IS NULL
  ```sql
  SELECT column_names FROM table_name WHERE column_name IS NULL;
  ```

- IS NOT NULL
  ```sql
  SELECT column_names FROM table_name WHERE column_name IS NOT NULL;
  ```

## UPDATE ... SET: 修改
```sql
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
```

## DELETE FROM ... (WHERE): 刪除

```sql
DELETE FROM table_name WHERE condition(s);
```

若要刪除整個表格，則執行:

```sql
DELETE FROM table_name;
```

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

## Operator

- (NOT) LIKE : (不)匹配
   ```sql
   SELECT column1, column2, ... FROM table_name WHERE columnN (NOT) LIKE pattern;
   ```
   Pattern check: https://www.w3schools.com/sql/sql_like.asp

   

    

- 1563