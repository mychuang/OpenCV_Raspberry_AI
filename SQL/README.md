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

當想取某個欄位的『不重複資料』時，可以使用**Count**
```sql
SELECT DISTINCT column1, column2, ... FROM table_name;
```
<br>
當想計算『滿足條件的資料有幾筆』時，可以使用**Distinct**

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

## chapter