# AEDAutoEmailer

Project Owner: Shahzeb Malik (smalik@abbotsford.ca)

# Purpose

The purpose of this application is to continually scan a directory for new files and Email them to a preconfigured Email address, relieving the need to manually attach and E-mail files.

# Requirements

* SMTP Server
* Network permission for the server hosting the scan directory to send Emails via SMTP

# Setup 

1) Download the following files:
  * AEDEmailer.exe
  * AEDEmailerConfig.ini
 
2) Create directories for the following purposes (You may name them however you wish):
  *  A directory for the application to scan each interval (AEDAttachment)
  *  A directory for log files to be generated in (AEDLog)
  *  A directory for succesfully Emailed files to be moved into (AEDSuccess)
  *  A directory for Failed files to be moved into (AEDFail)

3) Open the AEDEmailerConfig.ini file in a text editor and update the following values:
   
   Please note that all file paths use a forward slash and they must be closed paths (ie. end with a /)
  * EmailAttachmentsFolderPath || The fully qualified path to the folder that will be scanned
  * SuccessfulFolderPath || The fully qualified path to the folder which will hold all successfully emailed files (Archive)
  * FailureFolderPath || The fully qualified path to the folder which will hold all failed Email files (Archive)
  * LogPath || The fully qualified path to the folder which will hold the log file. A new log file will be generated every time the application is started.
  * ScanInterval || How long the application should wait before rescanning the folder (Milliseconds)
 
  * TLSEnabled || True, False || If TLS is enabled on your SMTP server, set this to true. (Contact your network administrator)
  * LoginRequired || True, False || If your SMTP server required a login, set this to true. (Contact your network administrator)
  * EmailFromAddress || The Sender Email address
  * EmailToAddress || The recipient Email address
  * EmailBody || The content of the Email message
  * SMTPAddress || the SMTP server domain (Contact your network administrator)
  * SMTPPort || The port used to access your SMTP server. Default is 25. (Contact your network administrator)
  * EmailUserName || If login required is set to true, the login username for the SMTP server.
  * EmailPassword || If login required is set to true, the login password for the SMTP server.

Once the fields have been updated, simply close the file and launch the AEDEmailer.exe application

# Advanced

Once you have confirmed that the application is working, you may wish to install the application as a service on your local server.
