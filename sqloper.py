# Steps to write data to mysql database using python and its module
# Step 1: Import module
import pymysql as p

# Step 2: Connect to DB
mydb = p.connect(host = 'localhost', user = 'root', password = 'Hello12345!', db = 'nalanadhitdb' )
print("Connected to NalanAdhitDB successfully")

# Step 3: Create cursor
mycursor = mydb.cursor()

# Step 4: Create/Prepare the query
# Write query
q1 = [
    "INSERT INTO persons (PersonID, LastName, FirstName, Address, City) VALUES (1, 'S.P', 'Nalan Adhit', 'Flat#A104, Chandapura', 'Bangalore');",
    "INSERT INTO persons (PersonID, LastName, FirstName, Address, City) VALUES (2, 'P', 'Sulochana', 'Flat#A104, Chandapura', 'Bangalore');",
    "INSERT INTO persons (PersonID, LastName, FirstName, Address, City) VALUES (3, 'D', 'Paramasivan', 'Flat#A104, Chandapura', 'Bangalore');",
    "INSERT INTO persons (PersonID, LastName, FirstName, Address, City) VALUES (4, 'D', 'Revathi', '1/93, Uthukuli', 'Tiruppur');",
    "INSERT INTO persons (PersonID, LastName, FirstName, Address, City) VALUES (5, 'S.R', 'Navaneeth', '1/94, Uthukuli', 'Tiruppur');",
    "INSERT INTO persons (PersonID, LastName, FirstName, Address, City) VALUES (6, 'S.R', 'Sri Dharshan', '1/95, Uthukuli', 'Tiruppur');"
]

# Steo 5: Execute the query

for query in q1:
    try:
        mycursor.execute(query)
        print("Executed successfully : ",query)
    except Exception as err:
        print("Ok to ignore it. Reason : ", err)

# Step 6: Commit the changes
mydb.commit()

# Step 7: Close DB connection
mydb.close()

# **************** Steps to read data or fetch data from database using python ****************

# Step 1: Import module
import pymysql as p

# Step 2: Connect to DB

mydb = p.connect(host='localhost', user='root', password='Hello12345!', db='nalanadhitdb')

# Step 3: Create cursor

mycursor = mydb.cursor()

# Step 4: Create search query
q1 = [
    "SELECT * FROM persons WHERE Address = '1/93, Uthukuli';",
    "SELECT count(*) FROM persons WHERE City = 'Bangalore'"
]

# Step 5: Execute the query
for query in q1:
    mycursor.execute(query)
    print("Query executed is : ",query)

# Step 6: Fetch all result
    res = mycursor.fetchall()
    print(res)

# Step 7: Close DB connection
mydb.close()

### ******************** Add below data in emp table ***************************************
# INSERT INTO emp VALUES ('7369','SMITH','CLERK','7902','1980-12-17','800.00',NULL,'20');,
# INSERT INTO emp VALUES ('7499','ALLEN','SALESMAN','7698','1981-02-20','1600.00','300.00','30');,
# INSERT INTO emp VALUES ('7521','WARD','SALESMAN','7698','1981-02-22','1250.00','500.00','30');,
# INSERT INTO emp VALUES ('7566','JONES','MANAGER','7839','1981-04-02','2975.00',NULL,'20');,
# INSERT INTO emp VALUES ('7654','MARTIN','SALESMAN','7698','1981-09-28','1250.00','1400.00','30');,
# INSERT INTO emp VALUES ('7698','BLAKE','MANAGER','7839','1981-05-01','2850.00',NULL,'30');,
# INSERT INTO emp VALUES ('7782','CLARK','MANAGER','7839','1981-06-09','2450.00',NULL,'10');,
# INSERT INTO emp VALUES ('7788','SCOTT','ANALYST','7566','1982-12-09','3000.00',NULL,'20');,
# INSERT INTO emp VALUES ('7839','KING','PRESIDENT',NULL,'1981-11-17','5000.00',NULL,'10');,
# INSERT INTO emp VALUES ('7844','TURNER','SALESMAN','7698','1981-09-08','1500.00','0.00','30');,
# INSERT INTO emp VALUES ('7876','ADAMS','CLERK','7788','1983-01-12','1100.00',NULL,'20');,
# INSERT INTO emp VALUES ('7900','JAMES','CLERK','7698','1981-12-03','950.00',NULL,'30');,
# INSERT INTO emp VALUES ('7902','FORD','ANALYST','7566','1981-12-03','3000.00',NULL,'20');,
# INSERT INTO emp VALUES ('7934','MILLER','CLERK','7782','1982-01-23','1300.00',NULL,'10');

# Connect to DB

mydb = p.connect(host='localhost', user='root', password='Hello12345!', db='nalanadhitdb')

# Create a cursor

mycursor = mydb.cursor()

# Create query
q2 = [
    "INSERT INTO emp VALUES ('7369','SMITH','CLERK','7902','1980-12-17','800.00',NULL,'20');",
    "INSERT INTO emp VALUES ('7499','ALLEN','SALESMAN','7698','1981-02-20','1600.00','300.00','30');",
    "INSERT INTO emp VALUES ('7521','WARD','SALESMAN','7698','1981-02-22','1250.00','500.00','30');",
    "INSERT INTO emp VALUES ('7566','JONES','MANAGER','7839','1981-04-02','2975.00',NULL,'20');",
    "INSERT INTO emp VALUES ('7654','MARTIN','SALESMAN','7698','1981-09-28','1250.00','1400.00','30');",
    "INSERT INTO emp VALUES ('7698','BLAKE','MANAGER','7839','1981-05-01','2850.00',NULL,'30');",
    "INSERT INTO emp VALUES ('7782','CLARK','MANAGER','7839','1981-06-09','2450.00',NULL,'10');",
    "INSERT INTO emp VALUES ('7788','SCOTT','ANALYST','7566','1982-12-09','3000.00',NULL,'20');",
    "INSERT INTO emp VALUES ('7839','KING','PRESIDENT',NULL,'1981-11-17','5000.00',NULL,'10');",
    "INSERT INTO emp VALUES ('7844','TURNER','SALESMAN','7698','1981-09-08','1500.00','0.00','30');",
    "INSERT INTO emp VALUES ('7876','ADAMS','CLERK','7788','1983-01-12','1100.00',NULL,'20');",
    "INSERT INTO emp VALUES ('7900','JAMES','CLERK','7698','1981-12-03','950.00',NULL,'30');",
    "INSERT INTO emp VALUES ('7902','FORD','ANALYST','7566','1981-12-03','3000.00',NULL,'20');",
    "INSERT INTO emp VALUES ('7934','MILLER','CLERK','7782','1982-01-23','1300.00',NULL,'10');"
]

# Execute query
for que in q2:
    try:
        mycursor.execute(que)
        print("Query executed successfully : ",que)
    except Exception as err:
        print("Ok to ignore it. Reason : ", err)

# Commit the changes

mydb.commit()

# Close the connect to DB
mydb.close()