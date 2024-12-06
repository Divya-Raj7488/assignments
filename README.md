# Web Scraping with Flask and MongoDB
## This project demonstrates a web scraping solution using Flask for the web interface, MongoDB for data storage, and BeautifulSoup and Selenium for scraping.

### Features
#### Web Scraping: Scrapes data (title, description, subject, word count, etc.) from a website.
#### Data Validation: Scrapes data is validated against a predefined schema.
#### REST API: Fetch all scraped data from MongoDB via a simple API.
#### Flask Interface: A minimal web interface to interact with the app.

### Installation
### With Docker (Recommended)
##### Clone the repo: git clone https://github.com/Divya-Raj7488/assignments.git
##### cd your-repository
##### Build and run the container: docker build -t web-scraping-flask-app .
##### docker run -p 5000:5000 --env-file .env web-scraping-flask-app
### Without Docker
##### Clone the repo: git clone https://github.com/Divya-Raj7488/assignments.git
##### cd your-repository
##### Create and activate a virtual environment: python -m venv venv
##### .\venv\Scripts\activate  # Windows
##### source venv/bin/activate # macOS/Linux
##### Install dependencies: pip install -r requirements.txt
##### Run the Flask app: flask run
### API Endpoint
##### GET- api/data: Retrieves all scraped data from MongoDB in JSON format.
### Files
#### scraper/scraper.py: Contains the scraping logic.
#### scraper/schema_validator.py: Defines data validation schema.
#### scraper/mongodb_handler.py: MongoDB connection and upsert logic.
#### main.py: Flask app entry point.
#### api.py - REST-api logic
#### templates - index.html - homepage template
### Dependencies
##### Flask
##### pymongo
##### BeautifulSoup
##### Selenium
##### lxml
##### jsonschema
##### python-dotenv
### Install using: pip install -r requirements.txt
