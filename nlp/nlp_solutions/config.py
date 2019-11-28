###################################################################
######## Configuration files for Bot   ##########################
###################################################################

"""
    config.py 
    
    This files has all the configurations for your bot.
    
"""

import os
import watson_developer_cloud
from slackclient import SlackClient

location = "/Users/Arvind/Downloads/Movie_Bot/"  # replace with the full folder path where you downloaded the github repo

###################################################################
######## Slack configuration   ##########################
###################################################################

SLACK_BOT_TOKEN='xoxb-762458134353-768410665828-TWM301hVVlAx1EGRTgmui17j'
SLACK_VERIFICATION_TOKEN='g3quhQgS81aDAGoB1XQjl5bR' 

# instantiate Slack client
slack_client = SlackClient(SLACK_BOT_TOKEN) # do not change this parameter

###################################################################
######## Watson service configuration   ##########################
###################################################################

service = watson_developer_cloud.AssistantV1(
    iam_apikey = 'dy3E6rp1EXmi-7TKsiAkDAz23iW5WNnEy7nYkzfBH1qD', # replace with Password
    version = '2018-09-20'
)

workspace_id = '2c1264f9-1510-411b-9988-42e40a5088bd' # replace with Assistant ID

###################################################################
######## Log files configuration   ##########################
###################################################################

log_commands_path = location + "logs/log_commands.py" # do not change this parameter
follow_up_path = location + "logs/followup_email.py" # do not change this parameter

###################################################################
######## Temp files configuration   ##########################
###################################################################

onetime_path = location + "nlp/nlp_solutions/onetime_run_file.py" # do not change this parameter
onetime_file = location + "nlp/nlp_solutions/onetime.txt" # do not change this parameter
