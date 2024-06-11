# web-scraper


Description-

This project scrapes laptop product data from Flipkart and stores it in a PostgreSQL 
database. The script collects details like product titles, prices, ratings, reviews, and 
links. Additionally, the scraped data is saved into a CSV file for easy access.

Features
    Web Scraping: Fetches data from multiple pages of Flipkart search results for laptops.
    Data Storage: Saves the scraped data into a PostgreSQL database.
    CSV Export: Exports the collected data into a CSV file for further analysis and for easy access.

Requirements
    - Python
    - Libraries:
        requests,
        BeautifulSoup (from bs4),
        pandas,
        psycopg2,
    - PostgreSQL

Usage
    
    1. This script will:
        Scrape data from the first three pages of Flipkart search results for laptops.
        Store the data in the laptops_data table within the products database.
        Export the data to a CSV file named products.csv.
    
    2. Check the output:
        The script prints the scraped data to the console.
        The CSV file products.csv is generated in the same directory as the script.

Database Setup
    Connects to the PostgreSQL database using the credentials provided.
    Creates a table laptops_data if it does not exist:
    
    CREATE TABLE IF NOT EXISTS laptops_data (    
        id SERIAL PRIMARY KEY,
        titles TEXT,
        prices TEXT,
        ratings TEXT,
        reviews TEXT,
        link TEXT
    );

Example Output:-

    id   Product Title   Price   Rating Reviews                                Link

    0  Laptop 1 Title   ₹45,999   4.5    100        https://www.flipkart.com/product-link-1
    1  Laptop 2 Title   ₹55,999   4.3     50        https://www.flipkart.com/product-link-2

Notes
    - Make sure you have a stable internet connection when running the script to ensure data scraping works correctly.

    - The script assumes Flipkart's HTML structure remains consistent. If the structure changes, the scraping logic might need adjustments.