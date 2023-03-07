import nltk
import gensim
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim.models.phrases import Phraser, Phrases

nltk.download('omw-1.4')
stop_words = stopwords.words('english')


def LDA_pipeline(data, column='Synopsis'):
    synopsis = data[column].values.tolist()
    sentences = [sent for sent in synopsis if sent != 'Unknown']

    wnl = WordNetLemmatizer()

    token = [gensim.utils.simple_preprocess(str(sentence), deacc=True) for sentence in sentences]

    tags = [pos_tag(text) for text in token]

    # TODO 詞形還原的部分將詞性作為參數
    lemmed_token = []
    for tag in tags:
        temp = []
        for t in tag:
            if t[1] == 'NNS':
                temp.append(wnl.lemmatize(t[0], pos = 'n'))
            elif t[1] == 'VBD' or 'VBG' or 'VBN' or 'VBZ':
                temp.append(wnl.lemmatize(t[0], pos = 'v'))
            elif t[1] == 'NN':
                temp.append(wnl.lemmatize(t[0], pos = 'n'))
            elif t[1] == 'JJ':
                temp.append(wnl.lemmatize(t[0], pos = 'a'))
            elif t[1] == 'RB':
                temp.append(wnl.lemmatize(t[0], pos = 'r'))
        lemmed_token.append(temp)

    bigram = Phrases(token)
    bigram_mod = Phraser(bigram)
    trigram = Phrases(bigram[token])
    trigram_mod = Phraser(trigram)

    word_bigram = [bigram_mod[doc] for doc in lemmed_token]
    word_trigram = [trigram_mod[bigram_mod[doc]] for doc in word_bigram]

    word_nostop = [[word for word in text if word not in stop_words] for text in word_trigram]

    return word_nostop





'''
# 斷詞、轉換小寫、移除符號
def tokenize(sentences):
    return [gensim.utils.simple_preprocess(str(sentence), deacc=True) for sentence in sentences]
'''

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

'''
# 移除停用詞
def remove_stopwods(texts):
    return [[word for word in text if word not in stop_words] for text in texts]
'''

'''
# 設定bigram
def make_bigrams(texts):
    return [bigram_mod[doc] for doc in texts]

# 設定trigram
def make_trigrams(texts):
    return [trigram_mod[bigram_mod[doc]] for doc in texts]

# 標註詞性
def tag(texts):
    return [pos_tag(text) for text in texts]

'''


'''
def tag(texts):
    tags = []
    for text in texts:
        tags.append(pos_tag(text))
    return tags
'''
