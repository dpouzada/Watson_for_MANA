# -*- coding: utf-8 -*-
"""
@author: Daniel Pouzada, IBM Watson Tech Sales Junior
"""

#Importation des modules nécessaires par la suite
import xlrd 
import watson_developer_cloud

import csv

from collections import Counter 

import os
import time

import Instances_Watson_modules

naturalLanguageUnderstanding=Instances_Watson_modules.naturalLanguageUnderstanding
assistant=Instances_Watson_modules.assistant
natural_language_classifier=Instances_Watson_modules.natural_language_classifier
language_translator=Instances_Watson_modules.language_translator
workspace_id_assistant=Instances_Watson_modules.workspace_id_assistant

from watson_developer_cloud.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions, ConceptsOptions, SentimentOptions, EmotionOptions

def input_file_to_treat_with_cells():
    namefile_to_treat=input("Please type the precise name of the file containing the articles you want to treat\n")
    # We prepare the object sheet for reading the excel file
    flag_file_correct=0
    while (flag_file_correct==0):
        try:
            loc = (namefile_to_treat) 
            wb = xlrd.open_workbook(loc) 
            sheet = wb.sheet_by_index(0)
            flag_file_correct=1
        except:
            namefile_to_treat=input("The file was not found, check the name you entered and type it again now, there was certainly a mistake (do not forget to include the path!). \n")
    
    Line_of_first_article_to_be_treated_in_the_excel_file=int(input("Please type the number of the first cell in the file (containing the first article) you want to treat)\n"))
    Line_of_last_article_to_be_treated_in_the_excel_file=int(input("Please type the number of the last cell in the file (containing the last article) you want to treat)\n"))
    flag_lines_correct=0
    while (flag_lines_correct==0):
        try:
            test=sheet.cell_value(Line_of_first_article_to_be_treated_in_the_excel_file, 0)
            test=sheet.cell_value(Line_of_last_article_to_be_treated_in_the_excel_file, 0)
            flag_lines_correct=1
            print("Those lines seem to be correct (supposing the intermediate lines are filled). We will then treat the articles stored in the file %s from lines %d to %d\n"%(namefile_to_treat,Line_of_first_article_to_be_treated_in_the_excel_file,Line_of_last_article_to_be_treated_in_the_excel_file))
        except:
            print("Those lines were not correct. We will ask you to type them again.")
            Line_of_first_article_to_be_treated_in_the_excel_file=int(input("Please type the number of the first cell in the file (containing the first article) you want to treat)\n"))
            Line_of_last_article_to_be_treated_in_the_excel_file=int(input("Please type the number of the last cell in the file (containing the last article) you want to treat)\n"))
    return namefile_to_treat, sheet, Line_of_first_article_to_be_treated_in_the_excel_file, Line_of_last_article_to_be_treated_in_the_excel_file

def identification_language_and_translation(text):
    language = language_translator.identify(text).get_result()
    langue=language['languages'][0]['language']
    if (langue!='en'):
        if langue=='ht':
            langue='fr'
        try:
            text = language_translator.translate(text=text,model_id=langue+'-en').get_result()
            text=text['translations'][0]['translation']
            language = language_translator.identify(text).get_result()
            langue=language['languages'][0]['language']
            if (langue=='en'):
                print("Successful translation ! \n")
                return text
            else:
                print("Translation not successful. \n")
        except KeyboardInterrupt:
            print("Interrupted Manually \n")
        except:
            print("Problem with translation. \n")  
            pass
    else:
        print("Language of this article was identified by the translator as english. \n")
        return text
   
def prospection_nlu():
      
    namefile, sheet, Line_of_first_article_to_be_treated_in_the_excel_file, Line_of_last_article_to_be_treated_in_the_excel_file=input_file_to_treat_with_cells()
    list_occurences_keywords=[]
    list_all_keywords=[]
    list_occurences_keywords.append(["initialisation",1])
    for text_index in range(Line_of_first_article_to_be_treated_in_the_excel_file, Line_of_last_article_to_be_treated_in_the_excel_file+1):  
        print("\nArticle number %d in the file about to be prospected\n"%text_index)
        # On amorçe la lecture du fichier excel    
        print("Analysis of text number %d is starting. \n"%text_index)
        text=sheet.cell_value(text_index, 0).replace("\n","")
        text=identification_language_and_translation(text)
    
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
        for l in range(len(response_nlu["keywords"])):
            split_it=response_nlu["keywords"][l]["text"].split()
            for keyword in split_it:
                list_all_keywords.append(keyword)
#            Manual way of storing the list of already appeared keywords, but counter module does the same faster below
#            flag_keyword_already_appeared=0
#            index_already_stored_keywords=0
#            length=len(list_occurences_keywords)
#            while flag_keyword_already_appeared==0 and index_already_stored_keywords<length:
#                if response_nlu["keywords"][l]["text"]==list_occurences_keywords[index_already_stored_keywords][0]:
#                    list_occurences_keywords[index_already_stored_keywords][1]+=1
#                    flag_keyword_already_appeared=1
#                index_already_stored_keywords+=1
#            if flag_keyword_already_appeared==0:
#                list_occurences_keywords.append([response_nlu["keywords"][l]["text"],1])
    count_intermediate = Counter(map(str.lower,list_all_keywords))
    most_occur = count_intermediate.most_common(10) 
    
    return most_occur

def setting_supervision(namefile_to_treat):
    print("We will now ask you how supervised you want the analysis to be on the articles contained in the file %s. \n"%namefile_to_treat)
    ask_for_Confirmation=input("Do you want to be asked each time to confirm whether it is correct to be alerted by a specific entity or not ? Type Y or N\n")
    ask_for_mana_alert=input("Do you want to be asked to confirm whether a sentence was successfully classified as a OuiMANA. Type Y or N\n")
    ask_for_deceitful_alert=ask_for_mana_alert
    ask_for_Training_intent=input("Do you want to be asked each time whether a classified sentence should train the related class of the chatbot ? Type Y or N\n")
    ask_for_NLC=input("Do you want to be asked each time whether to ultimately send the article to the 3rd layer external NLC (if no alerting entity was detected) ? Type Y or N\n")
    ask_for_save_MANA_article=input("Do you want to be asked each time whether you want to save the article in the list of already saved MANA articles ? Type Y or N\n")
    ask_for_Save_Non_MANA=input("Do you want to be asked each time whether you want to save the content of the article for the NonMANA class to train the 3rd layer NLC ? Type Y or N\n")
    return ask_for_Confirmation,ask_for_mana_alert,ask_for_deceitful_alert,ask_for_Training_intent,ask_for_NLC,ask_for_save_MANA_article,ask_for_Save_Non_MANA

def manage_confirmed_intent(counter_confirmed_mana_sentence,flag_article_retained,dictionary_article,keyword,sentence_keyword,list_confirmed_MANA_keywords):
    list_confirmed_MANA_keywords.append(keyword)
    # The value of the flag indicated that the 1st layer detected classified the article, i.e. an alerting entity was detected and its sentences were relevant for MANA
    flag_article_retained=1
    # If dictionary was empty, we create it, if not (as other keywords were already detected in this same article), we add the new keywords
    if bool(dictionary_article)==False:
        dictionary_article["keyword(s)"]=keyword+';'
        dictionary_article["sentence(s)"]=sentence_keyword+';'
        dictionary_article["flag"]=1
        counter_confirmed_mana_sentence+=1
    else:
        dictionary_article["keyword(s)"]+=keyword+';'
        if sentence_keyword not in dictionary_article["sentence(s)"]:
            dictionary_article["sentence(s)"]+=sentence_keyword+';'
            counter_confirmed_mana_sentence+=1
        #dictionary_article["flag"]=1
    return counter_confirmed_mana_sentence,flag_article_retained

# Fonction qui entraîne la classe "class_name" du chatbot avec les phrases stockées dans sentences_string
# Selon que ask_for_Training_intent est Y (pour Yes) ou N (pour No), on demande à l'utilisateur de confirmer
def train_intent(sentences_string,class_name,assistant,ask_for_Training_intent): 
    if ask_for_Training_intent=="N":
       Training_intent="Y"
    else:                             
        Training_intent=input("Do you want to train the %s intent/class of the chatbot with those sentences ? Type Y or N\n"%class_name)
    if Training_intent=="Y":
        print("The order to train the intent/class %s of the chatbot with this sentence was sent. \n"%class_name)
        # Si l'example sentences_string existe déjà, l'appel à l'api chatbot renvoie un message d'erreur. D'où la structure try except
        try:
            assistant.create_example(
                workspace_id=workspace_id_assistant,
                intent=class_name,
                text=sentences_string,
            ).get_result()
            print("%s intent was trained: the sentence was added to its examples\n"%class_name)
        except KeyboardInterrupt:
            return 0
        except:
            print("The intent %s had already been previously trained with this example\n"%class_name)
            pass

def confirmation_MANA_sentence(counter_confirmed_mana_sentence,flag_article_retained,keyword,sentence_keyword,ask_for_mana_alert,assistant,response_bot,dictionary_article,list_confirmed_MANA_keywords,ask_for_Training_intent,ask_for_deceitful_alert):
    confirmation_bot = assistant.message(
                    workspace_id=workspace_id_assistant,
                    input={
                        'text': sentence_keyword
                    },
                    context=response_bot["context"]
                ).get_result()
    print("The full sentence in the text was just sent for classification to the nodes of the bot detecting classes Oui_MANA/Non_MANA. \n" )
    if confirmation_bot["output"]["text"]==['OuiMANA']:                                        
        if ask_for_mana_alert=="N":
            mana_alert="Y"
            print("Following sentence was recognized by the intent Oui_MANA: \n \"%s\". \n" %sentence_keyword)
        else:
            mana_alert=input("Following sentence was recognized by the intent OUI_MANA: \"%s\".\nDo you confirm ? Type Y or N\n" %sentence_keyword)
        if mana_alert=="Y":
            counter_confirmed_mana_sentence,flag_article_retained=manage_confirmed_intent(counter_confirmed_mana_sentence,flag_article_retained,dictionary_article,keyword,sentence_keyword,list_confirmed_MANA_keywords)
            print("Those sentences were kept as relevant for MANA, and the relative information was stored. \n")
            train_intent(sentence_keyword,'Oui_MANA',assistant,ask_for_Training_intent)
            return counter_confirmed_mana_sentence,flag_article_retained
        elif mana_alert=="N":
            print("Alright, we correct the mistake and do not retain this sentence as relevant for MANA. Instead we are training the Non_MANA intent with this deceitful sentence to help refine the classification model. You also might want to check whether this exaxt same sentence is present in the examples data of the Oui_MANA intent (from mistaken past training from the same article), and if that's the case remove it.\n")
            train_intent(sentence_keyword,'Non_MANA',assistant,ask_for_Training_intent)
            return counter_confirmed_mana_sentence,flag_article_retained
            
    elif confirmation_bot["output"]["text"]==['NonMANA']:
        if ask_for_deceitful_alert=="N":
            deceitful_alert="Y"
            print("Following sentence(s) were recognized by the intent Non_MANA (DECEITFUL): \n \"%s\". \n " %sentence_keyword)
        else:
            deceitful_alert=input("The following sentence was recognized by the intent NON_MANA: \"%s\".\n Do you confirm ? Type Y or N\n"%sentence_keyword)
        if deceitful_alert=="Y":
            train_intent(sentence_keyword,'Non_MANA',assistant,ask_for_Training_intent)
            return counter_confirmed_mana_sentence,flag_article_retained
        elif deceitful_alert=="N":
            counter_confirmed_mana_sentence,flag_article_retained=manage_confirmed_intent(counter_confirmed_mana_sentence,flag_article_retained,dictionary_article,keyword,sentence_keyword,list_confirmed_MANA_keywords)
            print("Alright, we corrected the mistake and retained this sentence as relevant for MANA. Instead we are training the Oui_MANA intent with this deceitful sentence to help refine the classification model.You also might want to check whether this exaxt same sentence is present in the examples data of the Oui_MANA intent (from mistaken past training from the same article), and if that's the case remove it. \n")
            train_intent(sentence_keyword,'Oui_MANA',assistant,ask_for_Training_intent)
            return counter_confirmed_mana_sentence,flag_article_retained                                        
        
    else:
        choose=input("The following sentence was not recognized by either intents Oui_MANA or Non_MANA, you need to choose which one it corresponds to: \n \"%s\" \n Type O or N for this sentence to be considered respectively as a OuiMANA or NonMANA sentence.\n" %sentence_keyword)
        if choose=='O':
            counter_confirmed_mana_sentence,flag_article_retained=manage_confirmed_intent(counter_confirmed_mana_sentence,flag_article_retained,dictionary_article,keyword,sentence_keyword,list_confirmed_MANA_keywords)
            print("This sentence was kept as relevant for MANA, and the relative information was stored. \n")
            train_intent(sentence_keyword,'Oui_MANA',assistant,ask_for_Training_intent)
            return counter_confirmed_mana_sentence,flag_article_retained
        if choose=='N':
            print("This sentence was not retained as relevant for MANA, but the intent NonMANA was trained. \n")
            train_intent(sentence_keyword,'Non_MANA',assistant,ask_for_Training_intent)
            return counter_confirmed_mana_sentence,flag_article_retained

def fill_dictionary(dictionary_article,text,company,joy,anger,disgust,sadness,sentiment,score_pondere,counter_confirmed_mana_sentence,flag_article_retained):
    dictionary_article["text"]=text
    dictionary_article["company"]=company
    dictionary_article["joy"]=str(joy)
    dictionary_article["anger"]=str(anger)
    dictionary_article["disgust"]=str(disgust)
    dictionary_article["sadness"]=str(sadness)
    dictionary_article["sentiment"]=str(sentiment)
    dictionary_article["total_sentiment"]=score_pondere
    if counter_confirmed_mana_sentence!=0:
        dictionary_article["counter_mana_sentences"]=counter_confirmed_mana_sentence
    if  flag_article_retained==0:           
        dictionary_article["keyword(s)"]="Non MANA article"
        dictionary_article["flag"]=0
    if flag_article_retained==3:
        dictionary_article["keyword(s)"]="NLC 3rd layer identified this article as relevant for MANA"
        dictionary_article["flag"]=3

# Function to collect all the content of both classes Oui_MANA and Non_MANA and update the classifier of 3rd layer external NLC.
def train_3rd_layer_NLC(assistant, natural_language_classifier, list_already_treated_MANA_articles):
    classifiers = natural_language_classifier.list_classifiers().get_result()
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
    if classifiers["classifiers"]!=[]:
        ask_for_training_NLC=input("The 3rd layer NLC was last trained on the date: %s. Training it with new data will cost you 2 euros if you have exceeded the 4 free training per month. Do you still want to train the 3rd layer NLC? If you still want to, please type exactly \"Yes I do\".\n"%classifiers["classifiers"][-1]["created"])
    else: 
        ask_for_training_NLC="Yes I do"
    if ask_for_training_NLC=="Yes I do":
        # File where the classes will be stored
        namefile_training_classifier="file_training_classifier.csv"
        file_train_NLC=open(namefile_training_classifier,"w+", encoding="utf-8")
        
        # As NLC cannot update the examples of its classes, we need to delete the entire classifier, if we have stored its Past_ID
        print("Updating the classifier of NLC requires deleting the past class to recreate it with the updated .csv file \n")
        for classifier in classifiers["classifiers"]:
            status = natural_language_classifier.delete_classifier(classifier["classifier_id"]).get_result()
            time.sleep(5)
            if status=={}:
                print("The past classifier with id %s was successfully deleted\n"%classifier["classifier_id"])
        
        # We start by importing the intents Oui_MANA and Non_MANA from the chatbot as they are the most relevant pieces to train the classifier of the 3rd layer NLC
        response=assistant.list_intents(
        workspace_id=workspace_id_assistant,
        export=True
        ).get_result()
        
        # As there is no way to automatically export the intents as a .csv through API references, we do it manually by looping through the json and filling the file.
        for intent_looper in range(len(response["intents"])):
            if response["intents"][intent_looper]["intent"]=="Non_MANA" or response["intents"][intent_looper]["intent"]=="Oui_MANA":
                intent=response["intents"][intent_looper]["intent"]
                for examples_looper in range(len(response["intents"][intent_looper]["examples"])):
                    file_train_NLC.write("%s, %s"%(response["intents"][intent_looper]["examples"][examples_looper]["text"].replace('"', ''),intent)+'\n')
                    #print(("texte: %s \n intent: %s\n"%(response["intents"][intent_looper]["examples"][examples_looper]["text"],intent)))

        print("File %s content was updated  with intents\n"%namefile_training_classifier)
        
        # We append to the file already containing the chatbot intents all the articles classified MANA to train the NLC classifier, with limitation of the 1010 first characters (because of Watson NLC technical specs.)
        for mana_articles_looper in range(len(list_already_treated_MANA_articles)):
                file_train_NLC.write("%s, %s"%(list_already_treated_MANA_articles[mana_articles_looper]["text"][0:1010],"Oui_MANA")+'\n')
        print("File %s content was updated  with already classified MANA articles\n"%namefile_training_classifier)
        
        with open('Non_MANA_articles.tsv', encoding="utf8", errors='ignore') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='/')
            line_count = 0
            for row in csv_reader:
                if line_count!=0 and row!=[]:
                    file_train_NLC.write("%s, %s"%(row[3][0:1010],"Non_MANA")+'\n')
                line_count+=1
        print("File %s content was updated  with already classified Non_MANA articles\n"%namefile_training_classifier)
        file_train_NLC.close()
        
        # We train the classifier
        with open(namefile_training_classifier, 'rb') as training_data:
            classifier = natural_language_classifier.create_classifier(
                training_data=training_data,
                metadata='{"name": "MANA_classifier","language": "en"}'
              ).get_result()
        os.rename(namefile_training_classifier, "Classifier_NLC_ID=%s"%classifier["classifier_id"])
        print("New classifier (with ID: %s) was trained\n"%classifier["classifier_id"])
    else: 
        print("Alright the 3rd layer NLC was not updated.")
        
def register_file_Oui_MANA(list_already_treated_MANA_articles):
    with open('Oui_MANA_articles.tsv', 'w+', encoding="utf8") as csvfile:
        fieldnames = ["flag","company","counter_mana_sentences","keyword(s)","sentence(s)","text","sentiment","sadness","disgust","anger","joy","total_sentiment"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, dialect="myDialect")
        writer.writeheader()
        writer.writerows(list_already_treated_MANA_articles)
    print("The file Oui_MANA_articles.tsv was successfully updated with the new articles treated through the current execution of the script.\n")

def print_results_of_this_execution(vector_counters,position_in_the_input_file_of_misclassified_articles,list_confirmed_MANA_keywords):
    #print("This is vectors counter type:%s"%type(vector_counters))
    #print(vector_counters)
    print("Among %d articles treated during this past execution, %d were correctly classified, which represents a ratio of %f %% " %(vector_counters[0],vector_counters[1],100*vector_counters[1]/vector_counters[0]))
    if vector_counters[0]!=vector_counters[1]:
        print("The positions in the input file of the misplaced articles, along with beginning characters of the texts are:")
        print(position_in_the_input_file_of_misclassified_articles)
    list_split_confirmed_MANA_keywords=[]
    for keyword_full in list_confirmed_MANA_keywords:
        split_it=keyword_full.split()
        for keyword_single in split_it:
            list_split_confirmed_MANA_keywords.append(keyword_single)
    count_intermediate = Counter(map(str.lower,list_split_confirmed_MANA_keywords))     
    most_occur = count_intermediate.most_common(20) 
    print("For your information (if you want to manually adjust the entities of the chatbot): in this past execution, the most recurring keywords among the sentences that were validated by the intent Oui_MANA of the Chatbot were:\n")
    print(most_occur,"\n")