Menu

# Watson_for_MANA

Watson AI modules help MANA process thousands of articles to track environmental impact. 
The specific architecture of this solution make the best use of several Watson modules to achieve an optimized result.

Feel free to reuse and adapt this solution to tap into IBM Watson AI processing power within your own field. Create from it your own "Watson for good" use cases to serve purposeful causes, helping tackle other environmental or social challenges.

# Challenge definition

MANA Vox aspires to be the First citizen platform to collect and valorize data assessing the impact of businesses/corporations on the environment on a global scale. 

How to achieve this goal ?

By treating/processing information (articles, tweets) coming from its unique Network made of:

1500 sources
in 80 languages

=> Enormous amounts of articles to read through

Problem: It is (linearly) costly in time for human beings to read the articles

Solution: Watson Artificial Intelligence processing power can dramatically reduce the workload 

# A very general classification problem

In practice this amounts to a very typical classification task.

Image

Now, the requirements of the solution to be designed were:
- As user friendly and transparent as possible insofar as MANA staff is non technical and not comfortable with looking at the code to understand its behaviour, make adaptations or tuning parameters by investigating themselves the output. 
- Highly customizable and monitorable. The aim was to be able to have levers instead of a pure black box model which would work very well only for articles on a specific topic dealt with in the training datasets but not able to adapt when tackling new topics.

To answer with anticipation, the final solution implemented: 
1) explicitly displays on the screen every single major processing done for the user to be able to understand/follow it
2) The final architecture keeps best flexibility possible by optimizing the trade off between the speed of learning and the scaling power of the pure ML approach

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

# Watson Assistant

General intro of what it's capable of and what you can do with it

I encourage you to learn how to design your own assistant with ... tutorial

For this project I invite you to import as a starting point the skill MANA_orchestrator.json. It has the right dialog structure, intent and entities definition and it was already trained with about 300 examples per intent. 
You are evidently welcome to make your own modifications to it.

# Watson Natural Language Classifier


