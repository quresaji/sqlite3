import sqlite3
Dbname = input("Please enter the database name:")
tablename=input("Please enter the table name:")
nor=input("How many students you want to store:")

# Now to change the datdtype of nor (nor str->nor int)
nor=int(nor)
print(type(nor))
database = Dbname+".sqlite3"

#Open the file in append mode

fo=open(database,"a")


# Now we have to connect this datdabase
con=sqlite3.connect(database)
cur=con.cursor() 

# Now create a table
cur.execute(f"CREATE TABLE {tablename}(Name text,Surname text,mobile text)")

for x in range(nor):
    n=input("Enter the Student Name:")
    s=input("Enter the Student Surname:")
    m=input("Enter the Contact number:")
    cur.execute (f"INSERT INTO {tablename} VALUES ('{n}','{s}','{m}')")
     # TO save the changes use commit
    con.commit()

    # to close the databse 