# %%
import pandas as pd
import spacy
from tqdm import tqdm


nlp = spacy.load("en_core_web_sm")
data = pd.read_csv("train.csv")

def get_adjs(doc):
    # Find all adjectives in the doc
    result = [token.text for token in doc if token.pos_ == "ADJ"]
    return result

def get_ents(doc):
    # Find all named entities in the doc
    result = [ent.text for ent in doc.ents]
    return result

def get_number_of_sents(doc):
    # Find the number of sentences in the doc
    result = len(list(doc.sents))
    return result

# %%
from collections import Counter


number_of_sents, pos_adj_counter, neg_adj_counter, ent_counter = (
    [],
    Counter(),
    Counter(),
    Counter(),
)

for review, sentiment in tqdm(data.to_records(index=False)):
    doc = nlp(review)
    adjs = get_adjs(doc)
    ents = get_ents(doc)
    
    # Append the number of sentences to number_of_sents list
    number_of_sents.append(get_number_of_sents(doc))

    # Update pos_adj_counter and neg_adj_counter based on sentiment
    if sentiment == "positive":
        pos_adj_counter.update(adjs)
    else:
        neg_adj_counter.update(adjs)

    # Update ent_counter with named entities
    ent_counter.update(ents)

# %%
# Add number_of_sents as a new column to data DataFrame
data["number_of_sents"] = number_of_sents
import seaborn as sns

# Generate boxplot of number of sentences by sentiment
sns.boxplot(x="sentiment", y="number_of_sents", data=data)

# %%
# Generate barplot of top 20 named entities
top20_ent = ent_counter.most_common()[:20]

y = [t[0] for t in top20_ent]
x = [t[1] for t in top20_ent]

sns.barplot(x=x, y=y)

# %%
# Generate barplots of top 20 positive and negative adjectives
import matplotlib.pyplot as plt

_, axes = plt.subplots(1, 2, figsize=(16, 8))

top20_pos_adj = pos_adj_counter.most_common()[:20]
y = [t[0] for t in top20_pos_adj]
x = [t[1] for t in top20_pos_adj]
sns.barplot(x=x, y=y, ax=axes[0])


top20_neg_adj = neg_adj_counter.most_common()[:20]
y = [t[0] for t in top20_neg_adj]
x = [t[1] for t in top20_neg_adj]
sns.barplot(x=x, y=y, ax=axes[1])

# Questions:
# a. Is there a significant difference in the number of sentences depending on the overall sentiment of movie reviews?
# No, the difference in number of sentences between reviews with positive and negative sentiment are not statistically significant.

# b. What are the most frequently mentioned entities from the movie reviews?
# The most frequent entities mentioned in total are "one," "first," and "two,"
# And the most frequent entities mentioned that don't have to do with numerics are "Hollywood," "American," "today," "English," and "gore"

# c. What types of adjectives are more frequently used in positive movie reviews than negative ones?
# It is more likely to see the adectives "great," "best," and "real" in positive reviews than negative ones