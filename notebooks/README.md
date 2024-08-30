# 1. Financial News and Stock Price Analysis

This repository contains code and documentation for analyzing financial news and its impact on stock prices. The analysis aims to enhance predictive capabilities by examining the relationship between news sentiment and stock performance, as well as the frequency and distribution of news publication.

## Project Overview

The project involves several key analyses:

1. **Sentiment Analysis**: Evaluates the tone of financial news headlines to determine the sentiment associated with stock-related news.
2. **Correlation Analysis**: Investigates the relationship between news sentiment and stock price changes around the date of publication.
3. **Time Series Analysis**: Analyzes the frequency and distribution of news publications over time.
4. **Publisher Analysis**: Identifies the most frequent publishers and examines their contributions.

## Data

The analysis uses the Financial News and Stock Price Integration Dataset (`FNSPID`). The dataset includes the following columns:

- **headline**: The title of the news article.
- **url**: Direct link to the full news article.
- **publisher**: Author or creator of the article.
- **date**: Publication date and time (including timezone information).
- **stock**: Stock ticker symbol associated with the news.

### Sample Data

```csv
headline,url,publisher,date,stock
"Stocks That Hit 52-Week Highs On Friday","https://www.benzinga.com/news/20/06/16190091/stocks-that-hit-52-week-highs-on-friday","Benzinga Insights","2020-06-05 10:30:54-04:00","A"
"Stocks That Hit 52-Week Highs On Wednesday","https://www.benzinga.com/news/20/06/16170189/stocks-that-hit-52-week-highs-on-wednesday","Benzinga Insights","2020-06-03 10:45:20-04:00","A"
...
```

## Analysis

### 1. Sentiment Analysis

Sentiment analysis is performed on news headlines to determine the sentiment (positive, negative, neutral) using natural language processing (NLP) techniques. This helps in understanding the emotional context of news related to stock movements.

### 2. Correlation Analysis

Correlation analysis examines how sentiment from news articles relates to stock price changes around the publication date. This analysis includes:

- **Daily**: Count of articles published each day.
- **Weekly**: Count of articles published each week.
- **Monthly**: Count of articles published each month.

### 3. Time Series Analysis

Time series analysis evaluates:

- **Publication Frequency**: The number of articles published over time.
- **Spikes**: Identifying any spikes in publication frequency related to specific market events.
- **Publishing Times**: Determining if there are specific times when most news is released, which can be valuable for traders and automated systems.

### 4. Publisher Analysis

Publisher analysis includes:

- **Publisher Contribution**: Identifying which publishers contribute the most to the news feed.
- **Domain Extraction**: Extracting domains from URLs to identify unique domains and see if certain organizations contribute more frequently.

## Getting Started

### Prerequisites

Ensure you have the following Python libraries installed:

- `pandas`
- `numpy`
- `matplotlib`
- `nltk` (for sentiment analysis)
- `sklearn` (for NLP tasks)

You can install these libraries using pip:

```bash
pip install pandas numpy matplotlib nltk scikit-learn
```

# 2: Quantitative Analysis Using PyNance and TA-Lib

## Overview

In this task, we perform a quantitative analysis of stock prices using technical indicators and financial metrics. We leverage Python libraries such as `TA-Lib` for technical analysis and `PyNance` for financial metrics. This analysis helps in understanding stock price trends and predicting future movements.

## Datasets

We will be using historical stock price data for the following companies:

- AAPL (Apple Inc.)
- AMZN (Amazon.com, Inc.)
- GOOG (Alphabet Inc.)
- META (Meta Platforms, Inc.)
- MSFT (Microsoft Corporation)
- NVDA (NVIDIA Corporation)
- TSLA (Tesla, Inc.)

## Steps for Analysis

### 1. Load and Prepare the Data

- Load the stock price data into a Pandas DataFrame.
- Ensure the data includes the following columns: `Date`, `Open`, `High`, `Low`, `Close`, and `Volume`.
- Handle any missing values or incorrect data types.

### 2. Apply Analysis Indicators with TA-Lib

- **Moving Averages**: Calculate the Simple Moving Average (SMA) and Exponential Moving Average (EMA) to smooth out price data.
- **RSI (Relative Strength Index)**: Calculate the RSI to measure the speed and change of price movements.
- **MACD (Moving Average Convergence Divergence)**: Analyze the momentum and trend of the stock prices using the MACD indicator.

### 3. Use PyNance for Financial Metrics

- Calculate various financial metrics like volatility, beta, and Sharpe ratio using `PyNance`.
- Compare these metrics across different stocks to evaluate performance and risk.

### 4. Visualize the Data

- **Price Trends**: Plot the historical price trends along with the moving averages.
- **RSI**: Visualize the RSI to identify overbought or oversold conditions.
- **MACD**: Plot the MACD line and signal line to identify bullish or bearish trends.
- Use `matplotlib` or `seaborn` to create clear and insightful visualizations.

## Prerequisites

Ensure you have the following Python libraries installed:

- `pandas`
- `numpy`
- `matplotlib`
- `TA-Lib`
- `PyNance`

You can install these libraries using pip:

```bash
pip install pandas numpy matplotlib TA-Lib PyNance
```
