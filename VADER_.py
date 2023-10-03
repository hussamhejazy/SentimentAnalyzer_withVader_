import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


def sentiment(text):
    nltk.download('vader_lexicon')

    analyzer = SentimentIntensityAnalyzer()

    sentiment_scores = analyzer.polarity_scores(text)

    compound_score = sentiment_scores['compound']

    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

