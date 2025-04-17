# Sentiment Analysis NLP 🚀

This is a simple yet powerful sentiment analysis tool using NLTK’s VADER model. It classifies input text into Positive, Negative, or Neutral categories based on sentiment scores.

## Features
- Real-time sentiment detection
- Easy to extend into a web UI using Streamlit
- Lightweight and no training needed

## Setup
```bash
git clone https://github.com/your-username/Sentiment-Analysis-NLP.git
cd Sentiment-Analysis-NLP
pip install -r requirements.txt
```

## Run the Console App
```bash
python main.py
```

## Optional: Run the Streamlit UI
```bash
streamlit run streamlit_app.py
```

## Output Example
```
Sentiment: Positive
Positive Score: 0.52
Negative Score: 0.00
Neutral Score: 0.48
Compound Score: 0.8126
```

## References
- [NLTK VADER](https://www.nltk.org/_modules/nltk/sentiment/vader.html)
- [Streamlit Docs](https://docs.streamlit.io/)
