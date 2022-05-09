# Data Base Design Note
Refer: http://www.tsnien.idv.tw/DataBase_WebBook/%E7%AC%AC%E4%B9%9D%E7%AB%A0%20%E8%B3%87%E6%96%99%E5%BA%AB%E7%9A%84%E9%82%8F%E8%BC%AF%E8%A8%AD%E8%A8%88.html

## 資料庫設計流程
目前大多採用關聯式資料庫系統，資料庫的邏輯設計方法如下圖:<br>
<img src="./sql01.png" width="300px" />
<br>

### 系統規格與需求定義
- **針對客戶需求，確定設計範圍**：瞭解客戶的工作流程、各部門職掌範圍、資料處理方式，以確定資料庫設計的範圍及應具備的功能。
- **收集與分析資料**：除了要明確而具體的找出客戶的需求外，還要收集他們平時使用的各類表單、報表...等等，這些都是規劃資料庫的重要參考資料。
<br>

### 概念設計
分析及整理收集到的資料，產生一個能符合使用者需求的資料庫模型。一般都用 **E-R** 模式 (實體-關係模式)的圖形來製作。通常將此階段再細分為兩個階段:<p>
- 第一個階段: 建立分區的概念設計
- 第二個階段: 將各分區設計整合成全區的概念設計
<br>

### 邏輯設計
此階段是將 E-R 圖形的設計概念，轉換為實際的資料表，並符合資料表的正規化。
<br>

### 實體建置
選定所要使用的資料庫，譬如：Access、SQL Server、MySQL、、等等，再將上述所設計的資料表建立起來即完成。
<br>

## E-R Model
『實體關係模型』(Entity-Relation (E-R) Model)是將現場實境以圖形化顯現出來的工具。標準化的 E-R 圖符號如下：
<img src="./sql03.png" width="500px" />

個體之間需建立關係才可以由一個個體找到另一個個體，如果有一個個體它無法和其它個體建立關係，則他就沒有存在的價值。**E-R** 模式範例如下<p>

<img src="./sql02.png" width="500px" />

Refer: http://cc.cust.edu.tw/~ccchen/doc/db_03.pdf

### 多對一關係
下圖表示學生個體與班級個體之間的關係，表示學生是屬於哪一個班級的，因此，它們之間是屬於『隸屬』關係。Keys 分別為學號與班級代碼。班級代碼為共用Key

<img src="./sql04.png" width="500px" />

<br>

### 多對多關係
下圖表示學生同時可以修讀多門課，每一門課也可以讓多位學生選讀。另外，關係也可以附加屬性，譬如選課關係增加『分數』的屬性，其用來記錄學生修讀的分數。

<img src="./sql05.png" width="500px" />

<br>

### 一對一關係
下圖顯示1對1的關係: 假設每一位學生只有一位監護人，每一位監護人也僅隸屬一位學生。

<img src="./sql06.png" width="500px" />

<br>

##  邏輯設計: E-R 圖轉換為資料表
延續上圖的範例，以SQL語法，依序說明如下:
### 多對一關係
如果關係沒有增加屬性的話，只要分別建立學生資料表與班級資料表即可

```sql
-- 建立學生資料表
create table Student(
     s_id VARCHAR(20),
     s_name VARCHAR(20) NOT NULL DEFAULT '',
     s_sex VARCHAR(10) NOT NULL DEFAULT '',
     s_phone VARCHAR(10) NOT NULL DEFAULT '',
     class_id VARCHAR(10) NOT NULL DEFAULT '',
     PRIMARY KEY(s_id)
);

-- 建立班級資料表
create table Class(
     class_id VARCHAR(20),
     class_name VARCHAR(10) NOT NULL DEFAULT '',
     class_year VARCHAR(10) NOT NULL DEFAULT '',
     PRIMARY KEY(class_id)
);
```
<br>

### 多對多關係
設定每位學生可以選讀多門課，每一門課可讓學生修讀，但同一位學生、同一門課僅能選讀一次。因此，設定選課的資料表為『選課總表』，其屬性為 {學號、開課代碼、分數}，其中學號與開課代碼為複合主鍵。
```sql
create table Course(
     s_id VARCHAR(20),
     c_id VARCHAR(20),
     score VARCHAR(10) NOT NULL DEFAULT '',
     PRIMARY KEY(c_id), UNIQUE (s_Id)
);
```
<br>

### 一對一關係
兩個實體之間是一對一的關係，大多兩實體都使用相同屬性為主鍵，譬如學生與監護人之間是一對一的關係，兩者都採用『學號』當主鍵，其關係就不需要另外建立資料表。
```sql
create table Parent(
     s_id VARCHAR(20),
     p_name VARCHAR(20) NOT NULL DEFAULT '',
     p_phone VARCHAR(10) NOT NULL DEFAULT '',
     PRIMARY KEY(s_id)
)
```
<br>

##  邏輯設計: 正規化
正規化之目的是要檢測資料表是否符合減少重複性與避免資料更新的異常<p>
- 1NF-第一正規化: 在一個資料表內，所屬欄位的內容都是單元值(Atomic Value)，則稱該資料表滿足 1NF。每個欄位的內容都是最小單元，不可以再分割的。如需要再分割，則需另外再設計資料表的欄位。
- 2NF-第二正規化: 一個資料表，除了符合第一正規化特性外，所有主鍵以外的欄位都必須與主鍵功能相依，則稱該資料表滿足 2NF。所有欄位都必須與主鍵之間功能性相依。
-  3NF-第三正規化: 一個資料表，除了符合第二正規化特性外，所有主鍵以外的欄位都僅能與主鍵功能相依，且沒有與其它欄位相依，則稱該資料表滿足 3NF。所有欄位都必須、且僅能與主鍵之間功能性相依，其它欄位之間不可以有相依的特性存在。