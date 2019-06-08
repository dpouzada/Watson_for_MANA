# Watson_for_MANA

Watson AI modules help MANA process thousands of articles to track environmental impact. The specific architecture of this solution make the best use of different Watson modules to achieve an optimized result.

Feel free to reuse and adapt this script to tap into IBM Watson AI processing power with any relevant information in your own field. Only tacit requirement is that it is a purposeful challenge, helping with other environmental or social challenges.

# Challenge definition

MANA’s aim: Be the First citizen platform to collect and valorize data assessing the impact of businesses/corporations on the environment on a global scale. 
How to achieve this goal ?
By treating/processing information (articles, tweets) coming from its unique Network made of:
1500 sources
in 80 languages
=> Enormous amounts of articles to read through
Problem: It is (linearly) costly in time for human beings to read those
Solution: Watson Artificial Intelligence processing power can dramatically reduce the workload 


# How to use the code to create your own “Watson for good” use cases

First and foremost you will need instances of several Watson modules.

Those can all be created entirely FOR FREE on IBM Cloud, giving you access (for free again) for each module to about 10 000 API calls to experiment by yourself, build your own POCs and demos.

# Watson Natural Language Understanding

Allows you to extract Metadata (structured data) from an unstructured text: 
- Sentiment, Emotion
- Keywords
- Entities
- Categories, Concepts
- Syntax
- Semantic Roles

#Watson Assistant

General intro of what it's capable of and what you can do with it

I encourage you to learn how to design your own assistant with ... tutorial

For this project I invite you to import as a starting point the skill MANA_orchestrator.json. It has the right dialog structure, intent and entities definition and it was already trained with about 300 examples per intent. 
You are evidently welcome to make your own modifications to it.

# Watson Natural Language Classifier


