#!/usr/bin/python


from sqlite3 import connect

# Replace username with your own A2 Hosting account username:
conn = connect('personal.db')
cur = conn.cursor()
#name varchar(32), lastname varchar(32), nationality varchar(32), age varchar(3), address varchar(32) , school varchar(32)
##curs.execute("CREATE TABLE personal (name varchar(32), lastname varchar(32), nationality varchar(32), age varchar(3), address varchar(32) , school varchar(32));")


name = "Johns "
lastname = "Rodriguez"
nationality = "American"
age = "12"
address = "asdasd"
school = "fau"

#data=f"""{name}, {lastname}, {nationality}, {age}, {address}, {school}"""

#data=name+","+ lastname+","+ nationality+","+ age+","+ address+","+ school


# Insert Data
data_insert_query = '''INSERT INTO personal (name, lastname, nationality, 
age, address,school) VALUES 
(?, ?, ?, ?, ?, ?)'''
data_insert_tuple = (name, lastname, nationality,age,address,school)

cur.execute(data_insert_query, data_insert_tuple)
conn.commit()
conn.close()
