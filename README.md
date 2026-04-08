# Aerofit Treadmill Buyer Analysis

This is a self-guided project for learning, improving and showcasing my data analytics skills.
This project was completed following the instructions on this repo: https://github.com/J-Data-Guy/Aerofit_Project/tree/main

## Objective
The market research team at AeroFit wants to identify the characteristics of the target audience for each type of treadmill offered by the company, to provide a better recommendation of the treadmills to new customers. The team decides to investigate whether there are differences across the product with respect to customer characteristics.

1. Perform descriptive analytics to create a customer profile for each AeroFit treadmill product by developing appropriate tables and charts.

2. For each AeroFit treadmill product, construct two-way contingency tables and compute all conditional and marginal probabilities along with their insights/impact on the business.

## Data Description
The company collected data on individuals who purchased a treadmill from the AeroFit stores during the prior three months. The dataset in aerofit_treadmill_data.csv has the following features:

    Product - product purchased: KP281, KP481, or KP781
    Age - in years
    Gender - male/female
    Education - in years
    MaritalStatus - single or partnered
    Usage - the average number of times the customer plans to use the treadmill each week
    Fitness - self-rated fitness on a 1-5 scale, where 1 is the poor shape and 5 is the excellent shape
    Income - annual income in US dollars
    Miles - the average number of miles the customer expects to walk/run each week

## Approach
I wrote some initial [SQL queries](https://github.com/vish-mandalika/treadmill-buyer-analysis/blob/main/aerofit_sql.sql) to practice my skills and to get an understanding of what the data looks like. Following this I used Python for some more rigorous analytics. My EDA thought process, insights and recommendations to Aerofit are all included within the [Python notebook](https://github.com/vish-mandalika/treadmill-buyer-analysis/blob/main/aerofit_treadmill_buyer_analysis.ipynb).

## Key Findings
- KP781 (premium) buyers are a distinct "serious runner" segment: 
  82.5% male, high fitness (level 4-5), high income ($75k+), 
  planning 4-6 sessions/week
- KP281 and KP481 buyer profiles overlap significantly, suggesting 
  weak product differentiation
- Fitness level and usage intent are the strongest predictors of 
  product choice; marital status has no predictive value
- Age does not predict usage intensity — targeting should focus on 
  fitness behavior, not demographics

## Tools Used
Python (pandas, seaborn, matplotlib), MySQL
