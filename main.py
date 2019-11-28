###################################################################
########             It all starts here       #############
###################################################################

""" 
This code talks to the entire bot Framework. 

"""


import os,string
import time
import datetime
from slack.slack_commands import parse_bot_commands, output_command
from config import slack_client, log_commands_path
from nlp.nlp_commands import handle_command
import pandas as pd
import json

# Initialize with empty value to start the conversation.
user_input = ''
context = {}
current_action = ''
follow_ind = 0
session_df = pd.DataFrame({},columns=['timestamp', 'user', 'context']) #stores the session details of the user
# bot's user ID in Slack: value is assigned after the bot starts up
bot_id = None

# constants
RTM_READ_DELAY = 1 # 1 second delay between reading from RTM

if __name__ == "__main__":
    if slack_client.rtm_connect(with_team_state=False):
        print("Kelly connected and running!")
        
        # Read bot's user ID by calling Web API method `auth.test`
        bot_id = slack_client.api_call("auth.test")["user_id"]
        
        while True:
            user_id,message_user,message,team,channel,start_timestamp  = parse_bot_commands(slack_client.rtm_read(),bot_id) #slack processing
            
            if message: # If a User has typed something in Slack
                try:
                    context = json.loads(session_df.loc[session_df.user == message_user+channel,'context'].values[0])
                except:
                    context = {}
                    session_df = session_df.append({'timestamp': start_timestamp, 'user': message_user+channel, 'context': json.dumps(context)}, ignore_index=True)
                    
                context,slack_output,current_action = handle_command(message,channel, message_user,context) #nlp processing
                session_df.loc[session_df.user == message_user+channel,'context'] = json.dumps(context)
                output_command(channel, slack_output) #slack processing
                conversation_id = context['conversation_id']
                
                try:
                    if context['currentIntent'] in ['anything_else']:
                        follow_ind = 1
                    else:
                        follow_ind = 0
                except:
                    pass
                
                if current_action == 'end_conversation': # Based on the this, the context variables are reset
                    session_df = session_df[session_df.user != message_user+channel]
                    context = {}
                    current_action = ''
                
                end_timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                processing_time = str((datetime.datetime.strptime(end_timestamp, '%Y-%m-%d %H:%M:%S') - datetime.datetime.strptime(start_timestamp, '%Y-%m-%d %H:%M:%S')).total_seconds())
                
                string_to_run = string.Template("""python3 -W ignore "${log_commands_path}" "${user_id}" "${message_user}" "${conversation_id}" "${message}" "${slack_output}" "${team}" "${channel}" "${start_timestamp}" "${end_timestamp}" "${processing_time}" "${follow_ind}" &""").substitute(locals()) #logs processing
                os.system(string_to_run)
                
            time.sleep(RTM_READ_DELAY)
    else:
        print("Connection failed. Exception traceback printed above.")