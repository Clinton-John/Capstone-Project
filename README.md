**E-COMMERCE WEB SCRAPING AND DATA ANALYSIS PROJECT**

This project involves scraping products from Jumia, a well known and trusted e commerce website, adding the scraped data into a Mysql database, exploring the data and then using the retreived data to analyse and create and interactive dashboard. The dashboard contains different graphs and charts that show the distribution of the discounted data. 

The Project involves Scraping more than 100 pages of Jumia website and creating up to 7 different features which are passed into a csv file, then loaded to the local database where it can be fetched

TOOLS AND LIBRARIES FOR THE PROJECT 
1. BeautifulSoup - a Library used fro parsing the HTML extracting data from static web pages.
2. requests - a library used together with the beautifulSoup to send requests to the webpage
3. Python - for writing scripts that scrape the website, and for perfoming EDA
4. Pandas - For analysing and manipulating some of the data that are received from the webscraping.
5. Numpy - for all of the numerical operations and calculations.
6. Matplotlib and Seaborn - for creating the plots and charts that are used in the
7. Excel - For creating the Interactive Dashboards analysing the different features within the 

FILES 
1. main_scraper_file.py - The python script that sends requests to the e-commerce website to retreive the data
2. jumia_articles_preprocessing.ipynb - The notebook that is incharge of preprocessing the scrapped data before it is sent to the database.
3. project_tracker.txt - Shows the different steps taken throughout the project
4. jumia_articles_prep2.xlsx - Contains all the scrapped data and the dashboards created through pivot tables in Excel 
5. sql_analysis_jumia.sql - contains the databse creation, loading of the data, and some analysis using sql 

PROJECT DESCRIPTION
The Web Scraping and Analysis from Jumia shows how different categories of products relate to each other and their distribution. Through the charts, the top Brands are obtained, top brands per category, the categories with the highest discount, the categories with the highest ratings, and they are presented through charts.