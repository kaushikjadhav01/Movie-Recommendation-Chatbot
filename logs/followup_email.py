###################################################################
########             Follow up email                  #############
###################################################################

"""

   followup_email.py
   
   This is special use case code written to assist bot developers. It consolidates topics that are not familiar to the bot
   and sends it in a nicely formatted email to the developers team. 

"""

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib
import os,string,sys
sys.path.append(os.path.normpath(os.getcwd()))
from config import location

SERVER = " "
FROM = ["xxxx@gmail.com"]
TO = ["xxxx@gmail.com"] # must be a list
SUBJECT = "Follow up questions email"
TEXT = """Hello,

Here are the various questions users asked me today which I have no idea about. Could you help me learn these topics?

Regards,
Kelly
"""

msg = MIMEMultipart()
 
msg['From'] = ", ".join(FROM)
msg['To'] = ", ".join(TO)
msg['Subject'] = SUBJECT
 
body = TEXT

msg.attach(MIMEText(body, 'plain'))

filename = 'followup_file.TXT'
attachment = open(location + 'followup_file.TXT', "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

msg.attach(part)

message = msg.as_string()

server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()