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


# The List will be formated in the function to add the number to be passed
links_list = [
    "https://www.jumia.co.ke/mlp-tech-week-h-smartphones/mobile-accessories/?page={i}#catalog-listing", #mobile accesories
    "https://www.jumia.co.ke/watches-sunglasses/?page={i}#catalog-listing", # watches
    "https://www.jumia.co.ke/computing/?page={i}#catalog-listing", # computing
    "https://www.jumia.co.ke/home-office-appliances/?page={i}#catalog-listing", # home_appliances
    "https://www.jumia.co.ke/smartphones/?sort=rating&tag=JMALL&page={i}#catalog-listing", # smartphones
    "https://www.jumia.co.ke/home-office-appliances/?rating=3-5&shipped_from=jumia_global&page={i}#catalog-listing" # appliances from abroad
]


def add_data(mobile_article, category_type):
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

    category.append(category_type)


def scrape_pages(page_url, category_type):
    category_type = category_type
    page_response = requests.get(page_url)
    soup = BeautifulSoup(page_response.text, 'html.parser')
    pages_articles = soup.find_all('article', class_="prd _fb col c-prd")
    # articles_count = len(pages_articles)
    # print(f"There are {articles_count} in This page")
    for article in pages_articles:
        add_data(article, category_type)


# The condition incharge of collecting all of the information and 
def collect_data():
    for i_index, i_link in enumerate(links_list):
        if i_index == 0:
            for i in range(1, 25):
                category_type = "Mobile Accessories"
                scrape_pages(i_link.format(i=i), category_type)
        elif i_index == 1:
            for i in range(1, 25):
                category_type = "Watches"
                scrape_pages(i_link.format(i=i), category_type)
        elif i_index == 2:
            for i in range(1, 25):
                category_type = "Computing"
                scrape_pages(i_link.format(i=i), category_type)
        elif i_index == 2:
            for i in range(1, 25):
                category_type = "Home Appliances"
                scrape_pages(i_link.format(i=i), category_type)
        elif i_index == 4:
            for i in range(1,6):
                category_type = "Smartphones"
                scrape_pages(i_link.format(i=i), category_type)
        elif i_index == 5:
            for i in range(1,3):
                category_type = "Home Appliances"
                scrape_pages(i_link.format(i=i), category_type)

    articles_df = pd.DataFrame({
        'Article Name': article_names,
        'Current Price': current_prices,
        'Initial Price' : initial_prices,
        'Discount Percentage': discount_prcnts,
        'Article Rating': article_ratings,
        'Number of Ratings': no_of_ratings,
        'location' : locations,
        'category' : category
        })

    return articles_df

def main():
    articles_dataframe = collect_data()

    #convert the dataframe into a csv file for download
    articles_dataframe.to_csv("jumia_articles.csv", index=False)

if __name__ == '__main__':
    main()
