# Financial News and Stock Price Analysis

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
