from flask import Flask,render_template,request
import sqlalchemy
from sqlalchemy import create_engine
import datetimes

app=Flask(__name__)


app.debug=True
@app.route("/test")
def helo():
    name=request.form.get("name")

    return render_template("index.html",name=name)
@app.route("/form")
def form():
    return render_template("form.html")

# @app.route("/<string:name>",methods=['Post','get'])
# def cool(name):
#     return render_template("index.html",name=name)
all_posts=[
    {
        "title":"Posts 1",
        "author":"mukul",
        "content":"content  of 1 "
    },
    {
        "title":"Post 2",

        "content":"content of 2"
    }
]
@app.route("/posts")
def myPosts():
    return render_template("posts.html",posts=all_posts)
@app.route("/time")
def check():
    now=datetime.datetime.now()
    check=now.month==1 and now.date()==1
    return render_template("check.html",check=check)
notes=[]
@app.route("/notes",methods=['POST','GET'])
def note():
    if request.method=="POST":
        notet=request.form.get("note")
        notes.append(notet)
        return render_template("notes.html", note=notes)
    else:
        return render_template("notes.html", note=notes)






if __name__=="__main__":
    app.run()
