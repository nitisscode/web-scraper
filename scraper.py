# important libraries for the function
import requests
from bs4 import BeautifulSoup
import pandas as pd
import psycopg2

# postgreSQL database connection
conn = psycopg2.connect(
    host="localhost",      
    database="products",  
    user="postgres",  
    password="@123Nitish" 
)

cursor = conn.cursor()

# Create table if not exists
create_table_query = """
CREATE TABLE IF NOT EXISTS laptops_data (
    id SERIAL PRIMARY KEY,
    titles TEXT,
    prices TEXT,
    ratings TEXT,
    reviews TEXT,
    link TEXT
);
"""
cursor.execute(create_table_query)
conn.commit()


# URL for scraping
url = "https://www.flipkart.com/search?q=laptops&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="

# Lists to store data
product_title = []
product_price = []
product_rating = []
product_review = []
product_url = []

#function for scrap data from flipkart
def get_products():
    global product_title, product_price, product_rating, product_rating, product_review, product_url, url

    # loop for different pages and requests
    for page in range(1, 2):                
        search_url = f"{url}{page}"
        req = requests.get(search_url)
        
        if req.status_code == 200:
            soup = BeautifulSoup(req.content, "html.parser")
            products = soup.find_all('a', class_='CGtC98')

            # nested loop for get data values like title, price, rating, review and link
            for container in products:
                title_tag = container.find('div', class_='KzDlHZ')
                title = title_tag.get_text() if title_tag else "something went wrong"

                price_tag = container.find('div', class_="Nx9bqj _4b5DiR")
                price = price_tag.get_text() if price_tag else "0"

                rating_tag = container.find('div', class_='XQDdHH')
                rating = rating_tag.get_text() if rating_tag else "0"

                review_tag = container.find("span", class_="Wphh3N")
                review = "0"
                if review_tag:
                    text = review_tag.get_text(separator='&')
                    parts = text.split("&")
                    if len(parts) >= 3:
                        review = parts[3].strip()

                link = "https://www.flipkart.com" + container['href'] if container else "N/A"

                # push data to lists 
                product_title.append(title)
                product_price.append(price)
                product_rating.append(rating)
                product_review.append(review)
                product_url.append(link)

                # insert into PostgreSQL database
                sql = "INSERT INTO laptops_data(titles, prices, ratings, reviews, link) VALUES (%s, %s, %s, %s, %s)"
                values = (title, price, rating, review, link)
                cursor.execute(sql, values)
                conn.commit()  
        else:
            print(f"Something went wrong on page {page}")  # error handling for pages


# calling function for scrap data
get_products()

# creating DataFrame for view the scrapperd data
df = pd.DataFrame({
    'Product Title': product_title,
    'Price': product_price,
    'Rating': product_rating,
    'Reviews': product_review,
    'Link': product_url
})

print(df)

# save data to CSV
df.to_csv('products.csv', index=False)

# close the database connection
cursor.close()
conn.close()