import sys

# currentSite = 'http://' + str(sys.argv[1]) if len(sys.argv) > 1 else 'http://www.daum.net'

from selenium import webdriver
errorString = ''
formString=''
warningString='\n \n ========= warning / redirect / ========  \n \n '


class BColors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# print(' checking %s %s %s '  % (BColors.GREEN, currentSite, BColors.END))

browser = webdriver.Firefox()
try:

    for n in range(50):
        checkingUrl = 'http://www.daum.net'
        browser.get(checkingUrl)
        search_id = browser.find_elements_by_id('q')
        search_id[0].send_keys('문재인응원')
        search_button = browser.find_elements_by_css_selector('button.ico_pctop.btn_search')
        search_button[0].click()

        checkingUrl = 'http://www.naver.com'

        browser.get(checkingUrl)
        search_id = browser.find_elements_by_id('query')
        search_id[0].send_keys('문재인응원')
        search_button = browser.find_elements_by_id('search_btn')
        search_button[0].click()

except Exception as e:
    e_message = e.message if hasattr(e, 'message') else ','.join(map(str, e.args))
    print(e_message)

browser.close()

print(errorString)



