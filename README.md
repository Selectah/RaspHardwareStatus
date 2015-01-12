## Introduction

RaspHardwareStatus is a free opensource Project for Raspberry Pi Users. 
It shows every important Hardwareinformations e.g Load, Temp, Balance, Usage
You can Modify all Scripts but don't Remove Author Credits.

## Requirements

+ Platform: Raspbian
+ Python: 2.7.3 or higher (Tested on 2.7.3 and above)
+ OpenSSL: 1.0.0
+ GCC: 4.6.3 and above (Linux only)



## Install

[SETTING UP CPU OVERHEAT MAIL WARNING]

The first Part is a little HowTo to setting up tempwarning.py

Install all those Packets

apt-get install lm-sensors sensors-applet

apt-get install bc sendEmail

apt-get install libnet-ssleay-perl libio-socket-ssl-perl

[Some of them are optional but not bad to have, if you modify our script]

Place "tempwarning.py" in a Directory you like, but be careful better do not place this python file in a web directory just for security reasons.
After that just add a new crontab

type in your console: crontab -e

Place this Line at the Bottom of your crontab Editor

*/10 * * * * python /RELATIVE/PATH/TO/YOUR/PYTHON/FILE/tempwarning.py >/dev/null 2>&1

Be sure to add the relative path to the tempwarning.py
This crontab will execute the tempwarning.py every 10minutes, you can modify this time as you like. Just google "Howto Crontab"

Save the File with <Ctrl+X> and Hit Y or J after that <Hit Enter>

You're done!

[MORE TOOLS AND WEBFEATURES WILL BE MADE AS SOON AS POSSIBLE]

## FAQ

I've got no Emails, what can i do?
- Open tempwarning.py and search "cpuHeatWarning = 65"
- Replace the Celsius value to 10 and save the File
- Go to your console and type: python tempwarning.py (you must be in the same directory as the file is)
- You should receive a Alert Email. If you got one, just edit tempwarning.py again and set the Celsius Value back to 65
- This Pythonfile does not send an Email before your Cpu core reaches more than 65 Celsius.
