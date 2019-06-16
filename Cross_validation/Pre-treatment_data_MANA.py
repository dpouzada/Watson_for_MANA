#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: daniel pouzada

Script qui s'occuppe de pré-traiter les données des .csv:
    0) Enlever les lignes dupliquées du fichier qui fausseraient complètement la validation croisée
    1) Sélectionne la ligne le champ le plus long pour chaque ligne (correspond au texte))
    2) enlève les liens, caractères spéciaux et vérifie que la taille restante est inférieure à la limite 1024 caractères de NLC
    3) Traduit en anglais si besoin
    4) S'assure après appel à l'api d'identification de langue que c'est bien l'anglais qui est reconnu
    5) Tracke les lignes non inclues car plus de 1024 caractères ou identification anglais non réussie
    6) Reporte les lignes validées dans un .csv 
    
""" 
import csv
import re
from watson_developer_cloud import LanguageTranslatorV3

language_translator = LanguageTranslatorV3(
version='2018-05-01',
url='https://gateway.watsonplatform.net/language-translator/api',
username='4d608cab-6749-42f7-aad7-e6d02306e09b',
password='lcFtABe31AJS',)

#models = language_translator.list_models().get_result()
#print(json.dumps(models, indent=2))

missing_lines=[]

pattern = re.compile('([^\s\w]|_)+')

name_file_to_open="/Users/pouzada/Downloads/rejected-incidents(1).csv"
name_file_to_create="NonMana.csv"
name_classifier=", NonMANA"
name_pretreated_file="/Users/pouzada/MANA_NLC/rejected-incidents.csv"

s = set()
with open(name_pretreated_file, 'w+') as out:
    for line_duplicata in open(name_file_to_open,"r", encoding="utf8", errors='ignore'):
        if line_duplicata not in s:
            out.write(line_duplicata)
            content=line_duplicata.split(';')
            s.add(line_duplicata)
out.close()


f=open(name_file_to_create,"w+")
         
with open(name_pretreated_file, encoding="utf8", errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if len(row)!=0:
                print("line is :",line_count+1)
                #text = re.sub(r'http\S+', '', max(row, key=len))
                text = re.sub(r'http\S+', '', row[3])
                text = pattern.sub('',text)
                if len(text)<1024:
                    language = language_translator.identify(text).get_result()
                    langue=language['languages'][0]['language']
                    if (langue=='en'):
                        classifier_feed=text
                        print(classifier_feed)
                        f.write(classifier_feed+name_classifier+'\n')
                    else:
                        try:
                            classifier_feed = language_translator.translate(text=text,model_id=langue+'-en').get_result()
                            language = language_translator.identify(classifier_feed).get_result()
                            langue=language['languages'][0]['language']
                            if (langue=='en'):
                                print(classifier_feed)
                                f.write(classifier_feed+name_classifier+'\n')
                            else:
                                missing_lines.append('Bad translation in line'+str(line_count))
                        except KeyboardInterrupt:
                            break
                        except:
                            missing_lines.append('line broken'+str(line_count))
                            pass
                else:
                    missing_lines.append("too long string on line:"+str(line_count))
            line_count += 1
    print(f'Processed {line_count} lines.')

f.close()

"""
Si traduction du tout en français plutôt qu'en anglais:
    
                        if(langue=='en'):
                            translation = language_translator.translate(text=text,model_id='en-fr').get_result()
                            classifier_feed=translation['translations'][0]['translation']
                            print("model is:",'en-fr')
                        else:  
                            translation = language_translator.translate(text=text,model_id=langue+'-en').get_result()
                            translation_english=translation['translations'][0]['translation']
                            classifier_feed = language_translator.translate(text=translation_english,model_id='en-fr').get_result()
                            print("model is:",langue,"-fr")
"""                    

