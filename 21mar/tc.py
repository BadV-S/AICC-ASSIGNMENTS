import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Sample text
text = "OMG!!! This movie is sooo good 😂😂 I luv it!!!"

# Download once (run only first time)
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')

# Step 1: Lowercase
text = text.lower()

# Step 2: Remove punctuation & emojis
text = re.sub(r'[^a-z\s]', '', text)

# Step 3: Tokenize
words = word_tokenize(text)

# Step 4: Remove stopwords
stop_words = set(stopwords.words('english'))
clean_words = [word for word in words if word not in stop_words]

# Final cleaned text
clean_text = " ".join(clean_words)

print("Cleaned Text:", clean_text)