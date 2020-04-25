from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from  wtforms.validators import DataRequired
app=Flask(__name__)
app.config['SECRET_KEY']='ThisIsSecret'
class loginForm(FlaskForm):
    username=StringField('username', validators=[DataRequired()])
    password=PasswordField('password')

@app.route('/wtforms',methods=['GET','POST'])
def wtforms():
    form=loginForm()
    if form.validate_on_submit():
        return f'<h1>{form.username.data} Submitted succesfully'
    return render_template("wtform.html",form=form)

if __name__==('__main__'):
    app.run(debug=True)









