# Natural Language Processing with Disaster Tweets  


### Contents:
- [Problem Statement](#Problem-Statement)
- [Data Dictionary](#Data-Dictionary)
- [Brief Summary of Analysis](#Brief-Summary-of-Analysis)
- [Abstract Summary](#Abstract-Summary)
- [Conclusions and Recommendations](#Conclusions-and-Recommendations)


## Problem Statement

Kaggle: In this competition, you’re challenged to build a machine learning model that predicts which Tweets are about real disasters and which one’s aren’t. You’ll have access to a dataset of 10,000 tweets that were hand classified. 


## Why is this important?

Twitter has become an important communication channel in times of emergency.
The ubiquitousness of smartphones enables people to announce an emergency they’re observing in real-time. Because of this, more agencies are interested in programatically monitoring Twitter (i.e. disaster relief organizations and news agencies).


## Data Dictionary

|Feature|Type|Description|
|---|---|---|
|id|int64|a unique identifier for each tweet|
|text|object|the text of the tweet|
|location|object|the location the tweet was sent from (may be blank)|
|keyword|object|a particular keyword from the tweet (may be blank)|
|target|int64|in train.csv only, this denotes whether a tweet is about a real disaster (1) or not (0)|


## Brief Summary of Analysis

Text text data was run through several cleanup functions to remove punctuation, numbers, misspelled words, stop words, etc. The cleaned data was then split into features and target, vectorized, and transformed into tensors/multidimensional arrays to be fed into the neural network model.

Word cloud representations for disaster tweets and tweets that do not report disasters:

<div>
    Not Disaster Tweets<br>
<img src="./images/train0_wordcloud.jpg" width="500"/>
    <br>
    Disaster Tweets<br>
<img src="./images/train1_wordcloud.jpg" width="500"/>
</div>

Baseline: .42  
Models used:  
- Sequential Neural Network with one Dense input layer, one Dense intermediate layer, and one Dense output layer. Each layer has 16 units. The activation function used was 'relu', and the output function was 'sigmoid'. Optimizer 'rmsprop', loss function 'binary crossentropy', and metric used 'accuracy'. This model scored .46.
- Multinomial Naive Bayes scored .46.

## Abstract Summary


Recommendations discussed include:



## Conclusions and Recommendations

**Conclusions:**  

(1) The Naive Bayes models performed best.  
(2) Neural Networks requires very large amounts of data, so they may not be the best option for working with this dataset.  


**Next steps:**  

Collect more data from Twitter.  
Deploy with Streamlit.


**Resources:**

(1) Deep Learning with Python, by Francois Chollet


**Data Sources:**  

(1) [Kaggle/Data for Everyone](https://www.kaggle.com/c/nlp-getting-started/overview)  