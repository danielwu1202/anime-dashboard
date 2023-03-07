import gensim
from tqdm import tqdm
import matplotlib.pyplot as plt
import gensim.corpora as corpora
from gensim.models import CoherenceModel


# 建立LDA，並選擇coherence score最高的結果
def make_LDA(word_no_stopword, start, end, step):
    # 建立LDA模型
    id2word = corpora.Dictionary(word_no_stopword)
    corpus = [id2word.doc2bow(text) for text in word_no_stopword]

    coherence_score = []
    model_list = []

    for num_topic in tqdm(range(start, end, step)):
        lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=num_topic,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha='auto',
                                           per_word_topics=True)
        model_list.append(lda_model)
        coherence = CoherenceModel(model=lda_model, texts=word_no_stopword, dictionary=id2word, coherence='c_v')
        coherence_score.append(coherence.get_coherence())

    # 把coherence score視覺化
    plt.plot(range(start, end, step), coherence_score)
    plt.xlabel("Number of Topics")
    plt.ylabel("Coherence score")
    plt.legend(("coherence_score"), loc='best')
    plt.show()

    return max(coherence_score), model_list[coherence_score.index(max(coherence_score))]