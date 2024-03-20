# Stock-Pred-V2

This project aims to analyze the sentiment of news headlines related to a particular company and use this sentiment analysis along with historical stock price data to predict the movement of the company's stock price. The sentiment analysis is performed using VADER (Valence Aware Dictionary and sEntiment Reasoner), a rule-based sentiment analysis tool specifically designed for sentiments expressed in social media.

# Overview
1. Sentiment Analysis
The news headlines related to the company are fetched using the News API (powered by NewsAPI.org) based on user input for the company name.
The headlines are then analyzed for sentiment using the VADER sentiment analysis tool.
The sentiment analysis classifies each headline as Positive, Negative, or Neutral based on its compound score.

2. Stock Price Data
Historical stock price data for the selected company is retrieved using the Alpha Vantage API.
The stock prices for the previous week, including the current day, are obtained.

3. Prediction
The sentiment scores are aggregated to determine an overall sentiment score for the week.
The change in stock price from the start to the end of the week is calculated.
Based on the sentiment score and stock price change, a prediction is made:
"Prediction: Up" if sentiment is positive and stock price increased
"Prediction: Down" if sentiment is negative and stock price decreased
"Prediction: No Change" for other cases

# Requirements
Python 3.x
Libraries:
requests
nltk (Natural Language Toolkit)
pandas
alpha_vantage (for stock price data)

# Usage

Install the required libraries if not already installed:
<code>pip install requests nltk pandas alpha_vantage
 </code>

Run the py script:
<code> python main.py
</code>

Follow the prompts to enter the company name and stock symbol (e.g., AAPL for Apple).
The script will:

Fetch news headlines related to the company.
Analyze the sentiment of the headlines.
Retrieve historical stock prices for the previous week.
Calculate sentiment scores and stock price change.
Make a prediction for the stock movement.
The results will be displayed in the console, showing:
Sentiment Analysis for News Headlines
Stock Prices for the Previous Week
Stock Movement Prediction

![example](https://github.com/SrikarRP/Stock-Pred-V2/assets/152237612/8a80113d-4a15-4062-a574-39a647d8cb77)

# Additional Notes
The sentiment analysis and prediction are for educational purposes and should not be used as financial advice.
Stock market predictions are inherently uncertain, and this model is a basic example. Real-world trading decisions should consider a wide range of factors.
![example](https://github.com/SrikarRP/Stock-Pred-V2/assets/152237612/bd092aea-f8e4-4f5b-b928-fd052a3c1979)
