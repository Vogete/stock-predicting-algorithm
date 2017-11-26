# import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from data_preprocessing import read_csv
import sys

stop_words = set(stopwords.words("english"))
print stop_words

ps = PorterStemmer()

reload(sys)
sys.setdefaultencoding('utf8')

# nltk.download()

df_stock_news = read_csv('../assets/article_stock/nytimes1.csv', ',')

def create_corpus(df):
    corpus = []

    news_titles = df['title']
    news_description = df['description']

    for i, title in news_titles.iteritems():
        words = word_tokenize(title)
        filtered_title = []

        for word in words:
            if word not in stop_words:
                filtered_title.append(word.decode('utf-8').replace(u"\u2018", "").replace(u"\u2019", "").replace(u"\u201d", "").lower())
                print word

        print filtered_title
        stemmed_title = []
        for word in filtered_title:
            if word not in corpus:
                corpus.append(word)
            stemmed_title.append(ps.stem(word))

        print stemmed_title

        df.set_value(i, 'title', stemmed_title)

    for i, title in news_description.iteritems():
        words = word_tokenize(title)
        filtered_description = []

        for word in words:
            if word not in stop_words:
                filtered_description.append(word.decode('utf-8').replace(u"\u2018", "").replace(u"\u2019", "").replace(u"\u201d", "").lower())
                print word

        print filtered_description
        stemmed_description = []
        for word in filtered_description:
            if word not in corpus:
                corpus.append(word)
            stemmed_description.append(ps.stem(word))

        print stemmed_description

        df.set_value(i, 'description', stemmed_description)

    return corpus


corpus = create_corpus(df_stock_news)

text_file = open("corpus.txt", "w")
text_file.write(str(corpus))
text_file.close()
print len(corpus)
print df_stock_news.head()
