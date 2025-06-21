from flask import Flask,request,jsonify
import requests

app=Flask(__name__)
api_key="REDACTED_API_KEY_1"

app.route("/")
def index():
    return render_template("weather1.html")  

@app.route("/weather")
def get_weather():
    city=request.args.get("city")
    if not city:
        return jsonify({"error":"City name is required"}),400
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response=requests.get(url)
    if response.status_code!=200:
        return jsonify({"error":"City not found"}),404
    data=response.json()
    return jsonify({
        "city":city,
        "temperature":data["main"]["temp"],
        "condition":data["weather"][0]["description"]
        })


if __name__=="__main__":
    app.run(debug=True)




