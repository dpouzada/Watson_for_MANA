# -*- coding: utf-8 -*-
"""
@author: Daniel Pouzada, IBM Watson Tech Sales Junior
"""
import watson_developer_cloud

#Importation modules NLU
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions, ConceptsOptions, SentimentOptions, EmotionOptions

# Appel de l'instance NLU
naturalLanguageUnderstanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='7gen9EnMgYzzGQG7LGy9tVehlHDOihV5Msps1QXriKNC',
    #username='5ef6c23e-557c-45a1-ba3a-d7485a76e239',
    #password='NXYn5uS8nncC',
    #url='https://gateway.watsonplatform.net/natural-language-understanding/api'
    url='https://gateway-fra.watsonplatform.net/natural-language-understanding/api'
)

#Appel de l'instance Chatbot (Assistant)
assistant = watson_developer_cloud.AssistantV1(
    iam_apikey='fyWsqceWTmKH2wsNbKy7EjXwVcswoFeL4-4iFSsxLVmc',
    version='2018-09-20',
    url='https://gateway-fra.watsonplatform.net/assistant/api'
)

#Importation modules NLC
from watson_developer_cloud import NaturalLanguageClassifierV1

# Appel de l'instance NLC
natural_language_classifier = NaturalLanguageClassifierV1(
    iam_apikey='4n6XwggNiNH5MWpl11KgJ6fEX7rM72IPL0EZTCPtw0z7',
    url='https://gateway-fra.watsonplatform.net/natural-language-classifier/api')

#Importation modules Translator
from watson_developer_cloud import LanguageTranslatorV3

# Appel de l'instance Translator
language_translator = LanguageTranslatorV3(
version='2018-05-01',
#url='https://gateway.watsonplatform.net/language-translator/api',
#username='364d8460-a47e-466f-8878-9f1fc9ae0c34',
url='https://gateway-fra.watsonplatform.net/language-translator/api',
iam_apikey='ebZ9mgYgdiRd0-zv7hm2e_yxQma20ypX55xJS4ZPaJZg'
)

workspace_id_assistant='6d7f9feb-3d05-4c0e-82b5-6c509638648c'
