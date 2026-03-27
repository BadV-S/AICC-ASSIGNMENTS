# ----------------------------------------
# Spam Detection System using Naive Bayes
# ----------------------------------------

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# -----------------------------
# 1. Dataset (Sample)
# -----------------------------
messages = [
    "Win money now",
    "Free iPhone offer",
    "Call me tomorrow",
    "Meeting at 10 AM",
    "Congratulations you won prize",
    "Let's have lunch",
    "Claim your reward now",
    "Project submission reminder"
]

# Labels: 1 = Spam, 0 = Not Spam
labels = [1, 1, 0, 0, 1, 0, 1, 0]

# -----------------------------
# 2. Feature Extraction
# -----------------------------
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)

# -----------------------------
# 3. Model Training
# -----------------------------
model = MultinomialNB()
model.fit(X, labels)

# -----------------------------
# 4. Testing with New Input
# -----------------------------
test_message = ["Free reward waiting for you"]
test_vector = vectorizer.transform(test_message)

prediction = model.predict(test_vector)

# -----------------------------
# 5. Output
# -----------------------------
if prediction[0] == 1:
    print("🚫 Spam Message")
else:
    print("✅ Not Spam Message")