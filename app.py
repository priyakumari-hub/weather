from flask import Flask, render_template, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()

app= Flask(__name__)
WEATHER_API=os.getenv("WEATHER_API")

@app.route("/")  # Home page
def home():
    return render_template("weatherapp.html")  # Make sure this file exists in templates/

@app.route("/weather")  # Weather API endpoint
def get_weather():
    city = request.args.get("city")
    if not city:
        return jsonify({"error": "City name is required"}), 400

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API}&units=metric"
    response = requests.get(url)

    if response.status_code != 200:
        return jsonify({"error": "City not found"}), 404

    data = response.json()
    return jsonify({
        "city": city,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["description"]
    })

if __name__ == "__main__":
    app.run(debug=True)
