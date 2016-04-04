__author0__ = 'Matthew Ostovarpour'
__author1__ = 'Luis Valenzuela'

import smtplib
import os
import time
from time import gmtime, strftime, localtime

username = 'pythonprogram123@gmail.com'
password = 'python123'
fromaddr = 'pythonprogram123@gmail.com'
toaddrs = 'matt.ostovarpour@gmail.com'
msg = 'Hello!'
download_path = "/home/matthew/Downloads"


def main():
    files = os.listdir(download_path)
    while 1:
        new_files = os.listdir(download_path)

        for file in new_files:
            if file not in files:
                if file.endswith('.crdownload'):#Google Chrome Downloads
                    send_email("New Download", "New file is downloading.")
                elif file.endswith('.partial'):#Internet Explorer Downloads
                    send_email("New Download", "New file is downloading.")
                else:
                    if not file.endswith('.tmp'):
                        files = os.listdir(download_path)
                        send_email("Finished Download", file + " is finished downloading")
        time.sleep(5)


def send_email(subject,message):
    print("Sending Message\n")
    signature = "- PyBot"
    message = 'Subject: %s\n\n%s\n\n%s' % (subject, message, signature)

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(fromaddr, toaddrs, message)
    server.quit()

main()
