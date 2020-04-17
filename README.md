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

A few machine learning modules were used to build the recommendation engine and Slack API was used to provide the front end. Since the chatbot is hosted on Slack, multiple users can communicate with it at the same time.

# Note
Find how the project looks in screenshots folder Or <a href="https://github.com/kaushikjadhav01/Movie-Recommendation-Chatbot/blob/master/screenshots/screenshots.pdf">click here</a>

# Technologies Used
<li><a href="https://slack.com/intl/en-in/">Slack</a></li>
<li><a href="https://www.ibm.com/watson">IBM Watson</a></li>
<li><a href="https://docs.anaconda.com/anaconda/navigator/">Anaconda Navigator</a></li>
<li><a href="https://pypi.org/project/tabulate/">Tabulate</a></li>
<li><a href="https://pandas.pydata.org/">Pandas</a></li>

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


