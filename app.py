# Dependencies and Setup
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# Using flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

# Creating the application routes to bind URLs to the functions
@app.route("/")
def index():
    mars_values = mongo.db.mars_values.find_one()
    return render_template("index.html", mars_data=mars_values)

@app.route("/scrape")
def scrape():
    mars_values = mongo.db.mars_values
    mars_data = scrape_mars.scrape()
    mars_values.update({}, mars_data, upsert=True)
    return redirect("/", code=302)
    
if __name__ == "__main__":
    app.run(debug=True)