from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Access form data
    name = request.form['name']
    email = request.form['email']
    with open("name.txt","a") as file:
        file.write(name+"\n")
    with open("email.txt","a") as file:
        file.write(email+"\n")    


    return f"Name: {name}, Email: {email}"

if __name__ == '__main__':
    app.run(debug=True)
