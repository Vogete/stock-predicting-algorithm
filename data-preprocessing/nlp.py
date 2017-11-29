# import nltk
import json
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from data_preprocessing import read_csv
import sys

from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.feature_extraction.text import CountVectorizer

stop_words = set(stopwords.words("english"))
ps = PorterStemmer()
vectorizer = CountVectorizer()
reload(sys)
sys.setdefaultencoding('utf8')

# nltk.download()

df_stock_news = read_csv('../assets/article_stock/nytimes2.csv', ',')

def create_corpus(df):
    corpus = []

    news_titles = df['title']
    news_description = df['description']

    for i, title in news_titles.iteritems():
        words = word_tokenize(str(title))
        stemmed_title = []

        for word in words:
            if word not in stop_words:
                formatted_word = format_word(word)
                stemmed_word = ps.stem(formatted_word)

                stemmed_title.append(stemmed_word)

                if stemmed_word not in corpus:
                    corpus.append(stemmed_word)

        print stemmed_title
        df.set_value(i, 'title', stemmed_title)

    for i, description in news_description.iteritems():
        words = word_tokenize(str(description))
        stemmed_description = []

        for word in words:
            if word not in stop_words:
                formatted_word = format_word(word)
                stemmed_word = ps.stem(formatted_word)

                stemmed_description.append(stemmed_word)

                if stemmed_word not in corpus:
                    corpus.append(stemmed_word)

        print stemmed_description
        df.set_value(i, 'description', stemmed_description)

    return corpus

def read_corpus_from_txt():
    with open("corpus.txt", "r") as f:
        read_corpus = json.load(f)
        print "read_corpus"
        print read_corpus
    return read_corpus

def write_corpus_to_txt(corpus, filename):
    with open(filename, "w") as f:
        return json.dump(corpus, f)

def format_word(word):
    return word.decode('utf-8', 'replace')\
               .replace(u"\u2018", "")\
               .replace(u"\u2019", "")\
               .replace(u"\u201c", "")\
               .replace(u"\u201d", "")\
               .lower()

# corpus = create_corpus(df_stock_news)
# write_corpus_to_txt(corpus, "vocab.txt")

# bag_of_words = vectorizer.fit_transform(corpus)
# bag_of_words = bag_of_words.toarray()
# vocab = vectorizer.get_feature_names()

# print 'basketbal', vectorizer.vocabulary_.get("basketbal")
# print "vocab getme basketbal"
# print vocab[vocab.index("basketbal")]

# takes df_stock_news as the argument
def create_one_hot_df(df):
    df_training_data = pd.DataFrame(0, index=np.arange(df.shape[0]), columns=vocab)

    for i, row in df.iterrows():
        title = df.loc[i, 'title']
        for word in title:
            # print ps.stem(format_word(word))
            if word in vocab:
                print word
                df_training_data.set_value(i, word, df_training_data.loc[i, word] + 1)
        print title

    for i, row in df.iterrows():
        description = df.loc[i, 'description']
        for word in description:
            # print ps.stem(format_word(word))
            if word in vocab:
                df_training_data.set_value(i, word, df_training_data.loc[i, word] + 1)
        print description

# print df_training_data

# df_training_data.to_csv('training_data.csv')

def number_of_all_words(df):
    sum = 0

    for i, row in df.iterrows():
        one_hot_array = []
        text = []
        for column_i, column in df:
            word_number = df.loc[i, column]
            if word_number > 0:
                one_hot_array.append(word_number)
                word = vocab[column_i]
                text.append(word)

                sum = sum + word_number
        print one_hot_array
        print "SUM: ", sum

# number_of_all_words(df_training_data)

# print df_stock_news.head()

# df_training_data1 = read_csv('../assets/training_data/training_data-stock_change.csv', ',')
df_training_data = read_csv('../assets/training_data/training_data.csv', ',')

# print df_training_data1.shape
print df_training_data.shape

# print df_training_data['stock_price_change']

# for i, change in stock_change.iterrows():
#     print change


# df_training_data['stock_price_change'] = df_stock_news['stock_change']


def normalize_dataframe(df):
    values = df.values #returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    values_scaled = min_max_scaler.fit_transform(values)
    normalized_df = pd.DataFrame(values_scaled, columns=df_training_data.columns.values)

    return normalized_df

df_training_data = normalize_dataframe(df_training_data)

df_training_data.to_csv('training_data-stock_change-normalized.csv')
