import mysql.connector as m
try:
    con=m.connect(host='localhost',user='root',passwd='')
    cur=con.cursor()
    print('Connection Established')  
    cur.execute('DROP DATABASE IF EXISTS DIPAYAN')
    cur.execute('CREATE DATABASE DIPAYAN')
    cur.execute('USE DIPAYAN')
    cur.execute("CREATE TABLE STUDENTS(ADM INT, NAME CHAR(50), CLASS INT, `ROLL.NO` INT, `FATHERS NAME` CHAR(50), `MOTHERS NAME` CHAR(50),`D.O.B.` DATE, ATTENDANCE INT)")
    cur.execute("CREATE TABLE HY(ADM INT, ENGLISH FLOAT, PHYSICS FLOAT, CHEMISTRY FLOAT, MATHS FLOAT, COMPUTER FLOAT, `P.ED/ FA / LIB.SCI` FLOAT)")
    cur.execute("CREATE TABLE WT1(ADM INT, ENGLISH FLOAT, PHYSICS FLOAT, CHEMISTRY FLOAT, MATHS FLOAT, COMPUTER FLOAT, `P.ED/ FA / LIB.SCI` FLOAT)")
    cur.execute("CREATE TABLE WT2(ADM INT, ENGLISH FLOAT, PHYSICS FLOAT, CHEMISTRY FLOAT, MATHS FLOAT, COMPUTER FLOAT, `P.ED/ FA / LIB.SCI` FLOAT)")
    cur.execute('''INSERT INTO students VALUES 
                (10235, "TIYASHA MISHRA", 12, 42, "HARIMOY MISHRA", "SUPRITI MISHRA", "2007-11-26", 192),
                (10542, "SOUGATA BANERJEE", 12, 39, "SUBRATA BANERJEE", "SUNANDA BANERJEE", "2007-06-13", 102), 
                (10635, "BIDITA DAS", 12, 13, "TARASHANKAR DAS", "RUMA DAS", "2007-12-06", 165), 
                (10652, "AYUSHI JHA", 12, 4, "SHANTANU JHA", "SHEELA JHA", "2007-12-24", 163), 
                (10687, "ANISHA BASU", 12, 8, "BIPLAB BASU", "DEBJANI BASU", "2007-06-07", 183), 
                (10707, "SARTHAK ROY", 12, 29, "SUBRATA ROY", "UMA ROY", "2007-07-16", 186), 
                (10709, "DIPAYAN MONDAL", 12, 17, "PRADIP MONDAL", "TRINAYANI MONDAL", "2007-03-23", 162), 
                (10892, "SWASTIKA MUKHERJEE", 12, 43, "ANINDYA MUKHERJEE", "REEMA MUKHERJEE", "2007-11-22", 143), 
                (10965, "RAHUL DEY", 12, 23, "HARIANANDA DEY", "PRANTIKA DEY", "2007-06-23", 167), 
                (10986, "ARYA BANERJEE", 12, 10, "SUDIP BANERJEE", "TANU BANERJEE", "2007-12-23", 152)''')
    cur.execute('''INSERT INTO hy VALUES 
                (10235, 91.5, 82.5, 85, 87.5, 75, 80), 
                (10542, 89.5, 90, 77.5, 92.5, 92.5, 98), 
                (10635, 86, 80, 75, 73.5, 80.5, 86), 
                (10652, 86, 72, 70.5, 75, 80.5, 76.5), 
                (10687, 90, 86.5, 81.5, 85, 91.5, 95), 
                (10707, 85, 89.5, 80.5, 93, 95, 97), 
                (10709, 91, 81, 67, 92, 92, 97), 
                (10892, 89, 85, 92, 86.5, 82.5, 98), 
                (10965, 86, 89.5, 86.5, 92.5, 90, 96), 
                (10986, 92.5, 90.5, 86, 87, 81.5, 86)''')
    cur.execute('''INSERT INTO wt1 VALUES
                (10235, 21, 22.5, 20.5, 23, 21, 20), 
                (10542, 20.5, 21, 19.5, 20.5, 22, 21), 
                (10635, 18, 21.5, 15.5, 18.5, 20, 23), 
                (10652, 12, 13, 12.5, 15.5, 10, 17), 
                (10687, 21, 19, 18, 18.5, 22, 23), 
                (10707, 12, 19.5, 18, 21.5, 22, 25), 
                (10709, 18, 22, 18.5, 23, 24, 18), 
                (10892, 21, 19, 15, 20, 22, 21), 
                (10965, 21, 19.5, 18.5, 20.5, 22, 21), 
                (10986, 22, 19, 18.5, 21, 22, 23)''')
    cur.execute('''INSERT INTO wt2 VALUES 
                (10235, 22, 19.5, 23, 21.5, 19, 22.5), 
                (10542, 19, 21, 16.5, 20.5, 19, 20.5), 
                (10635, 20, 16.5, 17.5, 19, 21, 21), 
                (10652, 18, 15.5, 12, 14, 14, 16), 
                (10687, 22, 19, 19.5, 21, 22.5, 20), 
                (10707, 18, 15.5, 16, 20, 16.5, 23), 
                (10709, 21, 19, 18, 20.5, 21, 22), 
                (10892, 21.5, 20.5, 17.5, 22, 21, 23), 
                (10965, 21, 21.5, 19.5, 20.5, 20, 21), 
                (10986, 22, 19, 20.5, 23, 24, 22)''')
    con.commit()
    print('Sample Database created')

except m.errors.InterfaceError:
    print("Connection to MySQL was unsuccessful")