from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v1/<station>/<date>")
def about(station, date):
    # read the file from pandas
    filename = "data_small/TG_STAID" + str(station).zfill(6) + ".txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])

    temperature = df.loc[df["    DATE"] == date]["   TG"].squeeze() / 10

    return {"station": station,
            "date": date,
            "temperate": str(temperature)}


# run script only if main.py is called
if __name__ == "__main__":
    app.run(debug=True, port=5000)
