# this file, it will be a flask instance that is running our server
# first to test it out we will create a route with hello world, so first import flask

from flask import Flask, render_template, request
from weather import get_current_weather
from waitress import serve
# below we define our app
app = Flask(__name__)

# now we define routes on the flask app, that we can access on the web

# before writing code for each route, we have to specify the route in app.route followed by code


@app.route('/')
@app.route('/index')
# now following these routes we define a function that will return something for the route
def index():
    # return "hello world!"
    return render_template('index.html')


@app.route('/weather')
def get_weather():
    city = request.args.get('city')
    # first scenario we will work on is empty string or blank spaces
    # the params sent in the url after user has entered the city name
    # so here is where we will be working, which is received/processed in this part of the code, with below statement
    if not bool(city.strip()):
        city = "Bengaluru"

    # the second scenario to handle is what if we pass a strange city name that does not exist
    weather_data = get_current_weather(city)

    if not weather_data['cod'] == 200:
        # return "City not found."
        # above we can use simple string statement
        # # but instead we will create another template!
        return render_template("city-not-found.html")

    return render_template(
        "weather.html",
        # then we pass to template data from json object
        # now the third scenario is the gibberish city name which does not exist and will return code 404 nto found
        # which means we will not receive the below structure of json data
        title=weather_data["name"],
        status=weather_data["weather"][0]["description"].capitalize(),
        temp=f"{weather_data['main']['temp']:.1f}",
        feels_like=f"{weather_data['main']['feels_like']:.1f}"
    )

    # but we are not ready to ru our file yet until we add below statement
if __name__ == "__main__":
    # adding below statement helps it run on or localhost
    serve(app, host="0.0.0.0", port=8000)

# then check on http://localhost:8000/, after running python server.py in gitbash
# then stop the srever with Ctrl + C and now we will work on removing the following warning
# WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
# then install this in gitbash pip install waitress
# after installing this new dependency we update the requirements file
