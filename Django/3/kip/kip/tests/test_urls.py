from django.test import TestCase
from mybackend  import functions
from selenium import webdriver
import re


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class SiteUrlTest(TestCase):
    def test_URLs(self):
        print('%s -------------------------------- URL TEST ------------------------------ %s' % (bcolors.WARNING, bcolors.ENDC))
        # browser = webdriver.Chrome()
        browser = webdriver.Firefox()
        try:

            currentUrl = 'http://127.0.0.1:8000/sitemap.xml'
            browser.get(currentUrl)
            sitemap_content = browser.page_source
            content_list = sitemap_content.split('<loc>')
            for cl in content_list:
                if re.search('</loc', cl):
                    currentUrl = re.split('</loc', cl)[0]

                    browser.get(currentUrl)
                    print('%s - good' % currentUrl)

        except Exception as e:
            e_message = e.message if hasattr(e, 'message') else ','.join(map(str, e.args))
            print('current URL : ', currentUrl)
            print('Error : ', e_message)

        browser.close()
