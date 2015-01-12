###
# This CPU heat temperature Script is part from the RaspHardwareStatus (RHS)
# Written and expanded by StealthCoders.net Copyright (C) 2015
###

import os
import smtplib
import time
from email.mime.text import MIMEText
 
### Settings
# SMTP
smtpHost = "MailHost"
smtpPort = 587
smtpUser = "Mail Username"
smtpPassword = "Mail Password"
AUTHREQUIRED = 1 # If there is a Authentication needed just set it to 1
 
# E-Mail
mailSender = "Email which sends the warning"
mailReceiver = "Email which receive the warning"
 
###
# Set here your critical Temp Value
# You can set this Value to 10, for Testing purpose
# This Value is set as Celsius
###
cpuHeatWarning = 65
###

###
# We add a Time and a Date to let you know when this critical value was reached
###
date = "%02i.%02i.%04i" % (int(time.localtime()[2]), int(time.localtime()[1]), int(time.localtime()[0]))
time = "%02i:%02i:%02i" % (int(time.localtime()[3]), int(time.localtime()[4]), int(time.localtime()[5]))
###

###
# Do not change anything from here!
###
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))
 
tempFloat = float(getCPUtemperature())
 
if (tempFloat > cpuHeatWarning):
    server = smtplib.SMTP(smtpHost, smtpPort)
    server.starttls()
    server.login(smtpUser, smtpPassword)
 
    value = "Your Cpu Core Temp is Overheated " + str(tempFloat) + " Celsius." + "\n" + "Time: " + time + " Date: " + date
    msg = MIMEText(value)
    msg['Subject'] = "[Alert!] Raspberry CPU Overheat " + str(tempFloat) + " Celsius!"
    msg['From'] = mailSender
    msg['To'] = mailReceiver
    server.sendmail(mailSender, mailReceiver, msg.as_string())
    server.quit()
