# Dependencies and Setup
from bs4 import BeautifulSoup
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd
import time

def init_browser():
    # Setting up ChromeDriver
    executable_path = {"executable_path": ChromeDriverManager().install()}
 
    # Running "headless" mode; change to False for browser GUI display
    return Browser("chrome", **executable_path, headless=True)

def scrape():
    # Initializing browser
    browser = init_browser()

    ### NASA Mars News

    # URL of page to be scraped
    url = "https://mars.nasa.gov/news/"

    # Retrieving page with the requests module
    response = requests.get(url)

    # Creating BeautifulSoup object; parse with "html.parser"
    soup = BeautifulSoup(response.text, "html.parser")

    # Storing results
    results = soup.find("div", class_="slide")

    # Retrieving news URL
    news_partial_url = results.find("div", class_="content_title").a["href"].replace("/news","")
    news_url = url + news_partial_url

    # Storing title
    news_title = results.find("div", class_="content_title").text.strip()

    #Storing paragraph text
    news_p = results.find("div", class_="rollover_description_inner").text.strip()

    ### JPL Mars Space Images - Featured Image

    # URL of page to be scraped
    url2 = "https://www.jpl.nasa.gov/images?search=&category=Mars"

    # Accessing page using Splinter
    browser.visit(url2)

    # Navigating the page to find the title and image URL for the current "Featured Mars Image", storing both
    browser.links.find_by_partial_href("images").click()
    time.sleep(2)
    featured_image_title = browser.find_by_css("h1").text
    browser.links.find_by_partial_href("original_images").click()
    featured_image_url = browser.url

    ### Mars Facts

    # URL of page to be scraped
    url3 = "https://space-facts.com/mars/"

    # Scraping the facts table using pandas
    tables = pd.read_html(url3)

    # Converting table to formatted DataFrame
    df = tables[0].rename(columns={0: "Description", 1: "Mars"}).set_index("Description")

    # Converting the DataFrame back to an HTML table
    html_table = df.to_html()

    ### Mars Hemispheres

    # URL of page to be scraped
    url4 = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

    # Accessing page using Splinter
    browser.visit(url4)

    # Creating HTML object
    html = browser.html

    # Creating BeautifulSoup object; parse with "html.parser"
    soup = BeautifulSoup(html, "html.parser")

    # Scraping the page for the div items for each hempisphere
    items = soup.find_all("div", class_="item")

    # Creating an empty list for storing subsequent results
    hemisphere_image_urls = []

    # Looping through items for the relevant data
    for item in range(len(items)):

        # Navigating the page to find the links to the standalone page for each hemisphere
        link = browser.find_by_css("h3")
        link[item].click()

        # Locating and storing the formatted hemisphere name
        img = browser.find_by_css("h2").text
        title = img.replace(" Enhanced","")
        
        # Locating and storing the URL for the full-size image
        img_url = browser.links.find_by_partial_href("tif/full")["href"]
        
        # Creating dictionary with title/URL pairs and appending to list
        hemisphere_image_urls.append({"title": title, "img_url": img_url})
        
        # Navigating back one page before restarting loop
        browser.back()
        
    # Quitting browser session  
    browser.quit()

    mars_values = {
        "news_url": news_url,
        "news_title": news_title,
        "news_p": news_p,
        "featured_image_title": featured_image_title,
        "featured_image_url": featured_image_url,
        "mars_table": html_table, 
        "hemisphere_images": hemisphere_image_urls
    }

    return mars_values