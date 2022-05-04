# SQL quick note

假定存在以下資料，名為Customers:<br>
| CustomerID | CustomerName | PostalCode    |
|------------|--------------|---------------|
| 1          | Alfreds Futterkiste	 | 12209 |
| 2	         | Ana Trujillo Emparedados y helados | 05021 |
| 3          | Antonio Moreno Taquería   | 05023 |

## Select
從該表格中的指定欄位取出所有資料，定義如下:<br>
**Select + 要選擇的欄位 + From + 表格的名稱**<br>

例如執行下列語句:
```sql
SELECT CustomerName FROM Customers;
```
| CustomerName | 
|--------------|
| Alfreds Futterkiste	 |
| Ana Trujillo Emparedados y helados |
| Antonio Moreno Taquería   |

<br>
或取出多欄位:

```sql
SELECT CustomerName, PostalCode FROM Customers;
```
| CustomerName | PostalCode    |
|--------------|---------------|
| Alfreds Futterkiste	 | 12209 |
| Ana Trujillo Emparedados y helados | 05021 |
| Antonio Moreno Taquería   | 05023 |

<br>
或取出所有欄位:

```sql
SELECT * FROM Customers;
```
| CustomerID | CustomerName | PostalCode    |
|------------|--------------|---------------|
| 1          | Alfreds Futterkiste	 | 12209 |
| 2	         | Ana Trujillo Emparedados y helados | 05021 |
| 3          | Antonio Moreno Taquería   | 05023 |

當想取某個欄位的『不重複資料』時，可以使用 **Distinct**
```sql
SELECT DISTINCT column1, column2, ... FROM table_name;
```
<br>

當想計算『滿足條件的資料有幾筆』時，可以使用 **Count**

```sql
SELECT COUNT(DISTINCT column1, column2, ...) FROM Customers;
```

## Where
The **WHERE** clause is used to filter records.<br>
**Select + 要選擇的欄位 + From + 表格的名稱 Where 篩選的條件**<br>
例如執行下列語句:

```sql
SELECT * FROM Customers WHERE CustomerName='Alfreds Futterkiste';;
```
| CustomerID | CustomerName | PostalCode    |
|------------|--------------|---------------|
| 1          | Alfreds Futterkiste	 | 12209 |

<br>

### Operators in The WHERE Clause

| Operator | Description    |
|----------|---------------|
| =	 | Equal |
| >	 | Greater than |
| <>	 | Less than |
| >=	 | Greater than or equal |
| <=	 | Less than or equal |
| <>	 | Not equal. Note: In some versions of SQL this operator may be written as != |
| BETWEEN	 | Between a certain range |
| LIKE	 | Search for a pattern |
| IN	 | 	To specify multiple possible values for a column |

refer: https://www.w3schools.com/sql/sql_where.asp
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

## Order
**ORDER BY** 可以排序撈出來的資料，而排序不限制為數字和字串<br>
```sql
SELECT column1, column2, ... FROM table_name ORDER BY column1, column2, ... ASC|DESC;
 ```

## Insert
**INSERT INTO** statement is used to insert new records in a table:<br>
**Insert into + 表格名稱 ( 欄位名稱 ) + Values( 資料值 )**<br>

- Specify both the column names and the values to be inserted
  ```sql
  INSERT INTO table_name (column1, column2, column3, ...) VALUES (value1, value2, value3, ...);
   ```

 - If you are adding values for all the columns of the table
 
   ```sql
   INSERT INTO table_name VALUES (value1, value2, value3, ...);
   ```

例如執行下列語句:
```sql
INSERT INTO Customers VALUES (Miller, 000000 );
```
| CustomerID | CustomerName | PostalCode    |
|------------|--------------|---------------|
| 1          | Alfreds Futterkiste	 | 12209 |
| 2	         | Ana Trujillo Emparedados y helados | 05021 |
| 3          | Antonio Moreno Taquería   | 05023 |
| 4          | Miller   | 000000 |


## NULL

It is not possible to test for NULL values with comparison operators, such as =, <, or <>. <br>
We will have to use the **IS NULL** and **IS NOT NULL** operators instead.

- IS NULL
  ```sql
  SELECT column_names FROM table_name WHERE column_name IS NULL;
  ```

- IS NOT NULL
  ```sql
  SELECT column_names FROM table_name WHERE column_name IS NOT NULL;
  ```

## Update
The **UPDATE** statement is used to modify the existing records in a table.<br>
結構如下:<br>
**Update + 表格名稱 + Set + 欄位名稱 = 值 + Where + 條件**
```sql
UPDATE table_name SET column1 = value1, column2 = value2, ... WHERE condition;
```
"Be careful when updating records. If you omit the **WHERE** clause, ALL records will be updated!"<br>

例如執行下列語句:

```sql
UPDATE Customers SET PostalCode = 999999 WHERE CustomerName='Miller';
```
| CustomerID | CustomerName | PostalCode    |
|------------|--------------|---------------|
| 1          | Alfreds Futterkiste	 | 12209 |
| 2	         | Ana Trujillo Emparedados y helados | 05021 |
| 3          | Antonio Moreno Taquería   | 05023 |
| 4          | Miller   | 999999 |

## Delete
The **DELETE** statement is used to delete existing records in a table.<br>
**Delete + From + 表格名 + Where + 條件** <br>

```sql
DELETE FROM table_name WHERE condition;
```

例如執行下列語句:

```sql
DELETE FROM Customers WHERE CustomerName='Miller';
```
| CustomerID | CustomerName | PostalCode    |
|------------|--------------|---------------|
| 1          | Alfreds Futterkiste	 | 12209 |
| 2	         | Ana Trujillo Emparedados y helados | 05021 |
| 3          | Antonio Moreno Taquería   | 05023 |

若要刪除整個表格，則執行:

```sql
DELETE FROM table_name;
```