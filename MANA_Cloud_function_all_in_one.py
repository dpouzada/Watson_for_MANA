# main() will be invoked when you Run This Action.
#
# @param Cloud Functions actions accept a single parameter,
#        which must be a text in a JSON object.
# examples:
# params={"text":"Nestlé under fire for marketing claims on baby milk formulas. Exclusive: Report finds Swiss multinational is violating advertising codes and misleading consumers with nutritional claims.  The Swiss multinational Nestlé has been accused of violating ethical marketing codes and manipulating customers with misleading nutritional claims about its baby milk formulas. A new report by the Changing Markets Foundation has found that Nestlé marketed its infant milk formulas as “closest to”, “inspired by” and “following the example of” human breastmilk in several countries, despite a prohibition by the UN’s World Health Organisation (WHO). The study, which analysed over 70 Nestlé baby milk products in 40 countries, also found that Nestlé often ignored its own nutritional advice in its advertising. In South Africa, the firm used sucrose in infant milk formulas, while marketing its Brazilian and Hong Kong formulas as being free of sucrose “for baby’s good health”. In Hong Kong, it promoted its baby milk powders as healthier – because they were free from vanilla flavourings – even as it sold other vanilla-flavoured formulas elsewhere in the territory. Nusa Urbancic, campaigns director for the Changing Markets Foundation told the Guardian: “We have come to understand that companies manipulate consumers’ emotional responses to sell a variety of products, but this behaviour is especially unethical when it comes to the health of vulnerable babies. “If the science is clear that an ingredient is safe and beneficial for babies then such ingredients should be in all products. If an ingredient is not healthy, such as sucrose, then it should be in no products. Nestlé’s inconsistency on this point calls into serious question whether it is committed to science, as it professes to be.” Nestlé is the global market leader for infant milk products with a market share of close to a quarter. It has been dogged by the advertising issue since a 1974 report called The Baby sparked a worldwide boycott. In 1981, the WHO adopted a strict code of advertising banning the promotion of baby milk products as being in any way comparable to breastmilk. Nestle insists that it follows the code “as implemented by national governments”. But the new report finds that it touted products in the US such as Gerber Good Start Gentle powder as “our closest to breastmilk”, and sold its Beba Optipro 1 powder in Switzerland as “following the example of breastmilk”. Similar Nestlé products in Hong Kong and Spain were advertised as being “inspired by human milk”, and having “an identical structure” to breastmilk. The company did not respond to specific questions about the new study but a Nestlé spokesperson told the Guardian it supported WHO recommendations and believed that breastmilk was, wherever possible, “the ideal source of nutrition for babies.” However, not all infants could be breastfed as recommended and “where needed or chosen by parents, we offer high quality, innovative, science-based nutritional products for mothers and infants from conception to two years of age,” the employee said. “We market these products in a responsible way at all times, and the claims made on our products are based on sound scientific evidence.” Some academics, though, have highlighted the way that language used by corporates to promote infant milk formulas can sometimes mislead consumers about this. Last year, Prof George Kent of the University of Hawaii wrote that describing a product as “closer to breastmilk … is not the same as saying it is close to breastmilk. New York is closer than New Jersey to Paris, but that does not mean New York is close to Paris.” Breastmilk is a “personalised” and continuously changing nutrition between mother and child that contains live substances – such as antibodies and immune-system related compounds – which cannot yet be replicated in a lab."}
# params={"text":"PepsiCo, Kellogg's slammed for concealing palm oil secrets. Your favourite packet of chips or muesli bar snack could contain palm oil – a $65 billion industry which is destroying rainforests and threatening the survival of orangutan populations. But it is impossible for consumers to know for certain because popular brands such as PepsiCo (Doritos, Twisties) and Kellogg’s (Cornflakes, Nutri Grain) have refused to reveal to The New Daily which of their products contain palm oil. Environmental advocacy body Greenpeace released a report this week revealing that half of 16 companies that pledged in 2010 to eliminate deforestation from palm oil by 2020 had failed to disclose where they source their palm oil almost 10 years later. Companies are also avoiding listing “palm oil” explicitly in their product ingredients, instead masking it by using other vague terms. For example, Doritos contain “vegetable oil” and Colgate toothpaste has “glycerin” – both of which are terms commonly used to describe palm oil content in ingredient lists.PepsiCo, Kellogg’s, Ferrero (which makes Nutella), Kraft Heinz, Johnson & Johnson, Hershey, PZ Cussons and Smucker’s remain secretive about their sourcing of palm oil. The environmental concerns lie with brands buying palm oil from companies destroying rainforests, home to an array of wildlife. Indonesia lost 24 million hectares of rainforest between 1990 and 2015 – equivalent to 146 football fields worth of rainforest destroyed every hour between 2013 and 2015, according to the report. The Bornean orangutan population has halved since 1999, while a new species of orangutan discovered in Sumatra last year is already endangered. PepsiCo said some of its snack products are cooked in palm oil that is 100 per cent certified by the Roundtable on Sustainable Palm Oil (RSPO). “In Australia, we primarily use sunflower and/or canola oil for cooking our snacks,” a spokeswoman said. “Our entire Smith’s potato chip range has been cooked in sunflower and/or canola oil for a number of years.” Ferrero said it was the first global company in 2015 to source 100 per cent RSPO-certified palm oil. It told The New Daily it was committed to publicly disclosing the full list of mills it sources by May 15. Kellogg’s Australia’s Derek Lau said it was committed to working with all its suppliers to source sustainable and fully traceable palm oil.Meanwhile, eight companies have come clean about where they buy palm oil from. Nestlé (Kit Kat), Unilever (Ben & Jerry’s), Mars (M&M’s), Mondel_z (Cadbury), Colgate-Palmolive, General Mills (Betty Crocker cake mix), Procter & Gamble and Reckitt Benckiser each released details around their palm oil sourcing to provide greater public transparency. But when contacted by The New Daily, the companies still remained tight-lipped about which of their products contained palm oil. Nestle said it used palm oil in “a number of products”, mainly as a cooking oil in its food items. It purchased 420,000 tonnes of palm oil globally in 2016. “Our ambition is for all of the palm oil we use to be produced in an environmentally and socially responsible manner, meeting consumer expectations and ensuring care for people and the planet,” a spokeswoman said. “By 2020, we aim to use 100 per cent responsibly sourced palm oil. We have made significant progress in improving the sustainability of our palm oil sourcing.” Hershey has sourced 100 per cent RSPO-certified palm oil since 2016 and now publicly shares the names of its suppliers. “As a next step, we have committed to achieve 100 per cent traceable and sustainably sourced palm oil that doesn’t contribute to the destruction of wildlife habitat or negatively impact the environment,” it said. Unilever said it is “committed to … sourcing 100 per cent of our agricultural raw materials (including palm oil) sustainably by 2020”. Mars Australia told The New Daily it would not delve into brand specifics regarding palm oil content. The New Daily contacted all of the companies listed in the Greenpeace report. Those not mentioned in the article did not respond by deadline."}
#
# @return is a JSON object 
#
#
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
            emotion=EmotionOptions(document=True)                                  
            )
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
                workspace_id='6d7f9feb-3d05-4c0e-82b5-6c509638648c',
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
                                        #workspace_id = 'a2dd5d22-63b4-4915-aac8-1c4f6fd358f6',
                                        workspace_id='6d7f9feb-3d05-4c0e-82b5-6c509638648c',
                                        input={
                                            'text': sentence_keyword
                                        },
                                        context=response_bot["context"]
                                    ).get_result()
                        if confirmation_bot["output"]["text"]==['OuiMANA']: 
                            # The value of the flag indicated that the 1st layer detected classified the article, i.e. an alerting entity was detected and its sentences were relevant for MANA
                            try:
                                assistant.create_example(
                                    #workspace_id = 'a2dd5d22-63b4-4915-aac8-1c4f6fd358f6',
                                    workspace_id='6d7f9feb-3d05-4c0e-82b5-6c509638648c',
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
                                    #workspace_id = 'a2dd5d22-63b4-4915-aac8-1c4f6fd358f6',
                                    workspace_id='6d7f9feb-3d05-4c0e-82b5-6c509638648c',
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

