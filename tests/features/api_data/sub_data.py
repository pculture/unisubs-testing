#!/usr/bin/env python
from lettuce import *
import json
import glob
import os

class SubData():

    _DATA_DIR = os.path.join(os.getcwd(), 'features', 'api_data')
    """
    Make some sense of the json subs data.
    """

    def list_of_translations(self, directory):
        lang_list = []
        for f in glob.glob(os.path.join(self._DATA_DIR, directory, '*.json')):
            base = os.path.basename(f)
            if 'metadata' not in base:
                lang =  self.language_maps(os.path.splitext(base)[0].split('-')[1])
                if not lang == None:
                    lang_list.append([f, lang])
        return lang_list

    def pull_sub_strings_from_data(self, json_file):
        """create a list of the sub time and subtitle line pairs and return it.

        """
        lang_subs = {} 
        json_data=open(os.path.join(self._DATA_DIR, json_file))
        data = json.load(json_data)
        for sub in data['captions']:
            sub_text = sub['content']
            sub_time = int(sub['startTime'])/1000
            lang_subs[str(sub_time)+'.0'] =  sub_text
        json_data.close()
        return lang_subs

    def language_maps(self, code):
        lang_map = {
        "ara": "Arabic",
        "bul": "Bulgarian",
        "ger": "German",
        "gre": "Greek",
        "hin": "Hebrew",
        "hun": "Hungarian",
        "ita": "Italian",
        "jpn": "Japanese",
        "mac": "Macedonian",
        "por_br": "Brazilian Portuguese",
        "scr": "Croatian",
        "spa": "Spanish",
        "tur": "Turkish",
        }     
        try:
            return lang_map[code]  
        except:
            return None
