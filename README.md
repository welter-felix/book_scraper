# Book Scraping Project

This project contains a Scrapy spider that scrapes book details (title, price, availability) from [Books to Scrape](https://books.toscrape.com/) and stores the data in a MongoDB database.

## Features
- **Scrapes book data** such as title, price, and availability.
- **Navigates multiple pages** to collect data from the entire website.
- **Stores scraped data in MongoDB**, a NoSQL database.
- **Data cleaning and normalization** (e.g., trimming spaces, converting prices to float).

## How the Spider Works

The spider in `books_spider.py` follows these steps:

1. **Start URL**: It begins by visiting the homepage of [Books to Scrape](https://books.toscrape.com/).
2. **Pagination**: The spider automatically follows the pagination links to scrape all pages.
3. **Data Extraction**: On each page, it extracts the following details for every book:
   - **Title**: The title of the book.
   - **Price**: The price of the book (converted to a `float` type).
   - **Availability**: Whether the book is in stock (cleaned and normalized).
4. **MongoDB Storage**: The scraped data is passed through a pipeline where:
   - The data is cleaned (e.g., price is converted from string to float, and availability is normalized).
   - The data is inserted into a MongoDB collection.
   
## How to Run the Project

### 1. Clone the Repository
First, clone the repository to your local machine:

```bash
git clone https://github.com/your-username/book_scraper.git
cd book_scraper
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. MongoDB Setup

Make sure MongoDB is installed and running on your system. By default, the spider connects to MongoDB running locally on port 27017.

### 4. Run the spider
```bash
scrapy crawl books
```
- The spider will start scraping book details from Books to Scrape.
- The data will be automatically saved to your MongoDB database in the books_db database and books_collection collection.