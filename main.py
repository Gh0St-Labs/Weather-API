from flask import Flask, render_template

the_app = Flask("MyWeatherAPI")

@the_app.route("/")
def home():
    return render_template("home.html")

@the_app.route("/myweatherapi/v1/<enter_station_no_here>/<enter_date_here>")
def about(enter_station_no_here, enter_date_here):
    return render_template("about.html")

if __name__ == "__main__":
    the_app.run(debug=True)