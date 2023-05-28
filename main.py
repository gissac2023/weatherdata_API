from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    temperate = 23
    return {"station": station,
            "date": date,
            "temperate": str(temperate)}


# run script only if main.py is called
if __name__ == "__main__":
    app.run(debug=True)
