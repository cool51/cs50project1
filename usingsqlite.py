from flask import Flask,render_template,request
from sqlalchemy import create_engine
db = create_engine('sqlite:///newemployees.sqlite')
# echo output to console
db.echo = True
conn = db.connect()
conn.execute("""
CREATE TABLE newemployee12 (id INTEGER PRIMARY KEY,name STRING(100) NOT NULL,birthday DATE NOT NULL)""")
conn.execute("INSERT INTO employee VALUES (NULL, 'marcos mango',('1990-09-06'));")
conn.execute("INSERT INTO employee VALUES (NULL, 'rosie rinn',('1980-09-06') );")
conn.execute("INSERT INTO employee VALUES (NULL, 'mannie moon',('1970-07-06') );")
for row in conn.execute("SELECT * FROM employee"):
    print (row)

# give connection back to the connection pool
conn.close()