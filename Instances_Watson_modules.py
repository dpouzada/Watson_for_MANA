# -*- coding: utf-8 -*-
"""
@author: Daniel Pouzada, IBM Watson Tech Sales Junior
"""

import ibm_watson

#Importation modules NLU
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions, ConceptsOptions, SentimentOptions, EmotionOptions

# Appel de l'instance NLU
naturalLanguageUnderstanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='xxx',
    url='https://gateway-fra.watsonplatform.net/natural-language-understanding/api'
)

#Appel de l'instance Chatbot (Assistant)
assistant = ibm_watson.AssistantV1(
    iam_apikey='xxx',
    version='2018-09-20',
    url='https://gateway-fra.watsonplatform.net/assistant/api'
)

#Importation modules NLC
from ibm_watson import NaturalLanguageClassifierV1

# Appel de l'instance NLC
natural_language_classifier = NaturalLanguageClassifierV1(
    iam_apikey='xxx',
    url='https://gateway-fra.watsonplatform.net/natural-language-classifier/api')

#Importation modules Translator
from ibm_watson import LanguageTranslatorV3

# Appel de l'instance Translator
language_translator = LanguageTranslatorV3(
version='2018-05-01',
url='https://gateway-fra.watsonplatform.net/language-translator/api',
iam_apikey='xxx'
)

workspace_id_assistant='xxx'
