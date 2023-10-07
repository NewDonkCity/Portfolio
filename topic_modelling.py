import pandas as pd
import spacy
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer

nlp = spacy.load("en_core_web_sm")
data = pd.read_csv("train.csv")

def show_topic(model, feature_names, top):
    for index, distribution in enumerate(model.components_):
        sorted_word_indices = distribution.argsort()[::-1][:top]
        print(f"Topic {index}:")
        print(" ".join([feature_names[i] for i in sorted_word_indices]))

# CountVectorizer
tf_vectorizer = CountVectorizer(
    stop_words="english",  # Remove common English words
    max_df=0.8,            # Ignore terms that appear in more than 80% of the documents
    min_df=2               # Ignore terms that appear in fewer than 2 documents
)
tf = tf_vectorizer.fit_transform(data["review"])

# LatentDirichletAllocation
num_topics = 20  # Number of topics you want to extract
lda = LatentDirichletAllocation(
    n_components=num_topics,  # Number of topics
    max_iter=10,              # Maximum number of iterations
    learning_method="online", # Learning method for LDA
    random_state=42           # Random state for reproducibility
)
lda.fit(tf)

tf_feature_names = tf_vectorizer.get_feature_names_out()
top_words_per_topic = 10
show_topic(lda, tf_feature_names, top_words_per_topic)
