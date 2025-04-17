# Sentiment Analysis NLP 🚀

This is a simple yet powerful sentiment analysis tool using NLTK’s VADER model. It classifies input text into **Positive**, **Negative**, or **Neutral** categories based on sentiment scores.

## 🔍 Features
- ✅ Real-time sentiment detection
- 🌐 Easy to extend into a web UI using Streamlit
- 🪶 Lightweight and no training needed
- 📊 Outputs detailed sentiment scores (positive, negative, neutral, compound)

## 📦 Project Structure
```
Sentiment-Analysis-NLP/
├── notebooks/
│   └── sentiment_analysis.ipynb       # Optional Jupyter notebook for experimentation
├── src/
│   └── analyzer.py                    # Core sentiment analysis logic
├── main.py                            # CLI app to analyze text
├── requirements.txt                   # Python dependencies
├── README.md                          # This file
├── streamlit_app.py                   # (Optional) UI with Streamlit
```

## ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/your-username/Sentiment-Analysis-NLP.git
cd Sentiment-Analysis-NLP
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 🖥️ Run the Console App
```bash
python main.py
```
You’ll be prompted to enter a sentence, and the app will output sentiment classification along with detailed scores.

## 🌐 Optional: Run the Streamlit UI
```bash
streamlit run streamlit_app.py
```
A web interface will launch where users can input text and see sentiment predictions visually.

## 💡 Output Example
```
Enter text: I love using this sentiment analysis tool!

Sentiment: Positive
Positive Score: 0.52
Negative Score: 0.00
Neutral Score: 0.48
Compound Score: 0.8126
```

## 📚 References
- [NLTK VADER](https://www.nltk.org/_modules/nltk/sentiment/vader.html)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [VADER Sentiment Analysis Paper](https://ojs.aaai.org/index.php/ICWSM/article/view/14550)
