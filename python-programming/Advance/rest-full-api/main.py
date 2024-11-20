from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/api/v1/<state>/<date>/")
def api(state,date):
    temrature=89
    return {"state":state,"date":date,"temprature":temrature }
if __name__=="__main__":
    app.run(debug=True)
