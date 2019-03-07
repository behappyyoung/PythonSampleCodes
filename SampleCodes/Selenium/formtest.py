from sys import argv
from sys import exit

script, checksite, checkform = argv

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

currentSite =  checksite
print(' checking ' +  currentSite)
headString ='\n ====== Checking Domain :  ' + currentSite + ' \n ===== Checking form :   ' + checkform + ' \n ===== start : '+ datetime.datetime.now().strftime("%B %d , %H:%M:%S") + '========== \n'
formUrls = {'wp':'/resources/1518-stop-password-sprawl-with-saas-sso?utm_adgroup=SSO_Exact_-_General&utm_region=NA'}


def sendReport(message):
    msg = MIMEText(message)
    msg["From"] = "young.park"
    msg["To"] = "behappycentrify@gmail.com"
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


def solutionFormTest(checkingURL):
    print('young', checkingURL)
    driver.get(checkingURL)
    driver.find_elements_by_id('prospect_first_name')[0].send_keys('Young Park QA')
    driver.find_elements_by_id('prospect_last_name')[0].send_keys('Please Ignore @#@')
    driver.find_elements_by_id('prospect_job_title')[0].send_keys('Marketing')
    driver.find_elements_by_id('prospect_email')[0].send_keys('ignore-selenium@centrify.com')
    driver.find_elements_by_id('prospect_phone_number')[0].send_keys('669-444-5297')
    driver.find_elements_by_id('prospect_street_address')[0].send_keys('Centrify')
    driver.find_elements_by_id('select2-chosen-2')[0].send_keys(Keys.RETURN)

    ##thankyou = driver.find_elements_by_css_selector('.landing-page .content-channel h2')[0].text
    ##print thankyou
    return


def contactFormTest(checkingURL):
    print('young', checkingURL)
    try:
        driver.get(checkingURL)
        driver.find_elements_by_id('firstName')[0].send_keys('Young Park QA')
        driver.find_elements_by_id('lastName')[0].send_keys('Please Ignore @#@')
        driver.find_elements_by_id('title')[0].send_keys('Marketing')
        driver.find_elements_by_id('email')[0].send_keys('ignore-selenium@centrify.com')
        driver.find_elements_by_id('phone')[0].send_keys('669-444-5297')
        driver.find_elements_by_id('company')[0].send_keys('Centrify')
        driver.find_elements_by_id('s2id_autogen1')[0].send_keys(Keys.RETURN)
        driver.find_elements_by_id('s2id_autogen1_search')[0].send_keys('United States')
        driver.find_elements_by_id('s2id_autogen1_search')[0].send_keys(Keys.RETURN)
        driver.find_elements_by_id('s2id_autogen2')[0].send_keys(Keys.RETURN)
        driver.find_elements_by_id('s2id_autogen2_search')[0].send_keys('California')
        driver.find_elements_by_id('s2id_autogen2_search')[0].send_keys(Keys.RETURN)
        ##s2id_autogen3_search
        ##driver.find_elements_by_css_selector('.tabCompTR .tabCompTD .divCompList')[0].click()
        thankyou = driver.find_elements_by_css_selector('.landing-page .content-channel h2')[0].text
        print(thankyou)
    except Exception as exception:
        print(type(exception).__name__ , 'input error ' , checkingURL)
    return


def identityFormTest(checkingURL):
    print('young identity', checkingURL)
    try:
        driver.get(checkingURL)
        driver.find_elements_by_id('firstName')[0].send_keys('Young Park QA')
        driver.find_elements_by_id('lastName')[0].send_keys('Please Ignore @#@')
        driver.find_elements_by_id('title')[0].send_keys('Marketing')
        driver.find_elements_by_id('email')[0].send_keys('ignore-selenium@centrify.com')
        driver.find_elements_by_id('phone')[0].send_keys('669-444-5297')
        driver.find_elements_by_id('company')[0].send_keys('Centrify')
        driver.find_elements_by_id('s2id_autogen1')[0].send_keys(Keys.RETURN)
        driver.find_elements_by_id('s2id_autogen1_search')[0].send_keys('United States')
        driver.find_elements_by_id('s2id_autogen1_search')[0].send_keys(Keys.RETURN)
        driver.find_elements_by_id('s2id_autogen2')[0].send_keys(Keys.RETURN)
        driver.find_elements_by_id('s2id_autogen2_search')[0].send_keys('California')
        driver.find_elements_by_id('s2id_autogen2_search')[0].send_keys(Keys.RETURN)
        driver.find_elements_by_id('s2id_autogen3')[0].send_keys(Keys.RETURN)
        driver.find_elements_by_id('s2id_autogen3_search')[0].send_keys('North America West')
        driver.find_elements_by_id('s2id_autogen3_search')[0].send_keys(Keys.RETURN)
        driver.execute_script("document.getElementById('accept_eula').style.display='inline-block';")
        driver.find_elements_by_id('accept_eula')[0].click()
        driver.find_elements_by_css_selector('.tabCompTR .tabCompTD .divCompList')[0].click()
        thankyou = driver.find_elements_by_css_selector('.landing-page .content-channel h2')[0].text
        print(thankyou)
    except Exception as exception:
        print(type(exception).__name__ , 'input error ' , checkingURL )
    return


def serverFormTest(checkingURL):
    print('young', checkingURL)
    try:
        driver.get(checkingURL)
        driver.find_elements_by_id('firstName')[0].send_keys('Young Park QA')
        driver.find_elements_by_id('lastName')[0].send_keys('Please Ignore @#@')
        driver.find_elements_by_id('title')[0].send_keys('Marketing')
        driver.find_elements_by_id('email')[0].send_keys('ignore-selenium@centrify.com')
        driver.find_elements_by_id('phone')[0].send_keys('669-444-5297')
        driver.find_elements_by_id('company')[0].send_keys('Centrify')
        driver.find_elements_by_id('s2id_autogen1')[0].send_keys(Keys.RETURN)
        driver.find_elements_by_id('s2id_autogen1_search')[0].send_keys('United States')
        driver.find_elements_by_id('s2id_autogen1_search')[0].send_keys(Keys.RETURN)
        driver.find_elements_by_id('s2id_autogen2')[0].send_keys(Keys.RETURN)
        driver.find_elements_by_id('s2id_autogen2_search')[0].send_keys('California')
        driver.find_elements_by_id('s2id_autogen2_search')[0].send_keys(Keys.RETURN)

        ###driver.find_elements_by_css_selector('.tabCompTR .tabCompTD .divCompList')[0].click()

        ##raw_input("Press Enter to continue...")
        thankyou = driver.find_elements_by_css_selector('.landing-page .content-channel h2')[0].text
        print(thankyou)
    except Exception as exception:
        print( type(exception).__name__ , 'input error ' , checkingURL  )
    return
driver = webdriver.Firefox()
##driver = webdriver.PhantomJS()
try:
            
            subdriver = PhantomJS()    
    
            
            while True:
                if checkform in formUrls:
                        formURL = formUrls[checkform]
                else:
                        formURL = checkform
                        
                if 'resources' in formURL:
                    checkform = 'contact'
                elif 'server-suite-form' in formURL or 'mac-form' in formURL:
                    checkform = 'server'
                elif 'privilege-service-form' in formURL or 'identity-service-form' in formURL:
                    checkform = 'identity'
                elif 'solutions' in formURL:
                    checkform = 'solutions'
                else:
                    checkform ='contact'
                    
                checkingUrl = currentSite + formURL    
              
                response = subdriver.request('GET',  checkingUrl )
                print(checkingUrl, response.status_code, checkform)
                if response.status_code == 200 :
                    
                    if checkform=='identity':
                        identityFormTest(checkingUrl)    
                    elif checkform =='server':
                        print(checkform)
                        serverFormTest(checkingUrl)
                    elif checkform =='solutions':
                        # print checkform
                        solutionFormTest(checkingUrl)
                    elif checkform =='contact':
                        # print checkform
                        contactFormTest(checkingUrl)
                    else:
                        print('no form checking ')

                    formString += checkingUrl + '\n'
                else:
                    statusString = checkingUrl + " =====> " + str(response.status_code)
                    print (statusString)
                    ##warningString = '\n ****  '+ warningString + statusString + ' *** \n ' 
                    
                n = raw_input("Enter other form to continue... or 'q' to quit      : ")
                if n.strip() == 'q':
                    break
                else:
                    checkform = n
                
            subdriver.quit()

except Exception as exception:
    subdriver.quit()
    errorHandling(checkform,  type(exception).__name__)

driver.close()

print(errorString)

if errorString == '' :
    errorString =  formString + '\n  forms are working fine \n \n'

sendReport(' Test Done From '+ socket.gethostname() +' /  Finished : ' + datetime.datetime.now().strftime("%B %d , %H:%M:%S") + ' \n ' + headString + errorString + warningString )



