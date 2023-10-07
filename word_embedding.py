# %%
from itertools import combinations

import spacy

# Load spaCy's pre-trained word embedding model
nlp = spacy.load("en_core_web_sm")

# Input text containing words for similarity comparison
text = (
    "funny comedy music laugh humor song songs jokes musical hilarious"
)

# Process the input text with spaCy
doc = nlp(text)

# Calculate and display similarity between word pairs using spaCy's word vectors
for token1, token2 in combinations(doc, 2):
    print(
        f"similarity between {token1} and {token2} is {token1.similarity(token2)}"
    )

# %%
import pandas as pd
from gensim.models import Word2Vec
from tqdm import tqdm

# Read the movie reviews data from a CSV file named "train.csv"
data = pd.read_csv("train.csv")

# Preprocess the movie reviews into a list of sentences using spaCy's sentence detection
sentences = []
for review in tqdm(data["review"]):
    review_doc = nlp(review)
    review_sentences = [sent.text for sent in review_doc.sents]
    sentences.extend(review_sentences)

# Train a Word2Vec model using the list of sentences
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)

# Ensure words from the input text are present in the model's vocabulary
model.build_vocab([text.split()], update=True)

# %%
# Calculate and display similarity between word pairs using the trained Word2Vec model
for token1, token2 in combinations(text.split(), 2):
    similarity = model.wv.similarity(token1, token2)
    print(
        f"similarity between {token1} and {token2} is {similarity}"
    )
