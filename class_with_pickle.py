#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re
from pymorphy2 import MorphAnalyzer
import nltk
from nltk import sent_tokenize, word_tokenize, regexp_tokenize
from nltk.corpus import stopwords
from string import punctuation
import re
import pickle


# In[10]:


class Classification:
    def transform_df(df):
        df['Content'] = df['Content'].str.replace(r'<.*?>', ' ')
        df['Content'] = df['Content'].str.replace(r'\n',' ')
        df['Content'] = df['Content'].str.replace(r'[^А-Яа-я\s]',' ')
        df['Content'] = df['Content'].str.replace(r'\s+',' ')  
        return df
    def clean_df(main_df):
        nltk.data.path.append('./stopwords/')
        russian_stopwords = stopwords.words("russian")
        main_df['Content'] = main_df['Content'].map(lambda x: x.lower())
        main_df['Content'] = main_df['Content'].map(lambda x: x.split(' '))
        main_df['Content'] = main_df['Content'].map(lambda x: [token for token in x if token not in russian_stopwords                                                                  and token != " "                                                                   and token.strip() not in punctuation])
        main_df['Content'] = main_df['Content'].map(lambda x: ' '.join(x))

        def tokenize_n_normalize(sent, pat=r"(?u)\b\w\w+\b", morph=MorphAnalyzer()):
            return [morph.parse(tok)[0].normal_form 
                    for tok in regexp_tokenize(sent, pat)]
        main_df['Content'] = main_df['Content'].map(lambda x: " ".join(tokenize_n_normalize(x)))
        return main_df['Content']
    def result(text):
        loaded_model = pickle.load(open('classification_model.sav', 'rb'))
        dirty_df = pd.DataFrame({'Content' : [text], 'Рубрики' : ['no']})
        new_df = Classification.clean_df(Classification.transform_df(dirty_df))
        #print(new_df)
        return loaded_model.predict(new_df)[0]


# In[13]:


Classification.result(text)


# In[ ]:




