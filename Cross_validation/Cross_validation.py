#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: pouzada

Script de validation croisée qui:
    1) A partir des fichiers pré-traités OuiMANA.csv et NonMANA.csv, crée number_slices partitions contenant un fichier .csv d'entraînement et un de test
    2) Entraîne les classifiers à partir des fichiers MANA_train_i.csv créés. 
    3) Envoie les fichiers tests MANA_test_i.csv à l'api de classification et collecte les résultats
    4) Supprime les classifiers et itère sur i
    
"""
import csv
import math

number_slices=5

file=open("/Users/pouzada/MANA_NLC/nonMANA.csv","r").readlines(  )
count_nonMana = len(file)
step_nonMana=math.floor(count_nonMana/number_slices)

file=open("/Users/pouzada/MANA_NLC/ouiMANA.csv","r").readlines(  )
count_ouiMana = len(file)
step_ouiMana=math.floor(count_ouiMana/number_slices)

import json
from time import sleep

from watson_developer_cloud import NaturalLanguageClassifierV1

natural_language_classifier = NaturalLanguageClassifierV1(
    iam_apikey='Bb57UFUAPqAy9tTWnTiM4uWfb5j7Dx0umYyi13wpe2wr',
    url='https://gateway.watsonplatform.net/natural-language-classifier/api')



for i in range(number_slices):
    f1=open("MANA_train_"+str(i)+".csv","w+")
    f2=open("MANA_test_"+str(i)+".csv","w+") 
    j=0
    
    with open("/Users/pouzada/MANA_NLC/nonMANA.csv","r") as input:
        for line in input:
            j+=1
            if (j>i*step_nonMana and j<(i+1)*step_nonMana):
                f2.write(line+'\n')
            else:
                f1.write(line+'\n')
    j=0
    with open("/Users/pouzada/MANA_NLC/ouiMANA.csv","r") as input:
        for line in input:
            j+=1
            if (j>i*step_ouiMana and j<(i+1)*step_ouiMana):
                f2.write(line+'\n')
            else:
                f1.write(line+'\n')
    f1.close()
    f2.close()

test_array_values=[]
results_array=[]
results_dictionary={}
conclusion_validation_croisee=[]

for i in range(number_slices):
    results_dictionary[i]=[]
    print("cross validation number"+str(i))
    with open("MANA_train_"+str(i)+".csv", 'rb') as training_data:
      classifier = natural_language_classifier.create_classifier(
        training_data=training_data,
        metadata='{"name": "MANA","language": "en"}'
      ).get_result()
    print(json.dumps(classifier, indent=2))
    
    ID=classifier['classifier_id']
    
    sleep(500)
    
    counter_success=0
    counter_fail=0
    
    k=0
    while (classifier['status']!='Available'):
        classifier = natural_language_classifier.get_classifier(ID).get_result()
        print(k)
        k+=1
    
    with open("/Users/pouzada/MANA_NLC/MANA_test_"+str(i)+".csv","r") as input:
        csv_reader = csv.reader(input, delimiter=',')
        for row in csv_reader:
            if len(row)!=0:
                test_array_values.append(row[1])
                classes = natural_language_classifier.classify(ID, '%s'%row[0]).get_result()
                print(classes['top_class'])
                print(row[1])
                if (' %s'%classes['top_class']==row[1]):
                    print("Réussi")
                    counter_success+=1
                    results_array.append(['Réussi',classes['classes'][0]])
                    results_dictionary[i].append([1,classes['classes'][0]])
                    counter_success+=1
                    
                else:
                    print("Raté")
                    counter_fail+=1
                    results_array.append(['Raté',classes['classes'][0]]) 
                    results_dictionary[i].append([0,classes['classes'][0]])
                    counter_fail+=1
        
    conclusion_validation_croisee.append([counter_fail,counter_success])
    natural_language_classifier.delete_classifier(ID).get_result()
        
for l in range(number_slices):
    print("Test set n°%d: %d articles bien classifiés, %d articles mal classifiés"%(l,conclusion_validation_croisee[l][1],conclusion_validation_croisee[l][0]))


'''

m=0
graph_results={}
for l in range(5):
    counter_success=0
    counter_fail=0
    for s in range(l*75, (l+1)*75):
        if (results_array[s][m]=='Réussi'):
            counter_success+=1
        else:
            counter_fail+=1
    graph_results[l]=[['Mal identifié',counter_fail],['Bien identifié',counter_success]]
    print("Test set n°%d: %d articles bien classifiés, %d articles mal classifiés"%(l,counter_success,counter_fail))

    


Si traitement groupé: appel à l'api de classification par collection. Attention, bug incompréhensible "JSON format error"
    
    test_array_to_send=['']
    test_array_values=[]
    dictionnaire_results=[]
    dictionnaire_results[i]={}
    counter_maximum_classifier=0
    
    with open("MANA_test_"+str(i)+".csv","r") as input:
        csv_reader = csv.reader(input, delimiter=',')
        for row in csv_reader:
            if (counter_maximum_classifier<30):
                if len(row)!=0:
                    counter_maximum_classifier+=1
                    test_array_to_send[0]+="{'text':'%s'}"%row[0]+","
                    test_array_values.append(row[1])
                            
    
    classes = natural_language_classifier.classify_collection(ID, test_array_to_send).get_result()
    
    for k in range(len(classes['collection'])):
        if (classes['collection'][k]['top_class']==test_array_values[k]):
            print("Réussi")
            dictionnaire_results[str(k)]=['Réussi',classes['collection'][k]['classes']]
        else:
            print("Raté")
            dictionnaire_results[str(k)]=['Raté',classes['collection'][k]['classes']]
'''