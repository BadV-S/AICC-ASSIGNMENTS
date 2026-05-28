from textblob import TextBlob

reviews = [
    "This movie is amazing and शानदार",
    "Worst movie ever",
    "It was okay, not bad",
    "Absolutely loved the acting",
    "Terrible storyline and boring"
]

for review in reviews:
    polarity = TextBlob(review).sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    print(f"{review} → {sentiment}")
