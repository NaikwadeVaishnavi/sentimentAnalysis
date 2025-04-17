from src.analyzer import analyze_sentiment

if __name__ == "__main__":
    text = input("\nEnter text: ")
    result = analyze_sentiment(text)

    print(f"\nSentiment: {result['Sentiment']}")
    print(f"Positive Score: {result['Scores']['pos']}")
    print(f"Negative Score: {result['Scores']['neg']}")
    print(f"Neutral Score: {result['Scores']['neu']}")
    print(f"Compound Score: {result['Scores']['compound']}")
