
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download NLTK data (if not already downloaded)
nltk.download('vader_lexicon')

# Initialize the SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

# Sample text
text = input("\nEnter text :")

# Get sentiment scores
sentiment_scores = analyzer.polarity_scores(text)

# Interpret the sentiment scores
compound_score = sentiment_scores['compound']

if compound_score >= 0.05:
    sentiment = "Positive"
elif compound_score <= -0.05:
    sentiment = "Negative"
else:
    sentiment = "Neutral"

# Print the sentiment and scores
print(f"Sentiment: {sentiment}\n")
print(f"Positive Score: {sentiment_scores['pos']}\n")
print(f"Negative Score: {sentiment_scores['neg']}\n")
print(f"Neutral Score: {sentiment_scores['neu']}\n")
print(f"Compound Score: {sentiment_scores['compound']}\n")

