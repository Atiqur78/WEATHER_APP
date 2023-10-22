from flask import Flask, render_template, request
import requests

app=Flask(__name__)

@app.route("/")
def show_homepage():
    return render_template("index.html")

@app.route("/weather", methods=["POST"])
def weather():
    city= request.form.get("city")
    appkey=request.form.get("appid")
    units =request.form.get("units")
    url="https://api.openweathermap.org/data/2.5/weather"
    param ={
        'q':city,
        'appid':appkey,
        'units':units
    }
    response = requests.get(url, params= param)
    data= response.json()
    return f"data :{data}"

if __name__=='__main__':
    app.run(host="0.0.0.0")