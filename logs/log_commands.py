#######################################################################
######## Log of chat transaction between user and bot   #############
#######################################################################

"""

    log_commands.py
    
    This file captures all the conversation between User and bot and stores it in a log file (log_file.TXT). 
    Also when the bot does not understand a user question, it writes the question to a follow up log file which 
    can be sent user email if needed.

"""

import os,string,sys
sys.path.append(os.path.normpath(os.getcwd()))
import datetime
import re
import pandas as pd
from config import follow_up_path, location
from dateutil.relativedelta import relativedelta
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')

def process_log(log_line):
    
    with open(location + 'log_file.TXT', 'a') as f:
        f.write(log_line)
        
def followup_questions(log_line):
    
    with open(location + 'followup_file.TXT', 'a') as f:
        f.write(log_line)
    
if __name__ == "__main__":
    
    user_id = sys.argv[1]
    message_user = sys.argv[2]
    conversation_id = sys.argv[3]
    message = sys.argv[4]
    slack_output = sys.argv[5]
    team = sys.argv[6]
    channel = sys.argv[7]
    start_timestamp = sys.argv[8]
    end_timestamp = sys.argv[9]
    processing_time = sys.argv[10]
    follow_ind = sys.argv[11]
    
    log_line = user_id + '|' + message_user + '|' + conversation_id + '|' + message + '|' + REPLACE_BY_SPACE_RE.sub('',slack_output.replace('\n',',')) + '|' + team + '|' + channel + '|' + start_timestamp + '|' + end_timestamp + '|' + processing_time + '|' + follow_ind + '\n'
    
    process_log(log_line)
    
    if follow_ind == '1':
        followup_questions(message + '\n')
    