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