# Create a Python Virtual Environment: python3 -m venv venv
# Activate the Python Virtual Environment: source venv/bin/activate
# Install Scrapy using pip: pip install scrapy
# Listing the scrapy projects scrapy list
# Running the scrapy project: scrapy crawl bookspider

# pip install -r requirements.txt

# scrapy startproject bookscraper

## /spiders
# scrapy genspider bookspider books.toscrape.com

# scrapy crawl bookspider -o bookdata.csv