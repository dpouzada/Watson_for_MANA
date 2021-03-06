import http.client
import json 

conn = http.client.HTTPSConnection("xxx")
# Test 1 - Article MANA court
payload_1 = "{\"text\":\"PepsiCo, Kellogg's slammed for concealing palm oil secrets. Your favourite packet of chips or muesli bar snack could contain palm oil – a $65 billion industry which is destroying rainforests and threatening the survival of orangutan populations. But it is impossible for consumers to know for certain because popular brands such as PepsiCo (Doritos, Twisties) and Kellogg’s (Cornflakes, Nutri Grain) have refused to reveal to The New Daily which of their products contain palm oil. Environmental advocacy body Greenpeace released a report this week revealing that half of 16 companies that pledged in 2010 to eliminate deforestation from palm oil by 2020 had failed to disclose where they source their palm oil almost 10 years later.\"}"

# Test 2 - Article Non MANA mais avec keywords retenus par le chatbot, classifiés phrases NonMANA
payload_2 = "{\"text\":\"Nestlé under fire for marketing claims on baby milk formulas. Exclusive: Report finds Swiss multinational is violating advertising codes and misleading consumers with nutritional claims.  The Swiss multinational Nestlé has been accused of violating ethical marketing codes and manipulating customers with misleading nutritional claims about its baby milk formulas. A new report by the Changing Markets Foundation has found that Nestlé marketed its infant milk formulas as “closest to”, “inspired by” and “following the example of” human breastmilk in several countries, despite a prohibition by the UN’s World Health Organisation (WHO). The study, which analysed over 70 Nestlé baby milk products in 40 countries, also found that Nestlé often ignored its own nutritional advice in its advertising. In South Africa, the firm used sucrose in infant milk formulas, while marketing its Brazilian and Hong Kong formulas as being free of sucrose “for baby’s good health”. In Hong Kong, it promoted its baby milk powders as healthier – because they were free from vanilla flavourings – even as it sold other vanilla-flavoured formulas elsewhere in the territory. Nusa Urbancic, campaigns director for the Changing Markets Foundation told the Guardian: “We have come to understand that companies manipulate consumers’ emotional responses to sell a variety of products, but this behaviour is especially unethical when it comes to the health of vulnerable babies. “If the science is clear that an ingredient is safe and beneficial for babies then such ingredients should be in all products. If an ingredient is not healthy, such as sucrose, then it should be in no products. Nestlé’s inconsistency on this point calls into serious question whether it is committed to science, as it professes to be.” Nestlé is the global market leader for infant milk products with a market share of close to a quarter. It has been dogged by the advertising issue since a 1974 report called The Baby sparked a worldwide boycott. In 1981, the WHO adopted a strict code of advertising banning the promotion of baby milk products as being in any way comparable to breastmilk. Nestle insists that it follows the code “as implemented by national governments”. But the new report finds that it touted products in the US such as Gerber Good Start Gentle powder as “our closest to breastmilk”, and sold its Beba Optipro 1 powder in Switzerland as “following the example of breastmilk”. Similar Nestlé products in Hong Kong and Spain were advertised as being “inspired by human milk”, and having “an identical structure” to breastmilk. The company did not respond to specific questions about the new study but a Nestlé spokesperson told the Guardian it supported WHO recommendations and believed that breastmilk was, wherever possible, “the ideal source of nutrition for babies.” However, not all infants could be breastfed as recommended and “where needed or chosen by parents, we offer high quality, innovative, science-based nutritional products for mothers and infants from conception to two years of age,” the employee said. “We market these products in a responsible way at all times, and the claims made on our products are based on sound scientific evidence.” Some academics, though, have highlighted the way that language used by corporates to promote infant milk formulas can sometimes mislead consumers about this. Last year, Prof George Kent of the University of Hawaii wrote that describing a product as “closer to breastmilk … is not the same as saying it is close to breastmilk. New York is closer than New Jersey to Paris, but that does not mean New York is close to Paris.” Breastmilk is a “personalised” and continuously changing nutrition between mother and child that contains live substances – such as antibodies and immune-system related compounds – which cannot yet be replicated in a lab.\"}"

# Test 3 - Article Non MANA écourté, pas de keywords retenus par le chatbot
payload_3 = "{\"text\":\"Nestle under fire for marketing claims on baby milk formulas. Exclusive: Report finds Swiss multinational is violating advertising codes and misleading consumers with nutritional claims.  The Swiss multinational Nestle has been accused of violating ethical marketing codes and manipulating customers with misleading nutritional claims about its baby milk formulas.\"}"

# Test 4 - Article ne comprenant pas une entité company - donc rejeté
payload_4 = "{\"text\":\"This is a test with no company, hence discarded without being treated.\"}"

# Test 5 : Article MANA relativement long
payload_5 = "{\"text\":\"A Greenpeace investigation has exposed how the world’s biggest brands are still linked to rainforest destruction in Indonesia.Palm oil suppliers to the world’s largest brands, including Unilever, Nestlé, Colgate-Palmolive and Mondelez, have destroyed an area of rainforest almost twice the size of Singapore in less than three years, according to the report.Greenpeace International assessed deforestation by 25 major palm oil producers and found that:25 palm oil groups had cleared over 130,000ha of rainforest since the end of 201540% of deforestation (51,600ha) was in Papua, Indonesia – one of the most biodiverse regions on earth and until recently untouched by the palm oil industry12 brands were sourcing from at least 20 of the palm oil groups: Colgate-Palmolive, General Mills, Hershey, Kellogg’s, Kraft Heinz, L’Oreal, Mars, Mondelez, Nestlé, PepsiCo, Reckitt Benckiser and UnileverWilmar, the world’s largest palm oil trader, was buying from 18 of the palm oil groupsThe investigation exposes the total failure of Wilmar International, the world’s largest palm oil trader, to break its links to rainforest destruction. In 2013, Greenpeace International revealed that Wilmar and its suppliers were responsible for deforestation, illegal clearance, fires on peatland and extensive clearance of tiger habitat. Later that year, Wilmar announced a groundbreaking ‘no deforestation, no peat, no exploitation’ policy. Yet Greenpeace’s analysis found that Wilmar still gets its palm oil from groups that are destroying rainforests and stealing land from local communities.In addition to deforestation, the 25 individual cases in the report include evidence of exploitation and social conflicts, illegal deforestation, development without permits, plantation development in areas zoned for protection and forest fires linked to land clearance. It is also the most comprehensive assessment of deforestation in Papua, Indonesia.Palm oil impacts on environment, people and climateHalf of the Bornean orangutan population has been wiped out in just 16 years, with habitat destruction by the palm oil industry a leading driver. More than three-quarters of Tesso Nilo national park, home to tigers, orangutans and elephants, has been converted into illegal palm oil plantations. Globally, 193 Critically Endangered, Threatened and Vulnerable species are threatened by palm oil production.The plantation sector – palm oil and pulp – is the single largest driver of deforestation in Indonesia. Around 24 million hectares of rainforest was destroyed in Indonesia between 1990 and 2015, according to official figures released by the Indonesian government [1].Deforestation and peatland destruction are major sources of greenhouse gas emissions which contribute to climate change. This has pushed Indonesia into the top tier of global emitters, alongside the United States of America and China.Plantation development is a root cause of Indonesia’s forest and peatland fires. In July 2015, devastating blazes spread in Sumatra, Kalimantan and Papua. These fires produced a haze that affected millions of people across Southeast Asia. Researchers at Harvard and Columbia Universities estimate that the smoke from 2015 Indonesian fires may have caused 100,000 premature deaths. The World Bank calculated the cost of the disaster at USdollars16bn.Wilmar International and other palm oil companies are regularly accused of exploiting workers, children and local communities.\"}"

# Test 6 : Article MANA trop long, erreur du serveur 504 Gateway Timeout, que je ne sais pas comment débugger
payload_6 = "{\"text\":\"PepsiCo, Kellogg's slammed for concealing palm oil secrets. Your favourite packet of chips or muesli bar snack could contain palm oil – a $65 billion industry which is destroying rainforests and threatening the survival of orangutan populations. But it is impossible for consumers to know for certain because popular brands such as PepsiCo (Doritos, Twisties) and Kellogg’s (Cornflakes, Nutri Grain) have refused to reveal to The New Daily which of their products contain palm oil. Environmental advocacy body Greenpeace released a report this week revealing that half of 16 companies that pledged in 2010 to eliminate deforestation from palm oil by 2020 had failed to disclose where they source their palm oil almost 10 years later. Companies are also avoiding listing “palm oil” explicitly in their product ingredients, instead masking it by using other vague terms. For example, Doritos contain “vegetable oil” and Colgate toothpaste has “glycerin” – both of which are terms commonly used to describe palm oil content in ingredient lists.PepsiCo, Kellogg’s, Ferrero (which makes Nutella), Kraft Heinz, Johnson & Johnson, Hershey, PZ Cussons and Smucker’s remain secretive about their sourcing of palm oil. The environmental concerns lie with brands buying palm oil from companies destroying rainforests, home to an array of wildlife. Indonesia lost 24 million hectares of rainforest between 1990 and 2015 – equivalent to 146 football fields worth of rainforest destroyed every hour between 2013 and 2015, according to the report. The Bornean orangutan population has halved since 1999, while a new species of orangutan discovered in Sumatra last year is already endangered. PepsiCo said some of its snack products are cooked in palm oil that is 100 per cent certified by the Roundtable on Sustainable Palm Oil (RSPO). “In Australia, we primarily use sunflower and/or canola oil for cooking our snacks,” a spokeswoman said. “Our entire Smith’s potato chip range has been cooked in sunflower and/or canola oil for a number of years.” Ferrero said it was the first global company in 2015 to source 100 per cent RSPO-certified palm oil. It told The New Daily it was committed to publicly disclosing the full list of mills it sources by May 15. Kellogg’s Australia’s Derek Lau said it was committed to working with all its suppliers to source sustainable and fully traceable palm oil.Meanwhile, eight companies have come clean about where they buy palm oil from. Nestlé (Kit Kat), Unilever (Ben & Jerry’s), Mars (M&M’s), Mondel_z (Cadbury), Colgate-Palmolive, General Mills (Betty Crocker cake mix), Procter & Gamble and Reckitt Benckiser each released details around their palm oil sourcing to provide greater public transparency. But when contacted by The New Daily, the companies still remained tight-lipped about which of their products contained palm oil. Nestle said it used palm oil in “a number of products”, mainly as a cooking oil in its food items. It purchased 420,000 tonnes of palm oil globally in 2016. “Our ambition is for all of the palm oil we use to be produced in an environmentally and socially responsible manner, meeting consumer expectations and ensuring care for people and the planet,” a spokeswoman said. “By 2020, we aim to use 100 per cent responsibly sourced palm oil. We have made significant progress in improving the sustainability of our palm oil sourcing.” Hershey has sourced 100 per cent RSPO-certified palm oil since 2016 and now publicly shares the names of its suppliers. “As a next step, we have committed to achieve 100 per cent traceable and sustainably sourced palm oil that doesn’t contribute to the destruction of wildlife habitat or negatively impact the environment,” it said. Unilever said it is “committed to … sourcing 100 per cent of our agricultural raw materials (including palm oil) sustainably by 2020”. Mars Australia told The New Daily it would not delve into brand specifics regarding palm oil content. The New Daily contacted all of the companies listed in the Greenpeace report. Those not mentioned in the article did not respond by deadline.\"}"

headers = {
'content-type': "application/json",
'accept': "application/json"
}

# Variable résultat avec l'ensemble des jsons
output_jsons_of_tests=[]
# Compteur de test
counter_test=0

# Boucle pour parcours l'ensemble des tests
for payload in [payload_1, payload_2, payload_3, payload_4, payload_5, payload_6]:
    # On incrémente le compteur
    counter_test=counter_test+1
    print("Test with payload number %d : \n"%counter_test)
    print("Input payload sent: %s\n"%payload)
    
    # On envoie une requete sur l'api contenant le texte courant
    conn.request("POST", "/MANAapi/Manaclassification", payload.encode('utf-8'), headers)
    # On demande la réponse à la requete
    res = conn.getresponse()
    # On lit la réponse
    data = res.read()
    # Si le statut de la réponse est négatif (!=200)
    if res.status != 200:
        conn = http.client.HTTPSConnection("xxx",timeout=45)
        # On split notre texte en phrase
        tmp = payload.split('.') 
        # On enlève le dernier élément correspondant à ' "} '
        tmp.remove(tmp[len(tmp)-1])
        # On sauvegarde le nombre de phrases
        L = len(tmp)
        # On fait une boucle tant que la requete n'obtient pas une réponse positive (=200)
        # Ou que le nombre de phrases est supérieur à 0 
        # On décremente une phrase du texte a chaque tour de boucle
        while ((L>0) & (res.status != 200)):
            # On décremente le nombre de phrases 
            L = L - 1
            print("Test avec "+str(L)+" phrases du texte")
            # On assemble l'ensemble des phrases restantes
            payload1 = ''
            for i in tmp[0:L]:
                payload1 = payload1 + i + '.'
            payload1 = payload1 + '"}'
            # On tente d'envoyer une requete, d'obtenir la réponse et de la lire
            try :
                conn.request("POST", "/MANAapi/Manaclassification", payload1.encode('utf-8'), headers)
                res= conn.getresponse()
                data = res.read()
            # Si cela ne fonctionne pas, on continue 
            except :
                continue
        
        # Une fois que la réponse est positive on charge la réponse dans un json
        output_json=json.loads(data.decode("utf-8"))
        # on modifie le texte pour l'affichage
        output_json['text']=output_json['text'].replace("\"","\"")
        
        # Le texte n'a été traité que pour un certain nombre de phrases
        # Donc on traite l'autre partie du texte
        # On assemble l'ensemble des phrases restantes
        payload2 = '{"text":"'
        for i in tmp[L:len(tmp)]:
            payload2 = payload2 + i + '.'
        payload2 = payload2 + '"}'
        # On envoie la requete, lit la réponse
        conn.request("POST", "/MANAapi/Manaclassification", payload2.encode('utf-8'), headers)
        res= conn.getresponse()
        data = res.read()
        # On charge la réponse dans un json
        output_json2 = json.loads(data.decode("utf-8"))
        # on modifie le texte pour l'affichage
        output_json2['text']=output_json2['text'].replace("\"","\"")
        # On assemble le texte de la réponse ayant le moins de phrases à celle en ayant le plus
        if L > len(tmp) - L : 
            output_json['text']=output_json['text']+output_json2['text']
        else :
            output_json2['text']=output_json['text']+output_json2['text']
            output_json = output_json2
    # Si la réponse est positive
    else : 
        # On charge la réponse
        output_json=json.loads(data.decode("utf-8"))
        output_json['text']=output_json['text'].replace("\"","\"")

    print("Output json returned: %s\n"%output_json)
    # on charge la réponse dans la variable de résultats    
    output_jsons_of_tests.append(output_json)

