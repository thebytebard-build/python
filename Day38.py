#in this we have learnt how to hanlde sql quaries through python programming in oracle database

import oracledb
"""
#create a databse connection and make a table
try:
    con=oracledb.connect(user='system',password='romndrom',dsn='localhost:1521/XEPDB1')
    crsr=con.cursor()
    crsr.execute('create table employees (eno number , ename varchar2(12),esal number(10,2),eaddr varchar2(12))')
    print('table has created successfully')
except oracledb.DatabaseError as msg:
    print('the problem is :',msg)
finally:
    if crsr is not None:
        crsr.close()
    if con is not None:
        con.close()

#drop the table
try:
    con=oracledb.connect(user='system',password='romndrom',dsn='localhost:1521/XEPDB1')
    crsr=con.cursor()
    crsr.execute('drop table employees')
    print('table has dropped')
except oracledb.DatabaseError as msg:
    print('the problem is :',msg)
finally:
    if crsr is not None:
        crsr.close()
    if con is not None:
        con.close()

#do it with parametrize args nad with multiple row
con=oracledb.connect(user='system',password='romndrom',dsn='localhost:1521/XEPDB1')
crsr=con.cursor()
query='insert into employees values(:eno,:ename,:esal,:eaddr)'
records=[
    (1,'roshan',100.3,'mp'),
    (2,'raghav',4000.2,'america'),
    (3,'aditi',100.6,'usa'),
    (4,'roshani',0.0,)]

crsr.executemany(query,records)
con.commit()
crsr.close()
con.close()

#dynamically insert row in table employee
con=oracledb.connect(user='system',password='romndrom',dsn='localhost:1521/XEPDB1')
crsr=con.cursor()
while True :
    eno=int(input('enter the employee number'))
    ename=input('enter the employee name')
    esal=float(input('enter the employee sal'))
    eaddr=input('enter the addresss')
    query=f"insert into employees values({eno},'{ename}',{esal},'{eaddr}')"
    crsr.execute(query)
    print('data inserted successfully')
    option=input('do you want to insert one more data [yes/no]')
    if option.lower()=='no':
        con.commit()
        break
crsr.close()
con.close()

#dynamically insert row in table employee
con=oracledb.connect(user='system',password='romndrom',dsn='localhost:1521/XEPDB1')
crsr=con.cursor()
while True :
    eno=int(input('enter the employee number'))
    ename=input('enter the employee name')
    esal=float(input('enter the employee sal'))
    eaddr=input('enter the addresss')
    query=f"insert into employees values({eno},'{ename}',{esal},'{eaddr}')"
    crsr.execute(query)
    print('data inserted successfully')
    option=input('do you want to insert one more data [yes/no]')
    if option.lower()=='no':
        con.commit()
        break
crsr.close()
con.close()

#update esal if the salary is less than a given range
con=oracledb.connect(user='system',password='romndrom',dsn='localhost:1521/XEPDB1')
crsr=con.cursor()
increment=eval(input('enter the increment amount : '))
rang=eval(input('enter the salary range to which increment is applicable : '))
query=f"update employees set esal=esal+{increment} where esal <={rang}"
crsr.execute(query)
con.commit()
crsr.close()
con.close()

#delte esal if the salary is less than a given range
con=oracledb.connect(user='system',password='romndrom',dsn='localhost:1521/XEPDB1')
crsr=con.cursor()
rang=eval(input('enter the salary amount : '))
query=f"delete from employees  where esal <={rang}"
crsr.execute(query)
con.commit()
crsr.close()
con.close()

#use fetchone to fecth all data
con=oracledb.connect(user='system',password='romndrom',dsn='localhost:1521/XEPDB1')
crsr=con.cursor()
crsr.execute('select *from employees')
data=crsr.fetchone()
while data is not None:
    print(data)
    data=crsr.fetchone()
con.commit()
crsr.close()
con.close()

#use fetchall to fecth all data
con=oracledb.connect(user='system',password='romndrom',dsn='localhost:1521/XEPDB1')
crsr=con.cursor()
crsr.execute('select *from employees')
data=crsr.fetchall()
for row in data:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print()
con.commit()
crsr.close()
con.close()
"""
#use fetchmany to fecth all data
con=oracledb.connect(user='system',password='romndrom',dsn='localhost:1521/XEPDB1')
crsr=con.cursor()
crsr.execute('select *from employees')
data=crsr.fetchmany(2)
for row in data:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print()
con.commit()
crsr.close()
con.close()

