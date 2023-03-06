import gensim
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim.models.phrases import Phraser, Phrases

stop_words = stopwords.words('english')


# 斷詞、轉換小寫、移除符號
def tokenize(sentences):
    return [gensim.utils.simple_preprocess(str(sentence), deacc=True) for sentence in sentences]

'''
def tokenize(sentences):
    token = []
    for sentence in sentences:
        token.append(gensim.utils.simple_preprocess(str(sentence), deacc=True))
    return token
'''
'''
def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))
'''

# 移除停用詞
def remove_stopwods(texts):
    return [[word for word in text if word not in stop_words] for text in texts]


# 設定bigram
def make_bigrams(texts):
    return [bigram_mod[doc] for doc in texts]

# 設定trigram
def make_trigrams(texts):
    return [bigram_mod[doc] for doc in texts]

# 標註詞性
def tag(texts):
    return [pos_tag(text) for text in texts]

'''
def tag(texts):
    tags = []
    for text in texts:
        tags.append(pos_tag(text))
    return tags
'''

# 詞形還原
def lemmatization():
    lemmed_words = []
    wnl = WordNetLemmatizer()
    return lemmed_words