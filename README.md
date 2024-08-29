# Nova Financial Solutions

This project is designed to elevate Nova Financial Solutions' predictive analysis capabilities by enhancing the accuracy of financial forecasts and improving operational efficiency through sophisticated data analysis techniques.

My approach to the analysis is two-fold:

### Sentiment Analysis

I conducted sentiment analysis on the 'headline' text to measure the tone and sentiment conveyed in financial news. By applying natural language processing (NLP) techniques, I derived sentiment scores that are linked to the respective 'Stock Symbol,' enabling a deeper understanding of the emotional context associated with stock-related news.

### Correlation Analysis

I examined the correlations between the sentiment derived from news articles and the corresponding stock price fluctuations around the date the article was published. This analysis also considers the impact of news sentiment on stock performance, factoring in the publication date and, where possible, the specific time the article was released. This approach provides valuable insights into how news sentiment influences market behavior.

## Dataset Overview

The analysis is based on the Financial News and Stock Price Integration Dataset (FNSPID), a comprehensive financial dataset that combines quantitative and qualitative data to enhance stock market predictions. The dataset includes:

- **headline**: The title of the news article, often highlighting key financial actions like stocks hitting highs, price target changes, or company earnings.
- **url**: The direct link to the full news article.
- **publisher**: The author or creator of the article.
- **date**: The publication date and time, including timezone information (UTC-4).
- **stock**: The stock ticker symbol (e.g., AAPL for Apple), a unique series of letters assigned to a publicly traded company.
