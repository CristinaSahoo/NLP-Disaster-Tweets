from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np

# input dataframe, output vectorized dataframe
def vectorize_df(df):
    cvec = CountVectorizer()
    cvec.fit(df['text']);
    term_mat = cvec.transform(df['text'])
    term_df = pd.DataFrame(term_mat.todense(), columns=cvec.get_feature_names())
    return term_df

# input sequence, output vectorized sequence of specified dimension, all 0s and 1s
def vectorize_sequence(sequences, dimension=10_000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1
    return results