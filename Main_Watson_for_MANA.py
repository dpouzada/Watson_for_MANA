#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#!/usr/bin/env py -W ignore::DeprecationWarning
"""
@author: Daniel Pouzada, IBM Watson Tech Sales Junior
"""
#Importation des modules nécessaires par la suite

import ibm_watson
import Instances_Watson_modules

naturalLanguageUnderstanding=Instances_Watson_modules.naturalLanguageUnderstanding
assistant=Instances_Watson_modules.assistant
natural_language_classifier=Instances_Watson_modules.natural_language_classifier
language_translator=Instances_Watson_modules.language_translator
workspace_id_assistant=Instances_Watson_modules.workspace_id_assistant

from ibm_watson.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions, ConceptsOptions, SentimentOptions, EmotionOptions
    
import xlrd 

import atexit
import signal
import csv

from collections import Counter 
import time

import os

from Functions_Watson_for_MANA import input_file_to_treat_with_cells
from Functions_Watson_for_MANA import identification_language_and_translation
from Functions_Watson_for_MANA import prospection_nlu
from Functions_Watson_for_MANA import setting_supervision
from Functions_Watson_for_MANA import manage_confirmed_intent
from Functions_Watson_for_MANA import train_intent
from Functions_Watson_for_MANA import confirmation_MANA_sentence
from Functions_Watson_for_MANA import fill_dictionary
from Functions_Watson_for_MANA import train_3rd_layer_NLC
from Functions_Watson_for_MANA import register_file_Oui_MANA
from Functions_Watson_for_MANA import print_results_of_this_execution

print("All modules were imported and Watson instances were created\n")

print("The excel file names in the current directory that you might feed as an input are:\n")
directory = os.listdir('.')
for file in directory:
    if ".xls" in file:
        print(file)
        
Prospection=input("\n Do you want to do a prospection of the keywords recognized by NLU of some articles so that you can prepare/adjust the detecting entities of the chatbot ? Type exactly \'Yes\' if that is the case, otherwise press any other key\n")
if Prospection=="Yes":
    prospection_list_keywords=prospection_nlu()  
    print("For your information (if you want to manually adjust the entities of the chatbot): the most common keywords returned by NLU on the list of articles that just displayed on the screen are given by the following array:", prospection_list_keywords,"\n")       
else:
    print("Alright no prospection was done.\n")
 
csv.register_dialect('myDialect', delimiter = '/', quoting=csv.QUOTE_ALL)
    
if os.path.isfile('Oui_MANA_articles.tsv')==False:
    #initialisation de la liste contenant les articles traités
    list_already_treated_MANA_articles=[]
    for i in range(4):
        initialisation_dictionary={}
        initialisation_dictionary["keyword(s)"]="initialisation_%d"%i,
        initialisation_dictionary["flag"]=str(i)
        initialisation_dictionary["sentence(s)"]="This is a happy initialisation"
        initialisation_dictionary["text"]="This is a happy initialisation"
        initialisation_dictionary["company"]="random company"
        initialisation_dictionary["joy"]=1
        initialisation_dictionary["anger"]=0
        initialisation_dictionary["disgust"]=0
        initialisation_dictionary["sadness"]=0
        initialisation_dictionary["sentiment"]=1
        initialisation_dictionary["total_sentiment"]=2
        initialisation_dictionary["counter_mana_sentences"]=0
        #print(initialisation_dictionary)
        list_already_treated_MANA_articles.append(initialisation_dictionary)
    list_already_treated_MANA_articles=list_already_treated_MANA_articles[1:]+list_already_treated_MANA_articles[0:1]
        
    with open('Oui_MANA_articles.tsv', 'w+') as csvfile:
        fieldnames = ["flag","company","counter_mana_sentences","keyword(s)","sentence(s)","text","sentiment","sadness","disgust","anger","joy","total_sentiment"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect="myDialect")
        writer.writeheader()
        writer.writerows(list_already_treated_MANA_articles)
    print("File storing Oui MANA articles was created and initialised\n")


list_already_treated_MANA_articles=[]

with open('Oui_MANA_articles.tsv', encoding="utf8", errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='/')
    line_count = 0
    for row in csv_reader:
        if line_count!=0 and row!=[]:
            initialisation_dictionary={}
            initialisation_dictionary["flag"]=int(row[0])
            initialisation_dictionary["company"]=row[1]
            initialisation_dictionary["counter_mana_sentences"]=int(row[2])
            initialisation_dictionary["keyword(s)"]=row[3]        
            initialisation_dictionary["sentence(s)"]=row[4]
            initialisation_dictionary["text"]=row[5]
            initialisation_dictionary["total_sentiment"]=float(row[11])
            initialisation_dictionary["joy"]=row[10]
            initialisation_dictionary["anger"]=row[9]
            initialisation_dictionary["disgust"]=row[8]
            initialisation_dictionary["sadness"]=row[7]
            initialisation_dictionary["sentiment"]=row[6]
            list_already_treated_MANA_articles.append(initialisation_dictionary)
        line_count+=1

print("Already classified MANA articles were loaded.")

if os.path.isfile('Non_MANA_articles.tsv')==False:
    with open('Non_MANA_articles.tsv', 'w+') as csvfile:
        fieldnames = ["flag","company","keyword(s)","text","sentiment","sadness","disgust","anger","joy","total_sentiment"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect="myDialect")
        writer.writeheader()
    print("File storing Non MANA articles was created and initialised\n")

#register_file_Oui_MANA()
        
atexit.register(register_file_Oui_MANA,list_already_treated_MANA_articles)
signal.signal(signal.SIGTERM, register_file_Oui_MANA)
signal.signal(signal.SIGINT, register_file_Oui_MANA)

classifiers = natural_language_classifier.list_classifiers().get_result()
if classifiers["classifiers"]==[]:
    train_3rd_layer_NLC(assistant, natural_language_classifier, list_already_treated_MANA_articles)

atexit.register(train_3rd_layer_NLC,assistant, natural_language_classifier, list_already_treated_MANA_articles)


# Pathname of the file we want to treat            
#namefile_to_treat='file_articles_copie.xls'
#namefile_to_treat='test_IA_9_01_19.xlsx'

namefile_to_treat, sheet, Line_of_first_article_to_be_treated_in_the_excel_file, Line_of_last_article_to_be_treated_in_the_excel_file=input_file_to_treat_with_cells()
ask_for_Confirmation,ask_for_mana_alert,ask_for_deceitful_alert,ask_for_Training_intent,ask_for_NLC,ask_for_save_MANA_article,ask_for_Save_Non_MANA=setting_supervision(namefile_to_treat)
#ask_for_Confirmation,ask_for_mana_alert,ask_for_deceitful_alert,ask_for_Training_intent,ask_for_NLC,ask_for_save_MANA_article,ask_for_Save_Non_MANA=["N","N","N","N","N","N","N"]

#counter_well_recognized_articles_during_this_execution=0
#counter_treated_articles_during_this_execution=0
vector_counters=[0,0]
position_in_the_input_file_of_misclassified_articles=[]
list_confirmed_MANA_keywords=[]

atexit.register(print_results_of_this_execution,vector_counters=vector_counters,position_in_the_input_file_of_misclassified_articles=position_in_the_input_file_of_misclassified_articles,list_confirmed_MANA_keywords=list_confirmed_MANA_keywords)
signal.signal(signal.SIGTERM, print_results_of_this_execution)
signal.signal(signal.SIGINT, print_results_of_this_execution)    

number_keywords_considered=input("How many keywords do you want to consider from NLU?\n")
while number_keywords_considered.isdigit()==False:
    number_keywords_considered=input("This was not a number. Please type a digit?\n")
number_keywords_considered=int(number_keywords_considered)

ask_for_changing_supervision=input("Do you want to be asked before treating each new article whether to change the supervision settings ? Type Y or N\n")

# Treatment of the articles starts. It will loop through the cells of the excel file.
for text_index in range(Line_of_first_article_to_be_treated_in_the_excel_file, Line_of_last_article_to_be_treated_in_the_excel_file+1):
    
    print("\n Article number %d in the file about to be treated\n"%text_index)
    if ask_for_changing_supervision!='N':
        supervision=input("If you want to go through the supervision settings, type C (for Change settings), otherwise press any other key, e.g. Enter\n")
        if supervision=="C":
            ask_for_Confirmation,ask_for_mana_alert,ask_for_deceitful_alert,ask_for_Training_intent,ask_for_NLC,ask_for_save_MANA_article,ask_for_Save_Non_MANA=setting_supervision(namefile_to_treat)

    # On amorçe la lecture du fichier excel    
    print("Analysis of text number %d is starting. \n"%text_index)
    text=sheet.cell_value(text_index, 0).replace("\n","")
    text=identification_language_and_translation(text)
    expected_result_classification=sheet.cell_value(text_index, 1)
    
    # On envoie le texte à NLU                    
    response_nlu = naturalLanguageUnderstanding.analyze(
        text=text,
        features=Features(
            concepts=ConceptsOptions(limit=5),
            entities=EntitiesOptions(emotion=True, sentiment=True),
            keywords=KeywordsOptions(emotion=True, sentiment=True),   
            sentiment=SentimentOptions(document=True),  
            emotion=EmotionOptions(document=True)                                  
            )
        ).get_result()
    print("Article has been processed by NLU. \n")
    
    # Le premier critère est que l'article parle d'une entité "Company". On boucle donc sur les entités reconnues par NLU
    company=""
    i=0    
    while (i<len(response_nlu["entities"]) and company==""):
        if(response_nlu["entities"][i]["type"]=="Company"):
            company=response_nlu["entities"][i]["text"]
        i+=1
    # La company avec le plus grand score de confiance est la seule stockée.
    print("The company named %s was detected as an entity mentioned in the article. \n"%company)
    
    # On collecte et stocke les valeurs des sentiments et émotions de l'article
    sentiment=response_nlu["sentiment"]["document"]["score"]
    emotion_json_pointer=response_nlu["emotion"]["document"]["emotion"]
    sadness=emotion_json_pointer["sadness"]
    joy=emotion_json_pointer["joy"]
    disgust=emotion_json_pointer["disgust"]
    anger=emotion_json_pointer["anger"]
    print("The overall sentiment of the article is %f. \n"%sentiment)
    print("The emotions scores of the article are: sadness=%f, joy=%f, disgust=%f, anger=%f. \n"%(joy,sadness, disgust, anger))
    # Cette formule de score pondere est arbitraire
    score_pondere=-0.5*(anger+disgust+sadness-joy)+sentiment
    print("Hence the weighted average score -0.5*(anger+disgust+sadness-joy)+sentiment is equal to %f. \n"%score_pondere)
    
    flag_article_retained=0
    dictionary_article={}
    
    if (company!="" and score_pondere<0.5):
        print("The successful detection of company and weighted average score < 0.5 allows further analysis of this article. \n") 
        # We initialize the flag which will store the information on which layer of the classifier has detected the article
        # We initialize the list of keywords, the dictionary which will store the data on the article after processing and the counter to count how many entities were detected (to further place the article in list_already_treated_MANA_articles by its relevance)
        counter_confirmed_mana_sentence=0
        list_entities_already_confirmed=[]
        
        keywords_list=[]
        for l in range(number_keywords_considered):
        #for l in range(len(response_nlu["keywords"])):
            keywords_list.append(response_nlu["keywords"][l]["text"]) 
        #print("All keywords were stored in keywords_list. \n")

        for keyword in keywords_list:
            #print('#', end='', flush=True)
            print("keyword sent from NLU (to the chatbot):%s"%keyword)
            response_bot = assistant.message(
                workspace_id=workspace_id_assistant,
                input={
                    'text': keyword
                }
            ).get_result()
            # If the bot has recognized either an alerting entity or the intent Oui_MANA or Non_MANA then the answer is different that the anything else node with text: 'No redhibitory word detected'
            if response_bot["output"]["text"]!=['No redhibitory word detected']:
                #keyword_sentences_list=[]
                print("\n")
                for sentence_keyword in text.split('.'): 
                    if keyword in sentence_keyword:
                        #keyword_sentences_list.append(sentence)
                
                        # If an alerting entity was discovered, meaning it is not one of the intents by elimination
                        if response_bot["output"]["text"]!=['OuiMANA'] and response_bot["output"]["text"]!=['NonMANA']:
                            # Watson Assistant forces us to use the following little trick to catch the exact synonym of entity value that was detected in the input keyword
                            position_alerting_entity=response_bot['entities'][0]['location']
                            alerting_entity=response_bot['input']['text'][position_alerting_entity[0]:position_alerting_entity[1]]
                            if ask_for_Confirmation=="N":
                                print("A new alerting entity was detected: \"%s\" \n"%alerting_entity)  
                                Confirmation="Y"
                            elif alerting_entity not in list_entities_already_confirmed:
                                Confirmation=input("The new alerting entity was detected: \"%s\".\nDo you confirm it is correct to be detecting this entity ? Type Y or N\n"%alerting_entity)
                            else: 
                                print("The entity \"%s\" was detected, but you already confirmed it was correct to detect it. \n"%alerting_entity)
                                Confirmation="Y"
                            # Having collected the sentences in which this entity appears, we now send them back to the bot, whose nodes were placed with a jump to the nodes of the intents to check whether the sentences trigger the Oui_MANA or Non_MANA intent
                            if Confirmation=="Y": 
                                list_entities_already_confirmed.append(alerting_entity)
                                counter_confirmed_mana_sentence,flag_article_retained=confirmation_MANA_sentence(counter_confirmed_mana_sentence,flag_article_retained,keyword,sentence_keyword,ask_for_mana_alert,assistant,response_bot,dictionary_article,list_confirmed_MANA_keywords,ask_for_Training_intent,ask_for_deceitful_alert)
                            elif Confirmation=="N":
                                    print("Then we suggest that you manually correct the entity through the chatbot user interface. \n")
                                    
                        # It is possible that no alerting entity was detected but that the keyword triggered the intent of the bot
                        # Hence it might be a less evident, more subtle MANA phrase with no "redhibitory words" 
                        else:
                            print("Oui_MANA intent was triggered WITHOUT alerting entities by the keyword:\"%s\". \n"%keyword)
                            counter_confirmed_mana_sentence,flag_article_retained=confirmation_MANA_sentence(counter_confirmed_mana_sentence,flag_article_retained,keyword,sentence_keyword,ask_for_mana_alert,assistant,response_bot,dictionary_article,list_confirmed_MANA_keywords,ask_for_Training_intent,ask_for_deceitful_alert)
        
        # If the article passed the Chatbot, then the flag is still 0 and we can send the full article to the 3rd layer NLC
        #if flag_article_retained==0:
        if ask_for_NLC=="N":
            NLC="Y"
        else:
            NLC=input("No MANA alert was detected by the chatbot. Do you want to ask to 3rd layer NLC ? Type Y or N\n")
        if NLC=="Y": 
            classifiers = natural_language_classifier.list_classifiers().get_result()
            print("\n We are sending the following text to the 3rd layer external NLC:\n %s \n"%text[0:2045])
            response_nlc = natural_language_classifier.classify(classifiers["classifiers"][-1]["classifier_id"],text[0:2045]).get_result()
            print("The entire article was sent to the 3rd layer external NLC. \n")
            # The flag value of 3 stands for 3rd layer
            if response_nlc['top_class']=="Oui_MANA":
                print("This article was classified as a Oui_MANA article by by the 3rd layer NLC. \n")
                if flag_article_retained==0:
                    if expected_result_classification==1:
                        flag_article_retained=3
#                    ask_for_confirmation_3rd_layer_NLC=input("Yet the chatbot had not recognized any alerting entity or triggered Oui_MANA intent. Do you still want to trust the 3rd layer NLC classification by placing this article in the list of MANA articles ? Type Y or N \n")
#                    if ask_for_confirmation_3rd_layer_NLC=="Y":
#                        flag_article_retained=3
                else:
                    print("The 3rd layer NLC classification corresponds to the previous analysis by the chatbot.\n")
            elif response_nlc['top_class']=="Non_MANA":
                print("This article was considered as a Non_MANA article by the 3rd layer NLC. \n")
                if expected_result_classification==1:
                    print("The 3rd layer NLC result is wrong.\n")
            else:
                print("There was a problem with the NLC classification. \n")
        else: 
            print("The article was not sent to the 3rd layer external NLC. \n") 
        
        # If the article was retained by one layer, i.e. that the flag value is not 0, we store all its information
                    

    else:
        print("The unsuccessful detection of company or weighted average score > 0.5 discards further analysis of this article. \n")

    if flag_article_retained!=0:
        fill_dictionary(dictionary_article,text,company,joy,anger,disgust,sadness,sentiment,score_pondere,counter_confirmed_mana_sentence,flag_article_retained)
        print("All of the relevant information in the article was stored. \n")
        
        if (ask_for_save_MANA_article=="N"):
            Add_article_to_list="Y"
        else:
            Add_article_to_list=input("This article was identified as relevant for MANA by the layer number %d. Do you confirm you want to add this article to the list of MANA articles ? Type Y or N\n"%flag_article_retained)
        if Add_article_to_list=="Y":
            print("We will now place the article according to: (1) the number of confirmed MANA sentences, (2) the weighted average score \n")
            # If flag=1, we start comparing its "relevance score" to other elements of the list (to sort it) by the beginning of the list, as it is shorter
            if flag_article_retained==1:
                index_to_place_article=0
                while (counter_confirmed_mana_sentence<list_already_treated_MANA_articles[index_to_place_article]["counter_mana_sentences"]):
                    index_to_place_article+=1
                while (score_pondere>list_already_treated_MANA_articles[index_to_place_article]["total_sentiment"]
                and counter_confirmed_mana_sentence==list_already_treated_MANA_articles[index_to_place_article]["counter_mana_sentences"]):
                    index_to_place_article+=1
            
            length_list=len(list_already_treated_MANA_articles)
            
            if flag_article_retained==3:
                
                index_to_place_article=length_list
                #while (list_already_treated_MANA_articles[index_to_place_article-1]["flag"]!=3):
                #    index_to_place_article-=1
                while (score_pondere<list_already_treated_MANA_articles[index_to_place_article-1]["total_sentiment"]
                and list_already_treated_MANA_articles[index_to_place_article-1]["flag"]==3):
                        index_to_place_article-=1                      
            
            if (index_to_place_article<=length_list 
                and index_to_place_article>=0
                and list_already_treated_MANA_articles[index_to_place_article]["text"]!=dictionary_article["text"]
                and list_already_treated_MANA_articles[index_to_place_article-1]["text"]!=dictionary_article["text"]
                and list_already_treated_MANA_articles[index_to_place_article+1]["text"]!=dictionary_article["text"]):
                list_already_treated_MANA_articles.insert(index_to_place_article,dictionary_article)
                print("The article was placed in the list_already_treated_MANA_articles at position %d on the list of already treated articles containing %d articles for the moment.\n"%(index_to_place_article+1,length_list))
            else:
                print("This article had already been treated and registered, and was therefore not added now\n")

#                with open('Oui_MANA_articles.tsv', 'w+') as csvfile:
#                    fieldnames = ["flag","company","counter_mana_sentences","keyword(s)","sentence(s)","text","sentiment","sadness","disgust","anger","joy","total_sentiment"]
#                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect="myDialect")
#                    writer.writeheader()
#                    writer.writerows(list_already_treated_MANA_articles)
    else: 
        if ask_for_Save_Non_MANA=="N":
            Save_Non_MANA="Y"
        else:                     
            Save_Non_MANA=input("Do you want to save the content of this article which has sentiment/emotions score of %f at the end of the list_already_treated_MANA_articles to later train the 3rd layer NLC ? Type Y or N\n"%score_pondere)
        if Save_Non_MANA=="Y":
            fill_dictionary(dictionary_article,text,company,joy,anger,disgust,sadness,sentiment,score_pondere,counter_confirmed_mana_sentence,flag_article_retained)

            with open('Non_MANA_articles.tsv', 'a') as csvfile:
                fieldnames = ["flag","company","keyword(s)","text","sentiment","sadness","disgust","anger","joy","total_sentiment"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect="myDialect")
                #writer.writeheader()
                writer.writerows([dictionary_article])
                
    #counter_treated_articles_during_this_execution+=1
    vector_counters[0]+=1
    if (flag_article_retained!=0 and expected_result_classification!=0):
        #counter_well_recognized_articles_during_this_execution+=1
        vector_counters[1]+=1
        print("Result: Article well recognized by the classifier as a MANA article (compared to expectations). \n")
    elif (flag_article_retained==0 and expected_result_classification==0):
        #counter_well_recognized_articles_during_this_execution+=1
        vector_counters[1]+=1
        print("Result: Article well recognized by the classifier as a NON MANA article (compared to expectations). \n")
    else:
        position_in_the_input_file_of_misclassified_articles.append([text_index,text[0:30]])
        print("Result: there is a difference between expectations and classification for the article number %d in the file.\n"%text_index)

