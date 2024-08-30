

page_url = f"https://www.jumia.co.ke/watches-sunglasses/?page={i}#catalog-listing"


import pandas as pd 
import numpy as np
from bs4 import BeautifulSoup
import requests

article_names = []
current_prices = []
initial_prices = []
discount_prcnts = []
article_ratings = []
no_of_ratings = []
locations = []
category = []

def scrape_pages():
    # for i in range(1, 25): # This will give 400 items for the above 
    for i in range(1, 3):
        page_url = f"https://www.jumia.co.ke/watches-sunglasses/?page={i}#catalog-listing"
        page_response = requests.get(page_url)
        soup = BeautifulSoup(page_response.text, 'html.parser')
        mobile_articles = soup.find_all('article', class_="prd _fb col c-prd")
        articles_count = len(mobile_articles)
        print(f"There are {articles_count} in This page")
        for mobile_article in mobile_articles:
            add_data(mobile_article)

    mobile_accessory_df = pd.DataFrame({
    'Article Name': article_names,
    'Current Price': current_prices,
    'Initial Price' : initial_prices,
    'Discount Percentage': discount_prcnts,
    'Article Rating': article_ratings,
    'Number of Ratings': no_of_ratings,
    'location' : locations,
    'category' : category
    })

    return mobile_accessory_df


def add_data(mobile_article):
    # Extract article name
    article_names.append(mobile_article.find('h3', class_='name').text.strip() if mobile_article.find('h3', class_='name') else np.nan)
    
    # Extract current price
    current_prices.append(mobile_article.find('div', class_='prc').text.strip() if mobile_article.find('div', class_='prc') else np.nan)
    
    # Extract initial price
    initial_prices.append(mobile_article.find('div', class_='old').text.strip() if mobile_article.find('div', class_='old') and mobile_article.find('div', class_='old').text.strip() != '' else np.nan)
    
    # Extract discount percentage
    discount_prcnts.append(mobile_article.find('div', class_='bdg _dsct _sm').text.strip() if mobile_article.find('div', class_='bdg _dsct _sm') and mobile_article.find('div', class_='bdg _dsct _sm').text.strip() != '' else np.nan)
    
    # Extract article rating
    article_ratings.append(mobile_article.find('div', class_='stars _s').text.strip() if mobile_article.find('div', class_='stars _s') and mobile_article.find('div', class_='stars _s').text.strip() != '' else np.nan)
    
    # Extract number of ratings
    no_of_ratings.append(mobile_article.find('div', class_='in').text.strip() if mobile_article.find('div', class_='in') and mobile_article.find('div', class_='in').text.strip() != '' else np.nan)
    
    # Extract location
    locations.append(mobile_article.find('div', class_='bdg _glb _xs').text.strip() if mobile_article.find('div', class_='bdg _glb _xs') and mobile_article.find('div', class_='bdg _glb _xs').text.strip() != '' else 'Within Country')

    category.append("Watches")

# Get the dataframe and then convert the dataframe into a csv file
def main():
    mobile_dataframe = scrape_pages()
    mobile_dataframe.to_csv('mobile_access_df.csv', index=False)
    

if __name__ == '__main__':
    main()

