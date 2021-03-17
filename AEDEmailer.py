###################
## XML Exporter
###################

from datetime import datetime
from email.mime.text import MIMEText
import configparser
import os
import sys
import threading
import datetime
import time
import smtplib
import string
import subprocess
import mimetypes
import shutil
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication



#############################
## INITIALIZE CONFIG PARSER
#############################
name = 'AEDEmailerConfig.ini'

print("Initializing...")
#Looks through the computer for the full path of the above files location and stores it in a variable.
for root, dirs, files in os.walk("C:\\"):
        if name in files:
            configFileDir = os.path.abspath(os.path.join(root, name))
            break

#Initialize an Instance of the config file parser.
config = configparser.ConfigParser()

#Read the config file to the instance of the config parser.
config.read(configFileDir)

####################################
##READ GLOBAL VARIABLES FROM CONFIG
####################################

EmailAttachmentsFolderPath = str(config['AEDEmailer-config']['EmailAttachmentsFolderPath'])
SuccessfulFolderPath = str(config['AEDEmailer-config']['SuccessfulFolderPath'])
FailureFolderPath = str(config['AEDEmailer-config']['FailureFolderPath'])
LogPath = str(config['AEDEmailer-config']['LogPath'])
ScanInterval = int(config['AEDEmailer-config']['ScanInterval'])


TLSEnabled = str(config['AEDEmailer-Email']['TLSEnabled'])
LoginRequired = str(config['AEDEmailer-Email']['LoginRequired'])
EmailFromAddress = config['AEDEmailer-Email']['EmailFromAddress']
EmailToAddress = config['AEDEmailer-Email']['EmailToAddress']
EmailBody = str(config['AEDEmailer-Email']['EmailBody'])
SMTPAddress = config['AEDEmailer-Email']['SMTPAddress']
SMTPPort = int(config['AEDEmailer-Email']['SMTPPort'])
EmailUserName = config['AEDEmailer-Email']['EmailUserName']
EmailPassword = config['AEDEmailer-Email']['EmailPassword']

##############################
## PROGRAM GLOBAL VARIABLES
##############################

#Creates a log file with the current date and time used as the filename
logDT = datetime.datetime.now()
logDT = logDT.isoformat()
logDT = logDT.replace(":", ".")
logFileName = str(logDT) + ".txt"
loggingPath = LogPath + logFileName
    

##############################
##PROGRAM FUNCTIONS
##############################


def send_mail(file_name):
        emailRet = str(datetime.datetime.now()) + " || " + file_name + " || .Successful. \n"

        try:
                       msg = MIMEMultipart()
                       msg['From'] = EmailFromAddress
                       msg['To'] = EmailToAddress
                       msg['Subject'] = "AED report attached | " + str(datetime.datetime.now())

                       msg.attach(MIMEText(EmailBody,'plain'))

                       binary_file = MIMEApplication(open(EmailAttachmentsFolderPath+file_name, 'rb').read())
                       binary_file.add_header('Content-Disposition','attachment', filename=file_name)

                       msg.attach(binary_file)

                       mailserv = smtplib.SMTP(SMTPAddress, SMTPPort)
                       if TLSEnabled == "True":
                               mailserv.starttls()
                       if LoginRequired == "True":
                               mailserv.login(EmailUserName, EmailPassword)
                       mailserv.sendmail( EmailFromAddress, EmailToAddress, msg.as_string())
                       mailserv.quit()
        except Exception as e:
                       return str(e)        
        return emailRet
        



###################
## Export
###################


configloc = open(loggingPath, 'a')
configloc.write("Using Configuration File : [" + configFileDir + "] \n")
configloc.close()

print("\n Ready!")
while True:
        
    while len(os.listdir(EmailAttachmentsFolderPath)) != 0:

        for file_name in os.listdir(EmailAttachmentsFolderPath):
                logText = send_mail(file_name)
                logger = open(loggingPath, 'a')
                logger.write(logText)
                logger.close()
                if ".Successful." in logText: 
                        shutil.move(EmailAttachmentsFolderPath+file_name, SuccessfulFolderPath+file_name)
                else:
                        shutil.move(EmailAttachmentsFolderPath+file_name, FailureFolderPath+file_name)

    time.sleep(ScanInterval)

       
