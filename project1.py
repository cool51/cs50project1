from flask import Flask,render_template,request,session
from sqlalchemy import  create_engine
app=Flask(__name__)



db=create_engine('sqlite:///project1.db',connect_args={'check_same_thread': False})
db.echo=True
conn=db.connect()
app.debug=True
@app.route("/",methods=['POST','GET'])
def userLogin():
    return render_template("userlogin.html")

@app.route("/books",methods=['POST','GET'])
def books():
    tempemail = request.form.get("email")
    temppassword = request.form.get("password")

    data = conn.execute(
        "SELECT email,password FROM userData").fetchall()
    for checkdata in data:

        if (tempemail == checkdata.email and temppassword == checkdata.password):
            return render_template("searchbook.html")


    return ("Please login first ")






@app.route("/register",methods=['POST'])
def newAccount():
    conn.execute("""
    CREATE TABLE IF NOT EXISTS userData(id INTEGER PRIMARY KEY AUTOINCREMENT ,email STRING(100) NOT NULL ,password STRING(20))""")
    email=request.form.get("newemail")
    password=request.form.get("newpassword")
    trans=conn.begin()
    conn.execute("INSERT INTO userData(email,password) VALUES (:email,:password)",{"email":email,"password":password})
    trans.commit()

    return (email)








if __name__=="__main__":
    app.run()



