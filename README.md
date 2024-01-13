[![DOI](https://zenodo.org/badge/224627422.svg)](https://zenodo.org/doi/10.5281/zenodo.10499163)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://github.com/kaushikjadhav01/Movie-Recommendation-Chatbot/blob/master/LICENSE)
[![Code Coverage](https://codecov.io/gh/NCSU-Fall-2022-SE-Project-Team-11/XpensAuditor---Group-11/branch/master/graphs/badge.svg)](https://codecov.io)
![GitHub contributors](https://img.shields.io/badge/Contributors-1-brightgreen)
[![Documentation Status](https://readthedocs.org/projects/ansicolortags/badge/?version=latest)](https://github.com/kaushikjadhav01/Movie-Recommendation-Chatbot/edit/master/README.md)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/kaushikjadhav01/Movie-Recommendation-Chatbot)
![GitHub issues](https://img.shields.io/github/issues/kaushikjadhav01/Movie-Recommendation-Chatbot)
![GitHub closed issues](https://img.shields.io/github/issues-closed/kaushikjadhav01/Movie-Recommendation-Chatbot)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/kaushikjadhav01/Movie-Recommendation-Chatbot.svg)](https://img.shields.io/github/repo-size/kaushikjadhav01/Movie-Recommendation-Chatbot.svg)
[![GitHub last commit](https://img.shields.io/github/last-commit/kaushikjadhav01/Movie-Recommendation-Chatbot)](https://github.com/kaushikjadhav01/Movie-Recommendation-Chatbot/commits/master)
![GitHub language count](https://img.shields.io/github/languages/count/kaushikjadhav01/Movie-Recommendation-Chatbot)
[![Commit Acitivity](https://img.shields.io/github/commit-activity/m/kaushikjadhav01/Movie-Recommendation-Chatbot)](https://github.com/kaushikjadhav01/Movie-Recommendation-Chatbot)
[![Code Size](https://img.shields.io/github/languages/code-size/kaushikjadhav01/Movie-Recommendation-Chatbot)](mpp-backend)
![GitHub forks](https://img.shields.io/github/forks/kaushikjadhav01/Movie-Recommendation-Chatbot?style=social)
![GitHub stars](https://img.shields.io/github/stars/kaushikjadhav01/Movie-Recommendation-Chatbot?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/kaushikjadhav01/Movie-Recommendation-Chatbot?style=social)

# Movie-Recommendation-Chatbot
Movie Recommendation Slack chatbot using IBM Watson, nltk, pandas and scikit-learn
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#system-description-and-functions">System Description and Functions</a></li>
    <li><a href="#built-with">Built With</a></li>
    <li><a href="#installation">Installation</a></li>
    <li><a href="#authors">Authors</a></li>
    <li><a href="#links">Links</a></li>
  </ol>
</details>

## System Description and Functions
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

## Built With
![IBM Watson](https://img.shields.io/badge/IBM_Watson-blue?style=for-the-badge&amp;logo=ibm&amp;logoColor=white)
![Slack](https://img.shields.io/badge/Slack-A10E3B?style=for-the-badge&amp;logo=slack&amp;logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-323330?style=for-the-badge&logo=pandas&logoColor=F7DF1E)
![NLTK](https://img.shields.io/badge/NLTK-006699?style=for-the-badge&logo=nltk&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit_learn-E34F26?style=for-the-badge&logo=scikit-learn&logoColor=white)

## Installation
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

## Authors
### Kaushik Jadhav
<ul>
<li>Github: https://github.com/kaushikjadhav01</li>
<li>Medium: https://medium.com/@kaushikjadhav01</li>
<li>LinkedIn: https://www.linkedin.com/in/kaushikjadhav01/</li>
<li>Portfolio: http://kajadhav.me/</li>
<li>Linked In: https://www.linkedin.com/in/kajadhav/
<li>Dev.to: https://dev.to/kaushikjadhav01
<li>Codesignal: https://app.codesignal.com/profile/kaushik_j_vtc
<li>Google Scholar: https://scholar.google.com/citations?user=iRYcFi0AAAAJ
<li>Daily.dev: https://app.daily.dev/kaushikjadhav01
<li>Google devs: https://developers.google.com/profile/u/kaushikjadhav01
<li>Stack Overflow: https://stackoverflow.com/users/21890981/kaushik-jadhav
</ul>

## Links
* [Issue tracker](https://github.com/kaushikjadhav01/Movie-Recommendation-Chatbot/issues)
* [Source code](https://github.com/kaushikjadhav01/Movie-Recommendation-Chatbot)
