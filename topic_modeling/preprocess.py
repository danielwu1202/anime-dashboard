import nltk
import gensim
from nltk.tag import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from gensim.models.phrases import Phraser, Phrases

nltk.download('omw-1.4')
stop_words = stopwords.words('english')

pos_code = {
    'NNS': 'n', # 複數名詞
    'VBD':'v',  # 過去式動詞
    'VBG': 'v', # 現在分詞
    'VBN': 'v', # 物去分詞
    'VBZ': 'v', # 動詞(第三人稱)
    'VBP': 'v', # 現在式動詞
    'VB' : 'v', # 動詞
    'NN': 'n', # 名詞
    'JJ': 'a', # 形容詞
    'RB': 'r' # 副詞
            }


def LDA_pipeline(data, column='Synopsis', needed_pos=()):
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
            if t[1] in needed_pos:
                temp.append(wnl.lemmatize(t[0], pos = pos_code[t[1]]))
        lemmed_token.append(temp)

    # TODO 形成bigram、trigram的threshold和min_count
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
