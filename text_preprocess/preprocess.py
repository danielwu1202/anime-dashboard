import gensim
import nltk

nltk.download('stopwords')

# 斷詞、轉換小寫、移除符號
def preprocess(origin, data):
    origin['token'] = list(gensim.utils.simple_preprocess([sentence for sentence in data]))