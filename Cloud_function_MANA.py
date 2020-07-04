#
#
# main() will be invoked when you Run This Action.
#
# @param Cloud Functions actions accept a single parameter,
#        which must be a JSON object.
#
# @return which must be a JSON object.
#         It will be the output of this action.
#
#
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import watson_developer_cloud

#Importation modules NLU
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions, ConceptsOptions, SentimentOptions, EmotionOptions

apikeyNLU='xxx'
apikeyAssistant='xxx'
workspaceid='xxx'
apikeyNLC='xxx'

# Appel de l'instance NLU
naturalLanguageUnderstanding = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey=apikeyNLU,
    url='https://gateway-fra.watsonplatform.net/natural-language-understanding/api'
)

#Appel de l'instance Chatbot (Assistant)

assistant = watson_developer_cloud.AssistantV1(
    iam_apikey=apikeyAssistant,
    version='2018-09-20',
    url='https://gateway-fra.watsonplatform.net/assistant/api'
)

#Importation modules NLC
from watson_developer_cloud import NaturalLanguageClassifierV1

# Appel de l'instance NLC
natural_language_classifier = NaturalLanguageClassifierV1(
    iam_apikey=apikeyNLC,
    url='https://gateway-fra.watsonplatform.net/natural-language-classifier/api')

def main(params):

    text=params['text'].replace("\n","")
    # On envoie le texte à NLU                    
    response_nlu = naturalLanguageUnderstanding.analyze(
        text=text,
        features=Features(
            concepts=ConceptsOptions(limit=5),
            entities=EntitiesOptions(emotion=True, sentiment=True),
            keywords=KeywordsOptions(emotion=True, sentiment=True),   
            sentiment=SentimentOptions(document=True),  
            emotion=EmotionOptions(document=True),
            ),
        language = 'en'
        ).get_result()
    
    # Le premier critère est que l'article parle d'une entité "Company". On boucle donc sur les entités reconnues par NLU
    company=""
    location=""
    i=0    
    while (i<len(response_nlu["entities"]) and (company=="" or location=="")):
        if(response_nlu["entities"][i]["type"]=="Company" and company==""):
            company=response_nlu["entities"][i]["text"]
            sentiment=response_nlu["entities"][i]["sentiment"]["score"]
            emotion_json_pointer=response_nlu["entities"][i]["emotion"]
            sadness=emotion_json_pointer["sadness"]
            joy=emotion_json_pointer["joy"]
            disgust=emotion_json_pointer["disgust"]
            anger=emotion_json_pointer["anger"]
            score_pondere_company=-0.5*(anger+disgust+sadness-joy)+sentiment
        if(response_nlu["entities"][i]["type"]=="Location" and location==""):
            location=response_nlu["entities"][i]["text"]
        i+=1
    
    # On collecte et stocke les valeurs des sentiments et émotions de l'article
    sentiment=response_nlu["sentiment"]["document"]["score"]
    emotion_json_pointer=response_nlu["emotion"]["document"]["emotion"]
    sadness=emotion_json_pointer["sadness"]
    joy=emotion_json_pointer["joy"]
    disgust=emotion_json_pointer["disgust"]
    anger=emotion_json_pointer["anger"]
    score_pondere=-0.5*(anger+disgust+sadness-joy)+sentiment
    

    if (company!="" and score_pondere<0.5):
        flag_article_retained=0
        # We initialize the list of keywords, the dictionary which will store the data on the article after processing and the counter to count how many entities were detected (to further place the article in list_already_treated_MANA_articles by its relevance)
        keywords_list=[]
        list_keywords_confirmed=[]
        list_alerting_entities_confirmed=[]
        list_sentences_confirmed=[]
        list_keywords_deceitful=[]
        #counter_confirmed_detected_alerting_entities=0
        
        for l in range(len(response_nlu["keywords"])):
            emotion_json_pointer=response_nlu["keywords"][l]["emotion"]
            sadness=emotion_json_pointer["sadness"]
            joy=emotion_json_pointer["joy"]
            disgust=emotion_json_pointer["disgust"]
            anger=emotion_json_pointer["anger"]
            sentiment=response_nlu["keywords"][l]["sentiment"]["score"]
            score_pondere_keyword=-0.5*(anger+disgust+sadness-joy)+sentiment
            keywords_list.append([response_nlu["keywords"][l]["text"],score_pondere_keyword]) 
        
        
        for keyword_data in keywords_list:
            keyword=keyword_data[0]
            response_bot = assistant.message(
                #workspace_id = 'a2dd5d22-63b4-4915-aac8-1c4f6fd358f6',
                workspace_id=workspaceid,
                input={
                    'text': keyword
                }
            ).get_result()
            # If the bot has recognized either an alerting entity or the intent Oui_MANA or Non_MANA then the answer is different that the anything else node with text: 'No redhibitory word detected'
            if response_bot["output"]["text"]!=['No redhibitory word detected']:
                if response_bot["output"]["text"]!=['OuiMANA'] and response_bot["output"]["text"]!=['NonMANA']:
                    position_alerting_entity=response_bot['entities'][0]['location']
                    alerting_entity=response_bot['input']['text'][position_alerting_entity[0]:position_alerting_entity[1]]
                    list_alerting_entities_confirmed.append(alerting_entity)                                    
                    #counter_confirmed_detected_alerting_entities+=1                
                for sentence_keyword in text.split('.'): 
                    if keyword in sentence_keyword:            
                        # If an alerting entity was discovered, meaning it is not one of the intents by elimination
                        #if response_bot["output"]["text"]!=['OuiMANA'] and response_bot["output"]["text"]!=['NonMANA']:
                            # We need the following little trick to catch the exact synonym of entity value that was detected in the input keyword
                            # Having collected the sentences in which this entity appears, we now send them back to the bot, whose nodes were placed with a jump to the nodes of the intents to check whether the sentences trigger the Oui_MANA or Non_MANA intent
                        confirmation_bot = assistant.message(
                                        workspace_id=workspaceid,
                                        input={
                                            'text': sentence_keyword
                                        },
                                        context=response_bot["context"]
                                    ).get_result()
                        if confirmation_bot["output"]["text"]==['OuiMANA']: 
                            # The value of the flag indicated that the 1st layer detected classified the article, i.e. an alerting entity was detected and its sentences were relevant for MANA
                            try:
                                assistant.create_example(
                                    workspace_id=workspaceid,
                                    intent='OuiMANA',
                                    text=sentence_keyword,
                                ).get_result()
                            except KeyboardInterrupt:
                                return 0
                            except:
                                pass 

                            flag_article_retained=1
                            list_keywords_confirmed.append(keyword_data)
                            list_sentences_confirmed.append(sentence_keyword)
 
                        elif confirmation_bot["output"]["text"]==['NonMANA']:
                            #if response_bot["output"]["text"]!=['OuiMANA'] and response_bot["output"]["text"]!=['NonMANA']:
                            try:
                                assistant.create_example(
                                    workspace_id=workspaceid,
                                    intent='NonMANA',
                                    text=sentence_keyword,
                                ).get_result()
                            except KeyboardInterrupt:
                                return 0
                            except:
                                pass
                            list_keywords_deceitful.append(keyword_data)
                        # It is possible that no alerting entity was detected but that the keyword triggered the intent of the bot
                        # Hence it might be a less evident, more subtle MANA phrase with no "redhibitory words", hence the flag value 2 for 2nd layer 
                        #(if the flag was not already set to 1 by the confirmation of a MANA alert detection)
                        #else:
                            #confirmation_MANA_sentence(keyword,sentence_keyword,assistant,response_bot,counter_confirmed_detected_alerting_entities,flag_article_retained)
        
        if flag_article_retained==0:
            classifiers = natural_language_classifier.list_classifiers().get_result()
            response_nlc = natural_language_classifier.classify(classifiers["classifiers"][-1]["classifier_id"],text[0:2045]).get_result()
            # The flag value of 3 stands for 3rd layer
            if response_nlc['top_class']=="Oui_MANA":
                flag_article_retained=3
    
    # If the article was retained by one layer, i.e. that the flag value is not 0, we store all its information
        article_highlighted=text
        if flag_article_retained!=0:
            score_keywords_confirmed = []
            
            list_sentences_confirmed=list(set(list_sentences_confirmed))
            count_sentences=len(list_sentences_confirmed)
            for sentence in list_sentences_confirmed:
                article_highlighted=article_highlighted.replace(sentence,'<mark style="background-color: yellow">'+sentence+'</mark>')
            
            for k in list_keywords_confirmed:
                score_keywords_confirmed=+k[1]
            
            list_all_keywords=list_keywords_confirmed+list_keywords_deceitful
            list_all_keywords=list(set(map(tuple,list_all_keywords)))
            for keyword_data in list_all_keywords:
                article_highlighted=article_highlighted.replace(keyword_data[0],'<mark style="background-color: orange">'+keyword_data[0]+"("+str(round(keyword_data[1],2))+")"+'</mark>')  
                
            list_alerting_entities_confirmed=list(set(list_alerting_entities_confirmed))
            for keyword in list_alerting_entities_confirmed:
                article_highlighted=article_highlighted.replace(keyword,'<mark style="background-color: red">'+keyword+'</mark>')
            
            article_highlighted=article_highlighted.replace('$','dollars')
            
            return {
            'flag':flag_article_retained,
            'location':location,
            'company':company,
            'score_company':score_pondere_company,
            'score':score_pondere,
            'count':count_sentences,
            'text':article_highlighted,
            'score_keywords_confirmed':score_keywords_confirmed
            }
        
        else: 
            list_keywords_deceitful=list(set(map(tuple,list_keywords_deceitful)))
            for keyword_data in list_keywords_deceitful:
                article_highlighted=article_highlighted.replace(keyword_data[0],'<mark style="background-color: orange">'+keyword_data[0]+"("+str(round(keyword_data[1],2))+")"+'</mark>')  
                            
            return {
            'flag':flag_article_retained,
            'location':location,
            'company':company,
            'score_company':score_pondere_company,
            'score':score_pondere,
            'count':0,
            'text':article_highlighted,
            'score_keywords_confirmed':0
            }
    
    else:
        return {
            'flag':'-1',
            'location':'0',
            'company':'0',
            'score_company':'0',
            'score':'0',
            'count':'0',
            'text':text,
            'score_keywords_confirmed':'0'
            }
