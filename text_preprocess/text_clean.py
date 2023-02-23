import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
stop = stopwords.words('english')

# 將文字轉換成小寫
def lowercase(textSeries):
    return textSeries.str.lower()

'''
def remove_punctuation(text, symbol):
    punct = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{}~'
    transtab = str.maketrans(dict.fromkeys(punct, ''))
    text = str(symbol).join(text.tolist()).translate(transtab).split(str(symbol))
    textSeries = pd.Series(text)
    return textSeries
'''
# 移除標點符號
def remove_punctuation(textSeries):
    return textSeries.str.replace(r'[^\w\s]+', '', regex=True)

# 移除數字
def remove_digits(textSeries):
    return textSeries.str.replace(r'\d+', '', regex=True)

# 斷詞
def tokenize(origin, column, textSeries):
    origin[column] = textSeries.apply(word_tokenize)

# 移除停用詞
# FIXME
def remove_stopwords(origin, column, textSeries):
    origin[column] = textSeries.apply(lambda t: [].append(w for w in t if w not in stop))

# 形成bi-gram和tri-gram

'''
for l in token:
    for s in l:
        if s in stop:
            l.remove(s)
'''

