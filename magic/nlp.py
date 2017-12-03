# import nltk
import json
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from data_preprocessing import read_csv
import sys
from collections import Counter

from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.feature_extraction.text import CountVectorizer

stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()
vectorizer = CountVectorizer()
reload(sys)
sys.setdefaultencoding('utf8')

# nltk.download()

def create_lexicon(df):
    lexicon = []

    news_titles = df['title']
    news_description = df['description']

    for i, title in news_titles.iteritems():
        words = word_tokenize(str(title))
        lemmatized_title = []

        for word in words:
            if word not in stop_words:
                formatted_word = format_word(word)
                print 'formatted word: ', formatted_word
                lemmatized_word = ps.stem(formatted_word)
                print 'lemmatized_word: ', lemmatized_word

                lemmatized_title.append(lemmatized_word)
                lexicon.append(lemmatized_word)

        print lemmatized_title
        df.set_value(i, 'title', lemmatized_title)

    for i, description in news_description.iteritems():
        words = word_tokenize(str(description))
        lemmatized_description = []

        for word in words:
            if word not in stop_words:
                formatted_word = format_word(word)
                lemmatized_word = ps.stem(formatted_word)
                print 'formatted word: ', formatted_word
                print 'lemmatized_word: ', lemmatized_word

                lemmatized_description.append(lemmatized_word)

                if lemmatized_word not in lexicon:
                    lexicon.append(lemmatized_word)

        print lemmatized_description
        df.set_value(i, 'description', lemmatized_description)

    w_counts = Counter(lexicon)
    print 'word counts: ', w_counts
    filtered_lexicon = []

    for w in w_counts:
        if 10000 > w_counts[w] > 5:
            filtered_lexicon.append(w)

    print "filtered_lexicon: ", filtered_lexicon
    print "filtered_lexicon length: ", len(filtered_lexicon)
    return filtered_lexicon

def read_lexicon_from_txt():
    with open("lexicon.txt", "r") as f:
        read_lexicon = json.load(f)
        print "read_lexicon"
        print read_lexicon
    return read_lexicon

def write_lexicon_to_txt(corpus, filename):
    with open(filename, "w") as f:
        return json.dump(corpus, f)

def format_word(word):
    return word.decode('utf-8', 'replace')\
               .replace(u"\u2018", "")\
               .replace(u"\u2019", "")\
               .replace(u"\u201c", "")\
               .replace(u"\u201d", "")\
               .lower()

df_stock_news = read_csv('../assets/article_stock/nytimes1.csv', ',')
lexicon = create_lexicon(df_stock_news)
#lexicon = read_lexicon_from_txt()
print lexicon
write_lexicon_to_txt(lexicon, "lexicon.txt")

bag_of_words = vectorizer.fit_transform(lexicon)
bag_of_words = bag_of_words.toarray()
vocab = vectorizer.get_feature_names()

print 'apple', vectorizer.vocabulary_.get("appl")
print "vocab getme appl"
print vocab[vocab.index("appl")]

# takes df_stock_news as the argument
def create_one_hot_df(df):
    df_training_data = pd.DataFrame(0, index=np.arange(df.shape[0]), columns=vocab)

    for i, row in df.iterrows():
        title = df.loc[i, 'title']
        for word in title:
            print ps.stem(format_word(word))
            if word in vocab:
                print word
                df_training_data.set_value(i, word, df_training_data.loc[i, word] + 1)
        print title

    for i, row in df.iterrows():
        description = df.loc[i, 'description']
        for word in description:
            print ps.stem(format_word(word))
            if word in vocab:
                df_training_data.set_value(i, word, df_training_data.loc[i, word] + 1)
        print description

    for i, row in df.iterrows():
        stock_change = df.loc[i, 'stock_change']
        print stock_change
        if stock_change > 0.05:
            df_training_data.set_value(i, 'stock_price_up', 1)
            df_training_data.set_value(i, 'stock_price_stay', 0)
            df_training_data.set_value(i, 'stock_price_down', 0)
        if -0.05 <= stock_change <= 0.05:
            df_training_data.set_value(i, 'stock_price_up', 0)
            df_training_data.set_value(i, 'stock_price_stay', 1)
            df_training_data.set_value(i, 'stock_price_down', 0)
        if stock_change < -0.05:
            df_training_data.set_value(i, 'stock_price_up', 0)
            df_training_data.set_value(i, 'stock_price_stay', 0)
            df_training_data.set_value(i, 'stock_price_down', 1)

    df_stock_changes = pd.DataFrame({
        'stock_price_up': df_training_data['stock_price_up'],
        'stock_price_stay': df_training_data['stock_price_stay'],
        'stock_price_down': df_training_data['stock_price_down']
    })

    print "df_stock_changes", df_stock_changes.head()
    df_training_data.drop(['stock_price_up', 'stock_price_stay', 'stock_price_down'], axis=1, inplace=True)
    df_corpus = df_training_data

    print "df_corpus", df_corpus.head()

    df_corpus.to_csv('df-corpus.csv')
    df_stock_changes.to_csv('df-stock-changes.csv')

    np_corpus = df_corpus.as_matrix(columns=None)
    np_stock_change = df_stock_changes.as_matrix(columns=None)

    print np_corpus
    print np_stock_change

    print len(np_corpus)
    print len(np_stock_change)
    np_training_data = np.column_stack((np_corpus, np_stock_change))
    print np_training_data
    return np_training_data


np_training_data = create_one_hot_df(df_stock_news)

np.save('np_training_data.txt', np_training_data)


def number_of_all_words(df):
    sum = 0

    for i, row in df.iterrows():
        one_hot_array = []
        text = []
        for column_i, column in df.columns.values:
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

def classify_stock_change(df):
    for i, row in df.iterrows():
        print df.loc[i, 'stock_price_change']
        if df.loc[i, 'stock_price_change'] > 0.08:
            df.set_value(i, 'stock_price_change', [1, 0, 0])
        if -0.08 <= df.loc[i, 'stock_price_change'] <= 0.08:
            df.set_value(i, 'stock_price_change', [0, 1, 0])
        if df.loc[i, 'stock_price_change'] < -0.08:
            df.set_value(i, 'stock_price_change', [0, 0, 1])



# print df_training_data['stock_price_change']

# for i, change in stock_change.iterrows():
#     print change


# df_training_data['stock_price_change'] = df_stock_news['stock_change']


def normalize_dataframe(df):
    values = df.values #returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    values_scaled = min_max_scaler.fit_transform(values)
    normalized_df = pd.DataFrame(values_scaled, columns=df.columns.values)

    return normalized_df

# df_training_data = normalize_dataframe(df_training_data)

def init():
    # df_training_data = read_csv('../assets/training_data/training_data-stock_change.csv', ',')
    # classify_stock_change(df_training_data)
    # df_training_data.to_csv('training_data-stock_change-classified-stock-change.csv')
    # df_training_data = normalize_dataframe(df_training_data)
    # df_training_data.to_csv('training_data-stock_change-normalized-classified-stock-change.csv')
    print 'nlp.py is running'

init()
