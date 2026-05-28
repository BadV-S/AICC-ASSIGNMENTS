# ----------------------------------------
# NLP Mini App - Keyword Extractor (TF-IDF)
# ----------------------------------------

from sklearn.feature_extraction.text import TfidfVectorizer

text = """
Artificial Intelligence is transforming the world. 
Machine learning and deep learning are subsets of AI.
AI is used in healthcare, finance, and automation.
"""

vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform([text])

feature_names = vectorizer.get_feature_names_out()
scores = X.toarray()[0]

# Get top keywords
keywords = sorted(zip(feature_names, scores), key=lambda x: x[1], reverse=True)

print("Top Keywords:")
for word, score in keywords[:5]:
    print(word, round(score, 2))
