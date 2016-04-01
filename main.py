__author0__ = 'Matthew Ostovarpour'
__author1__ = 'Luis Valenzuela'

import smtplib
import os
import time
from time import gmtime, strftime, localtime

username = 'pythonprogram123@gmail.com'
password = 'python123'
fromaddr = 'pythonprogram123@gmail.com'
toaddrs = 'lav62@nau.edu'
msg = 'Hello!'

def main():
    files = os.listdir("C:\\Users\\lav62\\Downloads")
    while(1):
        newFiles = os.listdir("C:\\Users\\lav62\\Downloads")

        for newFile in newFiles:
            if newFile not in files:
                if newFile.endswith('.crdownload'):
                    doneTextSend("New file named " + newFile + " ")





def doneTextSend(message):

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()

doneTextSend()