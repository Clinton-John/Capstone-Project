
-- Create a Database that will hold all of the scrapped articles
CREATE DATABASE capstone_project;

-- use the database for operations
use capstone_project;

-- if there exists a similar table then drop it before creating a new one
Drop table if exists jumia_articles;

-- create a new table known as jumia_articles
CREATE TABLE jumia_articles (
    Article_Name VARCHAR(255) NOT NULL,
    Article_Brand VARCHAR(255) NOT NULL,
    Current_Price INT NOT NULL,
    Initial_Price INT NOT NULL,
    Discount_Percentage INT NOT NULL,
    Article_Rating FLOAT,
    Location VARCHAR(255),
    Category VARCHAR(255)
);

-- Depending on the location of the csv file, Load the data into the database specifying the location
LOAD DATA INFILE 'C:/Users/hp/Desktop/42/lux/Capstone_project/jumia_articles_prep1.csv'
INTO TABLE jumia_articles
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(Article_Name, Article_Brand, Current_Price, Initial_Price, Discount_Percentage, Article_Rating, Location, Category);

-- check if count resembles the columns in the csv file
select count(*) from jumia_articles;
select * from jumia_articles;



select * from jumia_articles;
-- count of total number of articles
select count(*) from jumia_articles;

-- check number of articles with zero ratings and check their percentages 
select * from jumia_articles where Article_Rating = 0; 
select count(*) from jumia_articles where Article_Rating = 0; 

-- check where the discount percentage is zero within the 0 rated articles
select count(*) from jumia_articles 
where Article_Rating = 0 and Discount_Percentage = 0;

-- check all the rows that dont have a 0 ratings
select * from jumia_articles where Article_Rating != 0;
select count(*) from jumia_articles where Article_Rating != 0;









