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
    iam_apikey='yFVW0tXh8_yT4U75Mho6vLkP0nVEI1H-S4G8iic5aJ5i',
    url='https://gateway-fra.watsonplatform.net/natural-language-understanding/api'
)

#Appel de l'instance Chatbot (Assistant)
assistant = ibm_watson.AssistantV1(
    iam_apikey='WLskhWCSWigQdpEOoPRZUkH6Fz1cF8mcB9kb4sgS4DYK',
    version='2018-09-20',
    url='https://gateway-fra.watsonplatform.net/assistant/api'
)

#Importation modules NLC
from ibm_watson import NaturalLanguageClassifierV1

# Appel de l'instance NLC
natural_language_classifier = NaturalLanguageClassifierV1(
    iam_apikey='4n6XwggNiNH5MWpl11KgJ6fEX7rM72IPL0EZTCPtw0z7',
    url='https://gateway-fra.watsonplatform.net/natural-language-classifier/api')

#Importation modules Translator
from ibm_watson import LanguageTranslatorV3

# Appel de l'instance Translator
language_translator = LanguageTranslatorV3(
version='2018-05-01',
url='https://gateway-fra.watsonplatform.net/language-translator/api',
iam_apikey='6TQOpf3QV-u1dRw0j5wEVZH60ifA46mvTImkuYyEFYhG'
)

workspace_id_assistant='6753a67d-ae39-4ef5-be4e-751e35aab09e'
