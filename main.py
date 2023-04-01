from flask import Flask, render_template
import pandas as pd

the_app = Flask("MyWeatherAPI")

station_data = pd.read_csv('data_small\\stations.txt', skiprows=17)
del station_data['CN']
del station_data['      LAT']
del station_data['       LON']
del station_data['HGHT']

@the_app.route("/")
def home():
    return render_template("home.html", data=station_data.to_html())

@the_app.route("/myweatherapi/v1/<enter_station_no_here>/<enter_date_here>")
def about(enter_station_no_here, enter_date_here):
    station_data_and_stuff = "data_small/TG_STAID" + str(enter_station_no_here).zfill(6) + ".txt"
    data = pd.read_csv(station_data_and_stuff, skiprows=20, parse_dates=['    DATE'])
    user_station = enter_station_no_here
    user_date = enter_date_here
    user_temperature = data.loc[data['    DATE'] == enter_date_here]['   TG'].squeeze() / 10
    ut_fahrenheit = user_temperature * (9/5) + 32
    return {"Your Station No:":user_station, "Date:":user_date, "Temperature:":user_temperature,
            "Temperature in Fahrenheit":ut_fahrenheit}

if __name__ == "__main__":
    the_app.run(debug=True)      
