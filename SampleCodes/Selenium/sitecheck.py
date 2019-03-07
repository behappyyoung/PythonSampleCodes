from sys import argv
from sys import exit

script, currentSite = argv

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime
import logging
from email.mime.text import MIMEText
from subprocess import Popen, PIPE
import socket
from seleniumrequests import PhantomJS, Firefox
errorString = ''
formString=''
warningString='\n \n ========= warning / redirect / ========  \n \n '

print(' checking ' +  currentSite)
headString ='\n ====== Checking Domain :  ' + currentSite + ' \n  ===== start : '+ datetime.datetime.now().strftime("%B %d , %H:%M:%S") + '========== \n'
formUrls = {'wp':'/resources/1518-stop-password-sprawl-with-saas-sso?utm_adgroup=SSO_Exact_-_General&utm_region=NA'}


def sendReport(message):
    msg = MIMEText(message)
    msg["From"] = "young.park"
    msg["To"] = "youngparkshc@gmail.com"
    msg["Subject"] = "Form Testing Result : " + currentSite
    p = Popen(["/usr/sbin/sendmail", "-t", "-oi"], stdin=PIPE)
    p.communicate(msg.as_string())


def errorHandling(url, errorName):
    currentError =  " Error connect to ============== " + url
    print(currentError)
    global warningString
    sendReport(' Test Done From '+ socket.gethostname() + headString + ' / \n   ************** ERROR ************** \n  ' + errorName +'  : '  + currentError + warningString)
    exit()


def softErrorHandling(url, referurl, errorName):
    currentError =  " Error connect to === \n " + url +  ' ( From url : ' + referurl + ') \n'
    print(currentError)
    global warningString
    sendReport(' Test Done From '+ socket.gethostname() + headString + ' / \n ******* Conncetion Error ********** \n ' + errorName +' : '  + currentError + warningString)
    exit()

wdriver = Firefox()
# browser = webdriver.Firefox()
##driver = webdriver.PhantomJS()
try:
            checkingUrl = currentSite
            while True:


                response = wdriver.request('GET', checkingUrl)
                # browser.get(checkingUrl)
                if response.status_code == 200 :


                    formString += checkingUrl + '\n'
                else:
                    statusString = checkingUrl + " =====> " + str(response.status_code)
                    print (statusString)
                    ##warningString = '\n ****  '+ warningString + statusString + ' *** \n ' 

                checkingUrl = input("Enter other url to continue... or 'q' to quit      : ")
                if checkingUrl.strip() == 'q':
                    break

except Exception as e:
    e_message = e.message if hasattr(e, 'message') else ','.join(map(str, e.args))
    print(e_message)

wdriver.close()

print(errorString)



