###########################################################
######## Slack Interface codes   ##########################
###########################################################

"""
    slack_commands.py
    
    This file contains all the slack related processing commands.     

"""

import os
import time
import re
from slackclient import SlackClient
from config import slack_client
import datetime

MENTION_REGEX = "^<@(|[WU].+?)>(.*)"

def parse_bot_commands(slack_events,bot_id):
    """
        Parses a list of events coming from the Slack RTM API to find bot commands.
        If a bot command is found, this function returns a tuple of command and channel.
        If its not found, then this function returns None, None.
    """
    for event in slack_events:
        if event["type"] == "message" and not "subtype" in event:
            user_id, message = parse_direct_mention(event["text"])
            if user_id == bot_id:
                message_user = event['user']
                team = event['team']
                channel = event['channel']
                start_timestamp = datetime.datetime.fromtimestamp(float(event['event_ts'])).strftime('%Y-%m-%d %H:%M:%S')
                return user_id,message_user,message,team,channel,start_timestamp
    return None, None, None, None, None, None

def parse_direct_mention(message_text):
    """
        Finds a direct mention (a mention that is at the beginning) in message text
        and returns the user ID which was mentioned. If there is no direct mention, returns None
    """
    matches = re.search(MENTION_REGEX, message_text)
    # the first group contains the username, the second group contains the remaining message
    return (matches.group(1), matches.group(2).strip()) if matches else (None, None)


def output_command(channel,slack_output):
    """
        Output bot command via the slack channel
    """
    slack_client.api_call(
        "chat.postMessage",
        channel=channel,
        text=slack_output
    )

def file_upload(channel, filename):
    with open(filename,'rb') as file_content:
        slack_client.api_call(
        "files.upload",
        channels=channel,
        file=file_content
        )

def slack_tiles(channel, search_term, title, title_url, image_url):
    attachments_json = [
            {
                "title": title.values[0],
                "title_link": title_url.values[0],
                "image_url": image_url.values[0]
            },
            {
                "title": title.values[1],
                "title_link": title_url.values[1],
                "image_url": image_url.values[1]
            },
            {
                "title": title.values[2],
                "title_link": title_url.values[2],
                "image_url": image_url.values[2]
            }
        ]
  
    # Send a message with the above attachment, asking the user if they want coffee
    slack_client.api_call(
      "chat.postMessage",
      channel=channel,
      text='Recommendations for "' + str(search_term) + '"',
      attachments=attachments_json
    )      
        
def message_buttons(channel, button, url, search_term):
    attachments_json = [
        {
            "text": " ",
            "fallback": "You didn't make a selection",
            "callback_id": "code_search",
            "color": "#3AA3E3",
            "attachment_type": "default",
            "actions": [
                {
                    "name": "code_link",
                    "text": "1. " + button.values[0],
                    "type": "button",
                    "url": url.values[0]
                },
                {
                    "name": "code_link",
                    "text": "2. " + button.values[1],
                    "type": "button",
                    "url": url.values[1]
                },
                {
                    "name": "code_link",
                    "text": "3. " + button.values[2],
                    "type": "button",
                    "url": url.values[2]
                },
                {
                    "name": "code_link",
                    "text": "4. " + button.values[3],
                    "type": "button",
                    "url": url.values[3]
                },
                {
                    "name": "code_link",
                    "text": "5. " + button.values[4],
                    "type": "button",
                    "url": url.values[4]
                }
            ]
        }
    ]

    # Send a message with the above attachment, asking the user if they want coffee
    slack_client.api_call(
      "chat.postMessage",
      channel=channel,
      text=search_term,
      attachments=attachments_json
    )