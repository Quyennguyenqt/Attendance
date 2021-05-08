import mysql.connector
import csv
import datetime
import time
conn = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="Recognition")
c = conn.cursor()

#============================Register============================
def create_data_register():
        c.execute(
            "create table if not exists Student(id integer primary key auto_increment,enrollment varchar(25) not null,fullname text not null,date varchar(20) not null, datetime varchar(50) not null);")

def insert_data_register(id, fullname, date, datetime):
    sql = "insert into Student (enrollment,fullname, date, datetime) values(%s,%s,%s,%s);"
    val = (id, fullname, date, datetime)
    c.execute(sql, val)
    conn.commit()

def get_list_register():
    sql = "Select * from Student;"
    c.execute(sql)
    row = c.fetchall()
    print(row)

#============================Attendance============================
def create_data_attendance(date):
    sql = "create table if not exists attendance" + str(date) + "(id integer primary key auto_increment,enrollment varchar(25) not null,fullname text not null,date varchar(20) not null, datetime varchar(50) not null);"
    c.execute(sql)

def insert_data_attendance(id,fullname,date,timestamp,datetable):
    sql = "insert into attendance"+ str(datetable) + " (enrollment,fullname,date,datetime) values(%s,%s,%s,%s);"
    val = (id, fullname, date, timestamp)
    c.execute(sql, val)
    conn.commit()

def check_absence():
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d_%m_%Y')
    sql1 = "Select enrollment,fullname from Student"
    c.execute(sql1)
    row1 = c.fetchall()

    sql2 = "Select enrollment,fullname from attendance_"+date
    c.execute(sql2)
    row2 = c.fetchall()
    ts = time.time()
    date1 = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    for r1 in row1:
        if row2.count(r1) == 0:
            absent = [str(r1[0]), '', str(r1[1])]
            with open("Attendance\Attendance_" + date1 + ".csv", 'a+') as csvFile1:
                writer = csv.writer(csvFile1)
                writer.writerow(absent)
            csvFile1.close()

def fillAttendanceCreatedFile():
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d_%m_%Y')
    sql3 = "Select * from attendance_" + date
    c.execute(sql3)
    row3 = c.fetchall()
    date1 = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    with open("Attendance\Attendance_" + date1 + ".csv", 'a+') as csvFile1:
        for r3 in row3:
            attendance = [str(r3[1]),'', str(r3[2]),'',str(r3[3]),'',str(r3[4])]
            writer = csv.writer(csvFile1)
            writer.writerow(attendance)
    csvFile1.close()

def fillAttendanceNotCreatedFile():
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%d_%m_%Y')
    sql3 = "Select * from attendance_" + date
    c.execute(sql3)
    row3 = c.fetchall()
    date1 = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y')
    with open("Attendance\Attendance_" + date1 + ".csv", 'a+') as csvFile1:
        for r3 in row3:
            attendance = [str(r3[1]),'', str(r3[2]),'',str(r3[3]),'',str(r3[4])]
            writer = csv.writer(csvFile1)
            writer.writerow(attendance)
    csvFile1.close()

def exist_name(ID,bb,date,timeStamp,datetable):
        sql = "Select enrollment from attendance"+str(datetable)+" where enrollment = "+ID+";"
        c.execute(sql)
        row = c.fetchall()
        if len(row) == 0:
            insert_data_attendance(ID, bb, date, timeStamp, datetable)
        return False
