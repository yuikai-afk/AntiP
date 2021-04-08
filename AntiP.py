#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
import docx2txt
import re
from os import listdir
from os.path import isfile, join


# In[2]:


path = './AntiP/'
files = [f for f in listdir(path) if isfile(join(path, f))]


# In[4]:


for doc_name in files:
    if doc_name.lower().endswith('.docx'):
        fulltext = docx2txt.process(path+doc_name)
        fulltext = '\n'.join(fulltext)
        text = re.sub(r'[a-zA-Z]', '', fulltext)[0:15000]
        print(doc_name)
        print(len(text))
        break


# In[5]:


text


# In[6]:


try:
    request = {
        'key': 'C9tn8XPpkBO8EpG',
        #'method':  'get_packages_info',
        #'visible': 'vis_on',
        'text': text
    }
    response = requests.post('https://content-watch.ru/public/api/', data = request).json()
    #print(response)
    # Будет выведено:
    # {u'size': 24698146}
except requests.exceptions.RequestException as ex:
    print('ERROR: %s' % ex)


# In[7]:


number = response['percent']
print('Уникальность текста: ', number, '%')


# In[ ]:




