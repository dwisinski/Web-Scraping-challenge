# Web-Scraping-challenge

by: Dave Wisinski

May 2021

## Description:
This project was created to demonstrate a number of web scraping and web application-building concepts by utilizing a variety of web sources which were scraped for data using a Jupyter Notebook, the Beautiful Soup HTML parsing package and the Splinter web application testing tool. Data was saved in variables and DataFrames, and repurposed using a Flask application connected to a MongoDB database (via PyMongo). The final output is a responsive webpage formatted with HTML, CSS and Bootstrap framework components.

## Notes:
**Please allow time for the scrape to complete (total time required will vary depending on internet connection).** 

This repo contains the following files:

- A Jupyter Notebook file containing the original scraping methods, variables and output previews.
- A `scrape_mars.py` Python script containing the aforementioned methods converted into a scrape function.
- An `app.py` Python script containing the flask application launcher and relevant routes for both an index page and a redirection to a post-scrape index page with relevant populated data.
- An index HTML template located in the templates folder. 
- A CSS stylesheet located in the static folder.
- Screenshot image files of the functioning index page pre and post-scrape located in the static folder.