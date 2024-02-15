# Sentiment Analysis using NLTK


This Python script demonstrates sentiment analysis using the Natural Language Toolkit (NLTK) library and its VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment intensity analyzer. 
The script takes user input, analyzes the sentiment of the entered text, and provides sentiment scores, including a compound score indicating overall sentiment.

## Usage

1. **Install Dependencies**:

   Make sure you have NLTK installed. You can install it using the following command:

   ```bash
   pip install nltk
   ```

2. **Download NLTK Data**:

   Run the script provided (`sentiment_analysis_nltk.py`) and follow the prompts to download the required NLTK data:

   ```python
   import nltk
   nltk.download('vader_lexicon')
   ```

3. **Run Sentiment Analysis Script**:

   Execute the script (`sentiment_analysis_nltk.py`) and enter the text for sentiment analysis when prompted.

   ```bash
   python sentiment_analysis_nltk.py
   ```

4. **Interpret Results**:

   The script will output sentiment scores, classifying the sentiment as Positive, Negative, or Neutral based on the compound score.

## Script Explanation

- The script initializes the SentimentIntensityAnalyzer from the NLTK library.
- User input is collected for sentiment analysis.
- Sentiment scores (positive, negative, neutral, compound) are obtained using the analyzer.
- The compound score is used to classify the overall sentiment as Positive, Negative, or Neutral.
- Results, including sentiment scores, are printed to the console.

## Dependencies

- Python 3.x
- NLTK library




