# Import necessary libraries
import os
from alpha_vantage.timeseries import TimeSeries
from datetime import datetime, timedelta
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import pandas as pd
import requests
api_key1 = "news api key"

# Define company name (user input)
company_name = input("Enter company name: ")

# Build the news API URL
url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={api_key1}"

# Send GET request and get response
response = requests.get(url)

# Check for successful response
if response.status_code == 200:
    # Parse JSON data
    data = response.json()

    # Directory to save news
    save_directory = r"/directory/news.txt"

    # Create the directory if it doesn't exist
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # File to store news
    file_name = os.path.join(save_directory, f"news.txt")

    # Print headlines and store in file with UTF-8 encoding
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f"Latest news for {company_name}:\n")
        for article in data["articles"]:
            file.write(f"- {article['title']}\n")
            print(f"- {article['title']}")

    print(f"\nNews saved to {file_name}")
else:
    print("Error: Failed to retrieve news.")
# Function to analyze sentiment using VADER
def analyze_sentiment_vader(text):
    sid = SentimentIntensityAnalyzer()
    # Polarity scores
    scores = sid.polarity_scores(text)
    # Classify sentiment
    if scores['compound'] > 0.05:
        return "Positive"
    elif scores['compound'] < -0.05:
        return "Negative"
    else:
        return "Neutral"

# Function to predict stock movement based on sentiment and stock data
def predict_stock_movement(sentiment_score, stock_change):
    if sentiment_score == 1 and stock_change > 0:
        return "Prediction: Up"
    elif sentiment_score == -1 and stock_change < 0:
        return "Prediction: Down"
    else:
        return "Prediction: No Change"

# Alpha Vantage API key (replace with your own key)
api_key2 = "Vantage API KEY"

# Define the stock symbol (e.g., AAPL for Apple)
stock_symbol = input("Enter stock symbol (e.g., AAPL): ")

# Create a TimeSeries object
ts = TimeSeries(key=api_key2, output_format='pandas')

# Get today's date and date one week ago
today = datetime.now()
one_week_ago = today - timedelta(days=7)

# Convert dates to strings in the format required by Alpha Vantage
today_str = today.strftime('%Y-%m-%d')
one_week_ago_str = one_week_ago.strftime('%Y-%m-%d')

# Get stock prices for the previous week including today
try:
    data, _ = ts.get_daily(symbol=stock_symbol, outputsize='full')

    # Sort the DataFrame by the index (date)
    data.sort_index(inplace=True)
    
    # Filter data for the previous week
    data_week = data.loc[one_week_ago_str:today_str]
    
    # Directory to save stock prices
    save_directory = r"/savelocation"

    # Create the directory if it doesn't exist
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)

    # File to store stock prices
    file_name = os.path.join(save_directory, f"{stock_symbol}_stock_prices.csv")

    # Save data to CSV file
    data_week.to_csv(file_name)

    # Path to the news file
    news_file = "newsfilelocation"

    # Calculate sentiment score based on news headlines
    positive_count = 0
    negative_count = 0
    neutral_count = 0

    with open(news_file, 'r', encoding='utf-8') as file:
        headlines = file.readlines()
        for headline in headlines:
            sentiment = analyze_sentiment_vader(headline)
            if sentiment == "Positive":
                positive_count += 1
            elif sentiment == "Negative":
                negative_count += 1
            elif sentiment == "Neutral":
                neutral_count += 1

    # Calculate sentiment score
    if positive_count > negative_count:
        sentiment_score = 1
    elif negative_count > positive_count:
        sentiment_score = -1
    else:
        sentiment_score = 0

    # Get stock price change from the start to the end of the week
    stock_change = data_week.iloc[-1]['4. close'] - data_week.iloc[0]['4. close']

    # Predict stock movement based on sentiment and stock data
    prediction = predict_stock_movement(sentiment_score, stock_change)

    # Display results
    print("Sentiment Analysis for News Headlines:")
    print(f"Positive News: {positive_count}")
    print(f"Negative News: {negative_count}")
    print(f"Neutral News: {neutral_count}")
    print("\nStock Prices for the Previous Week:")
    print(data_week)
    print("\nStock Movement Prediction:")
    print(prediction)

except Exception as e:
    print("Error:", e)
