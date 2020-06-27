# Movie-Recommendation-Chatbot
The chatbot uses a recommendation engine to suggest <b>similar movies</b> with their IMDB links and posters. In addition, it also provides information about the following properties of the movie input by the user:
<ul>
<li>movie genre</li>
<li>movie plot</li>
<li>revenue</li>
<li>budget</li>
<li>IMDB rating</li>
<li>IMDB site link</li>
</ul>

To give a recommendation of similar movies, Cosine Similarity and TFID vectorizer were used. Slack API was used to provide a Front End for the chatbot. IBM Watson was used to link the Python code for Natural Language Processing with the front end hosted on Slack API. Libraries like nltk, sklearn, pandas and nlp were used to perform Natural Language Processing and cater to user queries and responses. Since the chatbot is hosted on Slack, multiple users can communicate with it at the same time.

# Screenshots
<img src="https://github.com/kaushikjadhav01/Movie-Recommendation-Chatbot/blob/master/screenshots/banner1.PNG">
<img src="https://github.com/kaushikjadhav01/Movie-Recommendation-Chatbot/blob/master/screenshots/banner2.PNG">

Find more screenshots, please visit the screenshots folder Or <a href="https://github.com/kaushikjadhav01/Movie-Recommendation-Chatbot/blob/master/screenshots/screenshots.pdf">click here</a>

# Technical Concepts
<b>Natural Language Processing</b> is a subfield of linguistics, computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data.
Challenges in natural language processing frequently involve speech recognition, natural language understanding, and natural language generation.<br>
More information can be found <a href="https://en.wikipedia.org/wiki/Natural_language_processing">here</a>
<br>
<br>
<b>Pilot</b> is the stage of development where the chatbot is deployed to a small group of users for testing. Pilots are especially critical for chatbots, because unlike a web application, the range of possible user input is unlimited.<br>
More information can be found <a href="https://chatbotsmagazine.com/chatbot-vocabulary-10-chatbot-terms-you-need-to-know-3911b1ef31b4">here</a>
<br>
<br>
<b>Proof of Concept (POC)</b> is the stage of development where the chatbot functions properly so long as the input is artificially constrained. A POC demonstrates the potential. POCs are especially useful for emerging technologies that are not fully understood by stakeholders, like chatbots.<br>
More information can be found <a href="https://chatbotsmagazine.com/chatbot-vocabulary-10-chatbot-terms-you-need-to-know-3911b1ef31b4">here</a>
<br>
<br>
<b>Intent</b>  is the user’s intention. For example, if a user types “show me yesterday’s financial news”, the user’s intent is to retrieve a list of financial headlines. Intents are given a name, often a verb and a noun, such as “showNews”.<br>
More information can be found <a href="https://chatbotsmagazine.com/chatbot-vocabulary-10-chatbot-terms-you-need-to-know-3911b1ef31b4">here</a>
<br>
<br>
<b>Entities</b> modify an intent. For example, if a user types “show me yesterday’s financial news”, the entities are “yesterday” and “financial”. Entities are given a name, such as “dateTime” and “newsType”. Entities are sometimes referred to as slots.<br>
More information can be found <a href="https://chatbotsmagazine.com/chatbot-vocabulary-10-chatbot-terms-you-need-to-know-3911b1ef31b4">here</a>
<br>
<br>
<b>Conversational UI</b> are User interfaces based on human speech, either written or spoken. Conversational UIs don’t use buttons, links or other graphical elements. Many chatbots, including Tangowork, mix conversational UI with graphical UI.<br>
More information can be found <a href="https://chatbotsmagazine.com/chatbot-vocabulary-10-chatbot-terms-you-need-to-know-3911b1ef31b4">here</a>
<br>
<br>


# Technologies Used
<ul>
<li><a href="https://slack.com/intl/en-in/">Slack</a></li>
<li><a href="https://www.ibm.com/watson">IBM Watson</a></li>
<li><a href="https://www.nltk.org/">NLTK</a></li>
<li><a href="https://pypi.org/project/tabulate/">Tabulate</a></li>
<li><a href="https://pandas.pydata.org/">Pandas</a></li>
<li><a href="https://scikit-learn.org/">Scikit-learn</a></li>
<li><a href="https://www.python.org/">Python</a></li>
</ul>

# How to Install and Configure?
This file will walk you through the steps to setup your bot. Download the entire folder and the follow the steps below.<br>
Step 1: Create Slack Bot user
Please follows the instructions in the link below to create a Slack App.

https://github.com/kaushikjadhav01/Movie-Recommendation-Chatbot/blob/master/slack/Create_slack_app.ipynb

Step 2: Create a IBM Watson account and Upload the bot.json workspace
Please follows the instructions in the link below to create a Slack App.

https://github.com/kaushikjadhav01/Movie-Recommendation-Chatbot/blob/master/nlp/IBM_Watson_Conversation_setup.ipynb

Step 3: Install required packages
Install the required packages listed in the requirements.txt file. To install the required packages, please use the code below. I might have missed some packages to include in the requirements.txt file. When you initiate the bot, it might fail that a particular module does not exist. Please install it and then initiate bot again, which will fix the issue.

pip3 install -r requirements.txt

Step 4: Update the config files with the Slack and Watson API details
Please make sure that you modified the API details both for Slack and Watson in the config.py file

Step 5: Download data from source and perform Data Preparation
The data for this example is downloaded from the location below,

https://www.kaggle.com/rounakbanik/movie-recommender-systems/data

Name of the dataset - movies_metadata.csv

Since the dataset size is greater than 25MB, I provided only a snippet here in the data folder. However, the exercise is built on the entire dataset obtained from the source. Please download the data from Kaggle and use it for your practice.

"metadata_prep.csv" will be created after you run the data preparation code which will be later used in nlp models to train the movie recommendation system. The data preparation code is provided below.

https://github.com/kaushikjadhav01/Movie-Recommendation-Chatbot/blob/master/data/Data_Preparation.ipynb

I have uploaded the sample of the data here (metadata_prep_sample.csv).

Step 6: Create "onetime.txt" file
Navigate to the folder where the main.py file resides and execute the code below.

python3 nlp/nlp_solutions/onetime_run_file.py
This will create the "onetime.txt" file automatically. If you need to rename this file, update the name in "config.py" file.

Step 7: Initiate Bot
Navigate to the folder where the main python script exists and run the code below.

python main.py

# Authors
## Kaushik Jadhav
<ul>
<li>Github:https://github.com/kaushikjadhav01</li>
<li>Medium:https://medium.com/@kaushikjadhav01</li>
<li>LinkedIn:https://www.linkedin.com/in/kaushikjadhav01/</li>
<li>Portfolio:http://kaushikjadhav01.github.io/</li>
</ul>
