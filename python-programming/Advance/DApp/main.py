from flask import Flask,render_template,redirect,url_for,session
from flask_wtf import FlaskForm
from wtforms import (StringField,TextAreaField,SubmitField,RadioField,SelectField) 
from wtforms.validators import DataRequired

app=Flask(__name__)
app.config['SECRET_KEY']="Mybcasciuasuc"

class myform(FlaskForm):
    name=StringField("Type your name:",validators=[DataRequired()])
    gender=RadioField('Gender:',choices=[('M','Male'),('F','Female'),('O','Other')])
    address=SelectField("Select your city:",choices=[('goa','Goa'),('mumbai','Mumbai'),('bengluru','Bengluru'),('varanasi','Varanasi')])
    feedback=TextAreaField("Please provide feed back")
    submit=SubmitField("Submit")

@app.route('/',methods=['GET','POST'])
def  home():
    form=myform()
    if form.validate_on_submit():
        session['name']=form.name.data
        session['gender']=form.gender.data
        session['address']=form.address.data
        session['feedback']=form.feedback.data
        return redirect(url_for('response')) 
    return render_template("home.html",form=form)

@app.route("/response")
def response():
    return render_template('response.html')

if __name__=='__main__':
    app.run(debug=True)
    