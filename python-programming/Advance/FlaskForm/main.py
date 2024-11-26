from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "MYSCRATEKAY"  # Secret key for CSRF protection

# Define the form
class MyForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    submit = SubmitField('Submit')

# Define the route
@app.route("/", methods=['POST', 'GET'])
def home():
    first_name = None
    last_name = None
    form = MyForm()

    if form.validate_on_submit():
        # Extract and clear form data
        first_name = form.first_name.data
        last_name = form.last_name.data
        form.first_name.data = ''
        form.last_name.data = ''

    return render_template("home.html", form=form, first_name=first_name, last_name=last_name)

if __name__ == '__main__':
    app.run(debug=True)
