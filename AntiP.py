import requests

import re

from os import listdir

from os.path import isfile, join


class Antiplagiat:
      

    def Uniqueness(text):

        clean_text = re.sub(r'[a-zA-Z"\n"]', '', text)[0:15000]

        try:

            request = {

                'key': 'C9tn8XPpkBO8EpG',

                'text': clean_text

            }

            response = requests.post('https://content-watch.ru/public/api/', data = request).json()

        except requests.exceptions.RequestException as ex:

            print('ERROR: %s' % ex)
 
        return response['percent']

 