import string
import re
import nltk
import enchant

# remove numbers
def remove_numbers(text):
    return re.sub('\d+', '', text)

# lower case all letters
def lower_case(text):
    return text.lower()

# remove punctuation
def remove_punct(text):
    text = re.sub('\.', '\. ', text)
    text = re.sub(':', ': ', text)
    text  = "".join([char for char in text if char not in string.punctuation])
    text = re.sub('[0-9]+', '', text)
    return text

# tokenize text
def tokenize(text):
    text = re.split('\W+', text)
    return text

# remove stop words
def remove_stopwords(text):
    stopwords = nltk.corpus.stopwords.words('english')
    text = [word for word in text if word not in stopwords]
    return text

# only keep words that are successions of letters
def remove_bad_words(text):
    return ' '.join(re.findall('[a-z]+', text))

# only keep words in the English dictionary
def keep_dict_only(text):
    d = enchant.Dict("en_US")
    return ' '.join([word for word in str.split(text) if d.check(word)])

# input is a dataframe that has a 'text' column/feature
def process_text(df):
    df['text'] = df['text'].apply(lambda x: remove_numbers(x))
    df['text'] = df['text'].apply(lambda x: lower_case(x))
    df['text'] = df['text'].apply(lambda x: remove_punct(x))
    df['text'] = df['text'].apply(lambda x: tokenize(x))
    df['text'] = df['text'].apply(lambda x: remove_stopwords(x))
    df['text'] = df['text'].apply(lambda x: ' '.join(x))
    df['text'] = df['text'].apply(lambda x: remove_bad_words(x))
    df['text'] = df['text'].apply(lambda x: keep_dict_only(x))
    return df