from flask import Flask,render_template

app=Flask("Website")
@app.route("/")
def Home():
    return render_template("Home.html")
@app.route("/about/")
def about():
    return render_template("about.html")
@app.route("/contact/")
def contact():
    return render_template("contact.html")
@app.route("/services/")
def services():
    return render_template("services.html")
app.run(debug=True)

