from sklearn.feature_extraction.text import TfidfVectorizer

docs = [
    "machine learning is powerful",
    "deep learning improves AI",
    "AI is transforming industries",
    "machine learning and AI are related",
    "deep learning uses neural networks"
]

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(docs)

feature_names = vectorizer.get_feature_names_out()

# Get top keywords per document
for i, doc in enumerate(X):
    print(f"\nDocument {i+1}:")
    scores = zip(feature_names, doc.toarray()[0])
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    for word, score in sorted_scores[:3]:
        print(word, round(score, 2))
