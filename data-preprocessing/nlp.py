import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from data_preprocessing import read_csv

# nltk.download()

df_stock_news = read_csv('../assets/article_stock/nytimes1.csv', ',')
news_titles = df_stock_news['title']

print news_titles
