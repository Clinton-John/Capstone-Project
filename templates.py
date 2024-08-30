
#function that gets all of the 40 pages under the Mobile Accessories and append them to a list
response_list = []
for i in range(1, 40):
    page_url = f"https://www.jumia.co.ke/mlp-tech-week-h-smartphones/mobile-accessories/?page={i}#catalog-listing"
    page_response = requests.get(page_url)
    response_list.append(response)
    soup = BeautifulSoup(page_response.text, 'html.parser')






soup = BeautifulSoup(page_response.text, "html.parser")

mobile_articles = soup.find_all('article', class_="prd _fb col c-prd")

for mobile_article in mobile_articles:
    
    article_names =  [article.text.strip() for article in mobile_articles.find_all('h3', class_ = "name") ]  
    print(len(article_names))

    current_prices = [current_price.text.strip() for current_price in mobile_articles.find_all('div', class_ = "prc")]
    print(len(current_prices))

    initial_prices = [initial_price.text.strip() if initial_price != '' else np.Nan for initial_price in mobile_articles.find_all('div', class_ = "old")]
    print(f"Initials Prices: {len(initial_prices)}")