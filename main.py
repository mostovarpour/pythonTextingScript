__author__ = 'Luis Valenzuela'

import smtplib
import time
from time import gmtime, strftime, localtime

username = 'pythonprogram123@gmail.com'
password = 'python123'
fromaddr = 'pythonprogram123@gmail.com'
toaddrs = 'lav62@nau.edu'
msg = 'Hello!'


def doneTextSend():

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()


doneTextSend()