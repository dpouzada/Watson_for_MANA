# AI for the Environment - Watson for MANA

Watson AI modules help MANA process thousands of articles to track and assess environmental impact of corporations. 
The specific architecture of this solution makes the best use of several Watson modules to achieve an optimized performance for this challenge. With little training (less than 100 articles), a result of more than 90% of correct classification was achieved.

Below is a detailed step by step tutorial to invite you to run by yourself Watson for MANA algorithm. No prior knowledge at all is expected. It is meant to be achievable by anyone and is fully self explanatory, following the same pedagogical principle than for instance OpenClassroom.

Feel free to reuse and adapt this solution to tap into IBM Watson AI processing power within your own field. Create from it your own "Watson for good" use cases to serve purposeful causes, helping tackle other environmental or social challenges.

Menu

## Challenge definition

MANA Vox aspires to be the First citizen platform to collect and valorize data assessing the impact of businesses/corporations on the environment on a global scale. 

Please visit their website at: 

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

# Step by step guide to run the script

First and foremost you will need to instantiate several Watson modules.

Those instances can all be created entirely FOR FREE on IBM Cloud, giving you access for each module to about free 10 000 API calls to experiment by yourself, build your own POCs and demos.

# First step : Create your IBM Cloud account for free



# Watson Natural Language Understanding

In short, this module allows you to extract Metadata (structured data) from an unstructured text: 
- Sentiment, Emotion
- Keywords
- Entities
- Categories, Concepts
- Syntax
- Semantic Roles

Please consult the demo page to visualise by yourself what Watson NLU is capable of doing.

## How to create your own Watson NLU instance

Once you are logged in your IBM account, click on "Catalog" and the "AI section".
Scroll down to Naural Language Understanding and, after having set the region to deploy your service (Frankfurt in my case) you click on Create.

(Pictures here)

Now that you just created your instance, click on Manage and copy the API Key and URL, as you will need to insert them later in the script.

# Watson Assistant

General intro of what it's capable of and what you can do with it

I encourage you to learn how to design your own assistant with ... tutorial

## How to create your own Watson Assistant instance

Analogously yo what we did above with Watson Natural Language undesrtanding, on the "AI" section of the "Catalog", you can create an instance of Watson Assistant (in Frankfurt in my case) and save your credentials: URL and API Key.

Then click on launch Watson Assistant, then on the tab "Skills".
I invite you then to click on "create skill" and then "import skill".

For this project I invite you to import as a starting point the skill MANA_orchestrator.json. It has the right dialog structure, intent and entities definition and it was already trained with about 300 examples per intent. 
You are evidently welcome to make your own modifications to it.

# Watson Natural Language Classifier

What is it ?

Exactly same process as above, create from the catalog your instance (in Frankfurt in my case) and save your credentials.

# Watson Translator

No need to explain hopefully what the translator does. We will need it to treat articles from 80 languages for MANA ! 
Just create an instance and save your credentials, same process.

# Insert your credentials at the beginning of the script 

# How to run the script

As I will explain below, I suggest you start by running this script locally. This will be easier and allow to assess the performance of the solution by yourself.

Once you understand how the script works and trust its performance, I will explain to you how to run a much more compact version directly on IBM Cloud, through what is called a "Cloud function". This is what MANA Vox is currently doing.

## How to run the script locally on your machine

1) Install a Python interpreter if not already the case (Anaconda will do great, and includes the Spyder IDE which comes handy)
2) Install Watson packages by running on the terminal (command line called cmd on Windows): pip install --upgrade "watson-developer-cloud>=2.5.1"
3) Save the scripts on a folder, along with the excel file containing the articles to be treated.
4) On the terminal run the script with the command:
On Linux and MacOS: python script_name
On Windows: py script_name
5) In case you want to stop the script before the end of its execution, type Ctrl+C as the scrit is running on the terminal. All information from articles that had already been processed until that point will then be stored (without any loss) in the appropriate files OuiMANA and NonMANA.

# Follow the execution

A great care was taken such that all that the script does which is interesting for you to understand and follow, is displayed on the terminal during the execution. 

You are invited at the beginning to define your supervision settings, and the number of keywords from NLU that are to be considered.

# How to adapt the script to create your own “Watson for good” use cases

# Acknowledgments

On IBM side, thanks to Ramzi ben Ouagram and Vincent Perrin for allowing the project to develop. Thanks to Alexandre Berthet who supported actively the practical implementation for MANA of this solution, and is working on the improvement to bring it to next level.
On MANA side, thanks to Gabrielle Garmier and Capucine Lebois for their energy and pedagogy in co-desigining this solution together.
