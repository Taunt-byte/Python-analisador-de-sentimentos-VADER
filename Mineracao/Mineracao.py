# Lucas Neves da Silva
# 12/01/2023
# Precisa da biblioteca NLTK 

import nltk

nltk.download('punkt')
nltk.download('stopwords')

# Define the text to be mined
text = "Text mining, also referred to as text data mining, roughly equivalent to text analytics, is the process of deriving high-quality information from text. High-quality information is typically derived through the devising of patterns and trends through means such as statistical pattern learning."

# Tokenize the text into words
tokens = nltk.word_tokenize(text)

# Remove stop words from the token list
stop_words = nltk.corpus.stopwords.words('english')
tokens = [token for token in tokens if token.lower() not in stop_words]

# Perform stemming on the token list
stemmer = nltk.stem.PorterStemmer()
tokens = [stemmer.stem(token) for token in tokens]

# Print the resulting tokens
print(tokens)
